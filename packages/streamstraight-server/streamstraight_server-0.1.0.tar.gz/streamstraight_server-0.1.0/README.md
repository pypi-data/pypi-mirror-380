# Streamstraight Python SDK

`streamstraight-server` mirrors the `@streamstraight/server` Node SDK for producers who prefer Python. It connects to Streamstraight over Socket.IO, manages chunk acknowledgements, and exposes helpers for minting client JWTs.

## Quickstart

```bash
uv add streamstraight-server
```

For local development inside this monorepo, run `uv sync --all-extras` from `packages/python`.

## Usage

```python
import asyncio
from streamstraight_server import streamstraight_server

async def main() -> None:
    server = await streamstraight_server(
        {"api_key": "YOUR_STREAMSTRAIGHT_API_KEY"},
        {"stream_id": "your-stream-id"},
    )

    async def generate():
        # Replace with your LLM or other async generator
        yield {"content": "first chunk"}
        yield {"content": "second chunk"}

    await server.stream(generate())

asyncio.run(main())
```

### Mint a client JWT for your browser client

```python
from streamstraight_server import fetch_client_token

token = await fetch_client_token({"api_key": "YOUR_STREAMSTRAIGHT_API_KEY"})
```
