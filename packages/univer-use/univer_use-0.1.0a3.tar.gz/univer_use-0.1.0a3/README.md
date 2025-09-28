Univer Use
==========

LangGraph-powered agent utilities and tools for Univer spreadsheets. This library provides a ready-to-use graph entrypoint and helper tools to build agents that operate against Univer via [Univer-MCP](https://github.com/dream-num/univer-mcp).

Features
- LangGraph graph entrypoint: `univer_use/graph.py:build_graph`
- Spreadsheet action agent with MCP tools
- Prompt templates packaged with the library

Install
- pip: `pip install univer-use`
- uv: `uv add univer-use`
- Poetry: `poetry add univer-use`

Requirements
- Python 3.11+
- Credentials via environment or `.env` (python-dotenv):
  - `OPENROUTER_API_KEY` – API key for your OpenRouter-compatible provider
  - `OPENROUTER_ENDPOINT` – Base URL for the provider endpoint
  - `UNIVER_API_KEY` – Univer API key (if required by your MCP setup)

Quickstart
Minimal example to compile and run the graph once:

```python
import asyncio
from univer_use import build_graph

async def main():
    graph = await build_graph()
    # Provide initial state. At minimum, include a conversation_id.
    state = {
        "messages": [],
        "conversation_id": "local-dev",
    }
    result = await graph.ainvoke(state)
    print(result)

asyncio.run(main())
```

Run Locally with LangGraph CLI
The repo includes a local dev config that uses the `build_graph` entrypoint:

```bash
langgraph dev --config examples/sheet_edit/langgraph.json --debug-port 5678 --allow-blocking
```

This uses the graph at `univer_use/graph.py:build_graph`. Set env vars in `.env` or your shell before running. See `examples/sheet_edit/.env` for an example.

Development
- Install dependencies: `uv sync`
- Run tests: `uv run pytest -q`

License
MIT. See `LICENSE`.
