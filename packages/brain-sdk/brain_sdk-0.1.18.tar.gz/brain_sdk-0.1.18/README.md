# Brain SDK

![Coverage](https://img.shields.io/badge/coverage-85%25-brightgreen.svg)

A Python SDK for authorized users.

## Installation

```bash
pip install brain_sdk
```

## Usage

For authorized users only. Contact support for documentation

## Testing

```bash
python -m pip install -e '.[dev]'
coverage run -m pytest \
  tests/test_agent_helpers.py \
  tests/test_agent_networking.py \
  tests/test_agent_brain.py \
  tests/test_agent_core.py \
  tests/test_agent_call.py \
  tests/test_agent_integration.py \
  tests/test_memory_client_core.py \
  tests/test_rate_limiter_core.py \
  tests/test_result_cache.py \
  tests/test_execution_context_core.py \
  tests/test_execution_state.py \
  tests/test_client.py \
  tests/test_memory_events.py \
  tests/test_memory_flow_core.py
coverage report --skip-covered --omit='.venv/*'
```

The curated test set above keeps `brain_sdk.client`, `brain_sdk.agent_brain`, execution context/state primitives, and memory/rate-limiter utilities above the 80% coverage threshold required for public releases.
