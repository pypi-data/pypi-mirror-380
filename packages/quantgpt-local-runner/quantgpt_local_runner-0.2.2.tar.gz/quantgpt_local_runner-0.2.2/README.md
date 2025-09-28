QuantGPT Local Runner
=====================

Local WebSocket-capable runner for QuantGPT experiments.

Usage
-----

```bash
pip install quantgpt-local-runner
quantgpt-run-local --port 8000 --host 0.0.0.0 --log-level debug
```

WebSocket
---------

- Endpoint: `/ws`
- Send JSON with a `code` field containing Python to execute.

Example message:

```json
{"code": "print('hello world')"}
```

Response:

```json
{"status":"completed","content":"hello world\n","timestamp":"..."}
```

Notes
-----

- If available, `numpy`, `pandas`, and `vectorbtpro` are imported into the execution namespace as `np`, `pd`, and `vbt`.

