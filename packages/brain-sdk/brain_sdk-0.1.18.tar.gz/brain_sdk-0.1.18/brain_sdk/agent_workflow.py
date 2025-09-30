import asyncio
import inspect
import json
import sys
import time
import uuid
from datetime import datetime
from typing import Any, Callable, Optional

from brain_sdk.agent_utils import AgentUtils
from brain_sdk.execution_context import ExecutionContext
from brain_sdk.logger import log_track, log_fire, log_debug, log_warn, log_error
from brain_sdk.pydantic_utils import convert_function_args, should_convert_args
from pydantic import ValidationError


class AgentWorkflow:
    """
    Handles workflow tracking functionality for Agent instances.

    This class manages execution tracking, notifications, and workflow management
    for agent reasoner calls and cross-agent communications.
    """

    def __init__(self, agent_instance):
        """
        Initialize the workflow handler with a reference to the agent instance.

        Args:
            agent_instance: The Agent instance this workflow handler belongs to
        """
        self.agent = agent_instance

    def generate_execution_id(self) -> str:
        """Generate a unique execution ID."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_id = uuid.uuid4().hex[:8]
        return f"exec_{timestamp}_{unique_id}"

    def replace_function_references(
        self, original_func: Callable, tracked_func: Callable, func_name: str
    ) -> None:
        """
        Comprehensively replace all references to original function with tracked version.

        This ensures that direct calls like `await analyze_sentiment()` use the tracked
        version instead of bypassing workflow tracking.
        """
        try:
            # 1. Replace in agent instance
            setattr(self.agent, func_name, tracked_func)

            # 2. Replace in caller's module globals
            try:
                frame = sys._getframe(2)  # Get caller's frame (skip decorator frame)
                if func_name in frame.f_globals:
                    frame.f_globals[func_name] = tracked_func
                    if self.agent.dev_mode:
                        log_debug(f"SETUP: Replaced {func_name} in caller's globals")
            except Exception as e:
                if self.agent.dev_mode:
                    log_warn(f"SETUP: Could not replace {func_name} in caller's globals: {e}")

            # 3. Replace in original function's module
            try:
                if hasattr(original_func, "__module__"):
                    module = sys.modules.get(original_func.__module__)
                    if module and hasattr(module, func_name):
                        setattr(module, func_name, tracked_func)
                        if self.agent.dev_mode:
                            log_debug(
                                f"SETUP: Replaced {func_name} in module {original_func.__module__}"
                            )
            except Exception as e:
                if self.agent.dev_mode:
                    log_warn(
                        f"SETUP: Could not replace {func_name} in module {original_func.__module__}: {e}"
                    )

            # 4. Store reference to original function for debugging
            try:
                setattr(tracked_func, "__wrapped__", original_func)
            except (AttributeError, TypeError):
                # Some function types don't allow setting __wrapped__
                pass

            if self.agent.dev_mode:
                log_debug(f"SETUP: Function replacement complete for {func_name}")

        except Exception as e:
            if self.agent.dev_mode:
                log_error(f"Function replacement failed for {func_name}: {e}")

    async def _ensure_execution_registered(
        self,
        context: ExecutionContext,
        reasoner_name: str,
        parent_context: Optional[ExecutionContext],
    ) -> None:
        """Ensure the given execution context is registered with Brain."""

        if getattr(context, "registered", False):
            return

        client = getattr(self.agent, "client", None)
        async_request = getattr(client, "_async_request", None)

        run_id = context.run_id or (parent_context.run_id if parent_context else None)
        if run_id is None:
            # Fallback so registration still succeeds and the server assigns one.
            run_id = context.workflow_id
            context.run_id = run_id

        if async_request is None or not callable(async_request):
            # Nothing we can do; mark as registered to avoid repeated attempts.
            context.registered = True
            return

        payload = {
            "run_id": run_id,
            "workflow_id": context.workflow_id,
            "reasoner_id": reasoner_name,
            "agent_node_id": self.agent.node_id,
        }

        if parent_context and parent_context.execution_id:
            payload["parent_execution_id"] = parent_context.execution_id

        if context.session_id:
            payload["session_id"] = context.session_id

        try:
            response = await async_request(
                "POST",
                f"{self.agent.brain_server}/api/v1/workflow/executions",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=2.0,
            )
        except Exception as exc:  # pragma: no cover - network failure
            log_warn(f"Registration request failed for execution {context.execution_id}: {exc}")
            raise

        status = getattr(response, "status", None)
        if status is None:
            status = getattr(response, "status_code", None)

        if status and status >= 400:
            message = f"Registration failed with status {status}"
            log_error(message)
            raise RuntimeError(message)

        registration_data = None
        if hasattr(response, "json"):
            try:
                registration_data = response.json()
            except Exception:  # pragma: no cover - best effort
                registration_data = None

        if isinstance(registration_data, dict):
            if registration_data.get("execution_id"):
                context.execution_id = registration_data["execution_id"]
            if registration_data.get("workflow_id"):
                context.workflow_id = registration_data["workflow_id"]
            if registration_data.get("run_id"):
                context.run_id = registration_data["run_id"]

        context.registered = True

    async def execute_with_tracking(
        self, original_func: Callable, args: tuple, kwargs: dict
    ) -> Any:
        """
        Unified execution pipeline for both direct calls and app.call().

        This method provides consistent workflow tracking for all reasoner calls,
        whether they are direct function calls or cross-agent calls via app.call().
        """
        log_track(f"{original_func.__name__} called with args={args}, kwargs={kwargs}")

        # Check if we're in a tracked execution context (prefer enhanced decorator context)
        from brain_sdk.execution_context import get_current_context
        current_context = get_current_context() or self.agent._current_execution_context

        if current_context:
            log_track(f"Found execution context for {original_func.__name__}, creating child context")

            # Create child context for tracking
            child_context = current_context.create_child_context()
            # 🔥 FIX: Update the child context's reasoner name with the actual function name
            child_context.reasoner_name = original_func.__name__
            await self._ensure_execution_registered(
                child_context,
                original_func.__name__,
                current_context,
            )
            child_execution_id = child_context.execution_id

            if self.agent.dev_mode:
                log_debug(
                    "TRACK: Created child context for "
                    f"{original_func.__name__}\n"
                    f"  Parent Execution ID: {current_context.execution_id}\n"
                    f"  Child Execution ID: {child_execution_id}\n"
                    f"  Workflow ID: {child_context.workflow_id}\n"
                    f"  Parent Workflow ID: {child_context.parent_workflow_id}\n"
                    f"  Reasoner Name: {child_context.reasoner_name}"
                )

            # Inject execution context if function accepts it
            sig = inspect.signature(original_func)
            if "execution_context" in sig.parameters:
                kwargs["execution_context"] = child_context
                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: Injected execution context into {original_func.__name__}"
                    )

            # Set child context as current during execution
            previous_context = self.agent._current_execution_context
            self.agent._current_execution_context = child_context

            if self.agent.dev_mode:
                log_debug(
                    f"TRACK: Sending start notification for {original_func.__name__}"
                )

            # 🔧 FIX: Capture original input data before function execution
            # Combine args and kwargs to get complete input data
            original_input_data = {}
            
            # Add positional arguments with parameter names if available
            try:
                sig = inspect.signature(original_func)
                param_names = [name for name, param in sig.parameters.items() 
                             if name not in ["self", "execution_context"]]
                
                # Map positional args to parameter names
                for i, arg in enumerate(args):
                    if i < len(param_names):
                        original_input_data[param_names[i]] = arg
                
                # Add keyword arguments (these override positional if same name)
                original_input_data.update(kwargs)
                
            except Exception:
                # Fallback: use generic names for args and include kwargs
                for i, arg in enumerate(args):
                    original_input_data[f"arg_{i}"] = arg
                original_input_data.update(kwargs)

            # Send start notification and wait for acknowledgement so ordering is preserved.
            await self.notify_call_start(
                child_execution_id,
                child_context,
                original_func.__name__,
                original_input_data,  # 🔧 FIX: Send complete input data
                parent_execution_id=current_context.execution_id,
            )

            start_time = time.time()
            try:
                if self.agent.dev_mode:
                    log_debug(f"TRACK: Executing {original_func.__name__}")

                # 🔥 NEW: Automatic Pydantic model conversion (FastAPI-like behavior)
                try:
                    if should_convert_args(original_func):
                        converted_args, converted_kwargs = convert_function_args(original_func, args, kwargs)
                        args = converted_args
                        kwargs = converted_kwargs
                        if self.agent.dev_mode:
                            log_debug(
                                f"TRACK: Converted arguments for {original_func.__name__}"
                            )
                except ValidationError as e:
                    # Re-raise validation errors with context
                    raise ValidationError(
                        f"Pydantic validation failed for reasoner '{original_func.__name__}': {e}",
                        model=getattr(e, 'model', None)
                    ) from e
                except Exception as e:
                    # Log conversion errors but continue with original args for backward compatibility
                    if self.agent.dev_mode:
                        log_warn(
                            f"TRACK: Failed to convert arguments for {original_func.__name__}: {e}"
                        )

                # Execute the original function
                if asyncio.iscoroutinefunction(original_func):
                    result = await original_func(*args, **kwargs)
                else:
                    result = original_func(*args, **kwargs)

                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: {original_func.__name__} completed successfully, sending completion notification"
                    )

                end_time = time.time()
                await self.notify_call_complete(
                    child_execution_id,
                    child_context.workflow_id,
                    result,
                    int((end_time - start_time) * 1000),
                    child_context,  # 🔥 FIX: Pass child_context to get parent_workflow_id
                    input_data=original_input_data,  # 🔧 FIX: Pass original complete input data
                    parent_execution_id=current_context.execution_id,
                )

                return result

            except asyncio.CancelledError as cancel_err:
                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: {original_func.__name__} cancelled, sending error notification"
                    )

                end_time = time.time()
                await self.notify_call_error(
                    child_execution_id,
                    child_context.workflow_id,
                    "Execution cancelled by upstream client",
                    int((end_time - start_time) * 1000),
                    child_context,
                    input_data=original_input_data,
                    parent_execution_id=current_context.execution_id,
                )
                raise cancel_err

            except Exception as e:
                if self.agent.dev_mode:
                    log_error(
                        f"TRACK: {original_func.__name__} failed with error: {e}, sending error notification"
                    )

                end_time = time.time()
                await self.notify_call_error(
                    child_execution_id,
                    child_context.workflow_id,
                    str(e),
                    int((end_time - start_time) * 1000),
                    child_context,  # 🔥 FIX: Pass child_context to get parent_workflow_id
                    input_data=original_input_data,  # 🔧 FIX: Pass original complete input data
                    parent_execution_id=current_context.execution_id,
                )
                raise
            finally:
                # Always restore previous context
                self.agent._current_execution_context = previous_context
                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: Restored previous context for {original_func.__name__}"
                    )
        else:
            if self.agent.dev_mode:
                log_debug(
                    f"TRACK: No execution context found for {original_func.__name__}, creating root context"
                )

            # Create a new root execution context for tracking
            root_context = ExecutionContext.create_new(
                agent_node_id=self.agent.node_id,
                workflow_name=f"{self.agent.node_id}_{original_func.__name__}",
            )
            root_execution_id = root_context.execution_id  # Use the execution_id from the root context

            if self.agent.dev_mode:
                log_debug(
                    "TRACK: Created root context\n"
                    f"  Workflow ID: {root_context.workflow_id}\n"
                    f"  Execution ID: {root_execution_id}"
                )

            # Inject execution context if function accepts it
            sig = inspect.signature(original_func)
            if "execution_context" in sig.parameters:
                kwargs["execution_context"] = root_context
                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: Injected execution context into {original_func.__name__}"
                    )

            # Set root context as current during execution
            previous_context = self.agent._current_execution_context
            self.agent._current_execution_context = root_context

            if self.agent.dev_mode:
                log_debug(
                    f"TRACK: Sending start notification for {original_func.__name__}"
                )

            # Ensure the root start notification lands before execution proceeds.
            await self.notify_call_start(
                root_execution_id,
                root_context,
                original_func.__name__,
                kwargs,
                parent_execution_id=None,  # This is a root context
            )

            start_time = time.time()
            try:
                if self.agent.dev_mode:
                    log_debug(f"TRACK: Executing {original_func.__name__}")

                # 🔥 NEW: Automatic Pydantic model conversion (FastAPI-like behavior)
                try:
                    if should_convert_args(original_func):
                        converted_args, converted_kwargs = convert_function_args(original_func, args, kwargs)
                        args = converted_args
                        kwargs = converted_kwargs
                        if self.agent.dev_mode:
                            log_debug(
                                f"TRACK: Converted arguments for {original_func.__name__}"
                            )
                except ValidationError as e:
                    # Re-raise validation errors with context
                    raise ValidationError(
                        f"Pydantic validation failed for reasoner '{original_func.__name__}': {e}",
                        model=getattr(e, 'model', None)
                    ) from e
                except Exception as e:
                    # Log conversion errors but continue with original args for backward compatibility
                    if self.agent.dev_mode:
                        log_warn(
                            f"TRACK: Failed to convert arguments for {original_func.__name__}: {e}"
                        )

                # Execute the original function
                if asyncio.iscoroutinefunction(original_func):
                    result = await original_func(*args, **kwargs)
                else:
                    result = original_func(*args, **kwargs)

                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: {original_func.__name__} completed successfully, sending completion notification"
                    )

                end_time = time.time()
                await self.notify_call_complete(
                    root_execution_id,
                    root_context.workflow_id,
                    result,
                    int((end_time - start_time) * 1000),
                    root_context,  # 🔥 FIX: Pass root_context (parent_workflow_id will be None for root)
                    input_data=kwargs,  # 🔧 FIX: Pass actual input data
                )

                return result

            except asyncio.CancelledError as cancel_err:
                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: {original_func.__name__} cancelled, sending error notification"
                    )

                end_time = time.time()
                await self.notify_call_error(
                    root_execution_id,
                    root_context.workflow_id,
                    "Execution cancelled by upstream client",
                    int((end_time - start_time) * 1000),
                    root_context,
                    input_data=kwargs,
                )
                raise cancel_err

            except Exception as e:
                if self.agent.dev_mode:
                    log_error(
                        f"TRACK: {original_func.__name__} failed with error: {e}, sending error notification"
                    )

                end_time = time.time()
                await self.notify_call_error(
                    root_execution_id,
                    root_context.workflow_id,
                    str(e),
                    int((end_time - start_time) * 1000),
                    root_context,  # 🔥 FIX: Pass root_context (parent_workflow_id will be None for root)
                    input_data=kwargs,  # 🔧 FIX: Pass actual input data
                )
                raise
            finally:
                # Always restore previous context (which was None)
                self.agent._current_execution_context = previous_context
                if self.agent.dev_mode:
                    log_debug(
                        f"TRACK: Restored previous context for {original_func.__name__}"
                    )

    async def notify_call_start(
        self,
        execution_id: str,
        context: ExecutionContext,
        reasoner_name: str,
        input_data: dict,
        parent_execution_id: Optional[str] = None,
    ):
        """Fire-and-forget notification when internal call starts"""
        try:
            payload = {
                "execution_id": execution_id,
                "workflow_id": context.workflow_id,
                "parent_workflow_id": context.parent_workflow_id,
                "parent_execution_id": parent_execution_id,
                "agent_node_id": self.agent.node_id,
                "reasoner_id": reasoner_name,
                "status": "running",
                "input_data": AgentUtils.serialize_result(input_data),
                "started_at": time.time(),
                "type": reasoner_name,
                "run_id": context.run_id,
            }

            # Validation logging for parent-child relationships
            if self.agent.dev_mode:
                log_debug(f"🔍 VALIDATION: Workflow tracking for {reasoner_name}")
                log_debug(f"  Execution ID: {execution_id}")
                log_debug(f"  Workflow ID: {context.workflow_id}")
                log_debug(f"  Parent Workflow ID: {context.parent_workflow_id}")
                log_debug(f"  Parent Execution ID: {parent_execution_id}")
                log_debug(f"  Context Depth: {getattr(context, 'depth', 'unknown')}")
                
                # Validate parent-child relationship
                if parent_execution_id and context.parent_workflow_id:
                    log_debug(f"✅ VALIDATION: Child call detected - proper hierarchy")
                    log_debug(f"  → Child execution {execution_id} has parent execution {parent_execution_id}")
                    log_debug(f"  → Child workflow {context.workflow_id} has parent workflow {context.parent_workflow_id}")
                elif parent_execution_id is None and context.parent_workflow_id is None:
                    log_debug(f"✅ VALIDATION: Root call detected - no parent")
                else:
                    log_warn(f"⚠️ VALIDATION: Potential hierarchy issue detected")
                    log_warn(f"  → parent_execution_id: {parent_execution_id}")
                    log_warn(f"  → parent_workflow_id: {context.parent_workflow_id}")

            # Fire-and-forget HTTP call
            await self.fire_and_forget_update(payload)

        except Exception as e:
            if self.agent.dev_mode:
                log_error(f"⚠️ Failed to notify call start: {e}")

    async def notify_call_complete(
        self, execution_id: str, workflow_id: str, result: Any, duration_ms: int, context: ExecutionContext, input_data: Optional[dict] = None, parent_execution_id: Optional[str] = None
    ):
        """Fire-and-forget notification when internal call completes"""
        try:
            # 🔥 FIX: Serialize Pydantic models and other complex objects
            serialized_result = AgentUtils.serialize_result(result)

            # 🔥 FIX: Use parent_workflow_id directly from the child context
            # This ensures consistency with notify_call_start() which also uses context.parent_workflow_id
            parent_workflow_id = context.parent_workflow_id

            # 🔥 FIX: Use context.reasoner_name (now properly updated) instead of fallback
            reasoner_name = context.reasoner_name if hasattr(context, 'reasoner_name') and context.reasoner_name != "child_call" else "unknown"

            # 🔧 FIX: Use actual input data instead of empty dict
            serialized_input = AgentUtils.serialize_result(input_data) if input_data is not None else {}

            payload = {
                "execution_id": execution_id,
                "workflow_id": workflow_id,
                "parent_execution_id": parent_execution_id,
                "parent_workflow_id": parent_workflow_id,  # 🔥 FIX: Now correctly includes parent_workflow_id
                "agent_node_id": self.agent.node_id,
                "reasoner_id": reasoner_name,  # 🔥 FIX: Use properly updated reasoner name
                "status": "succeeded",
                "input_data": serialized_input,  # 🔧 FIX: Send actual input data
                "result": serialized_result,  # ✅ JSON-serializable
                "duration_ms": duration_ms,
                "completed_at": time.time(),
                "type": reasoner_name,  # 🔥 FIX: Use properly updated reasoner name
                "run_id": context.run_id,
            }

            # Validation logging for completion tracking
            if self.agent.dev_mode:
                log_debug(f"🔍 COMPLETION: Workflow completion for {reasoner_name}")
                log_debug(f"  Execution ID: {execution_id}")
                log_debug(f"  Workflow ID: {workflow_id}")
                log_debug(f"  Parent Workflow ID: {parent_workflow_id}")
                log_debug(f"  Parent Execution ID: {parent_execution_id}")
                log_debug(f"  Reasoner Name: {reasoner_name} (was: {context.reasoner_name})")
                if parent_execution_id and parent_workflow_id:
                    log_debug(f"✅ COMPLETION: Child workflow completion - proper hierarchy maintained")
                elif parent_execution_id is None and parent_workflow_id is None:
                    log_debug(f"✅ COMPLETION: Root workflow completion - no parent")
                else:
                    log_warn(f"⚠️ COMPLETION: Potential hierarchy issue in completion")

            # Fire-and-forget HTTP call
            await self.fire_and_forget_update(payload)

        except Exception as e:
            if self.agent.dev_mode:
                log_error(f"🔥 FIRE: Error in completion notification: {e}")
            # Continue execution - don't break workflow

    async def notify_call_error(
        self, execution_id: str, workflow_id: str, error: str, duration_ms: int, context: ExecutionContext, input_data: Optional[dict] = None, parent_execution_id: Optional[str] = None
    ):
        """Fire-and-forget notification when internal call fails"""
        try:
            # 🔥 FIX: Use parent_workflow_id directly from the context (consistent with completion fix)
            parent_workflow_id = context.parent_workflow_id

            # 🔥 FIX: Use context.reasoner_name (now properly updated) instead of fallback
            reasoner_name = context.reasoner_name if hasattr(context, 'reasoner_name') and context.reasoner_name != "child_call" else "unknown"

            # 🔧 FIX: Use actual input data instead of empty dict
            serialized_input = AgentUtils.serialize_result(input_data) if input_data is not None else {}

            payload = {
                "execution_id": execution_id,
                "workflow_id": workflow_id,
                "parent_execution_id": parent_execution_id,
                "parent_workflow_id": parent_workflow_id,  # 🔥 FIX: Now correctly includes parent_workflow_id
                "agent_node_id": self.agent.node_id,
                "reasoner_id": reasoner_name,  # 🔥 FIX: Use properly updated reasoner name
                "status": "failed",
                "input_data": serialized_input,  # 🔧 FIX: Send actual input data
                "result": {},  # Provide empty dict as default for result
                "error": error,
                "duration_ms": duration_ms,
                "completed_at": time.time(),
                "type": reasoner_name,  # 🔥 FIX: Use properly updated reasoner name
                "run_id": context.run_id,
            }

            # Validation logging for error tracking
            if self.agent.dev_mode:
                log_debug(f"🔍 ERROR: Workflow error for {reasoner_name}")
                log_debug(f"  Execution ID: {execution_id}")
                log_debug(f"  Workflow ID: {workflow_id}")
                log_debug(f"  Parent Workflow ID: {parent_workflow_id}")
                log_debug(f"  Parent Execution ID: {parent_execution_id}")
                log_debug(f"  Reasoner Name: {reasoner_name} (was: {context.reasoner_name})")
                log_error(f"  Error: {error}")

            # Fire-and-forget HTTP call
            await self.fire_and_forget_update(payload)

        except Exception as e:
            if self.agent.dev_mode:
                log_error(f"⚠️ Failed to notify call error: {e}")

    async def fire_and_forget_update(self, payload: dict):
        """Send update to Brain server without waiting for response"""
        try:
            log_fire(
                f"Sending workflow update - {payload.get('status')} for {payload.get('reasoner_id')}",
                payload
            )
            log_fire(f"URL: {self.agent.brain_server}/api/v1/workflow/update")
            
            # 🔧 DEBUG: Log input data specifically to diagnose empty input issue
            input_data = payload.get('input_data')
            if input_data is not None:
                log_fire(f"🔍 INPUT_DEBUG: Sending input_data: {input_data} (type: {type(input_data)})")
            else:
                log_fire("🔍 INPUT_DEBUG: Sending None input_data")

            client = getattr(self.agent, "client", None)
            async_request = getattr(client, "_async_request", None)

            if async_request is None or not callable(async_request):
                log_fire("Skipping workflow update - async request handler unavailable")
                return

            response = await async_request(
                "POST",
                f"{self.agent.brain_server}/api/v1/workflow/update",
                json=payload,
                headers={"Content-Type": "application/json"},
                timeout=1.5,
            )

            status = getattr(response, "status", None)
            if status is None:
                status = getattr(response, "status_code", None)
            if status is not None:
                log_fire(f"Response status: {status}")
        except Exception as e:
            log_fire(f"Error sending workflow update: {e}")
            # Continue silently for fire-and-forget
            pass
