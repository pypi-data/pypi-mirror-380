Univer Use
==========

LangGraph-powered agent utilities and tools for Univer spreadsheets. This library provides a ready-to-use graph entrypoint and helper tools to build agents that operate against Univer via [Univer-MCP](https://github.com/dream-num/univer-mcp).

Features
- LangGraph graph entrypoint: `univer_use/graph.py:build_graph`
- Spreadsheet action agent with MCP tools
- Prompt templates packaged with the library

Install
You can install this package using either name (both are the same package):

**Option 1: univer-use**
- pip: `pip install univer-use`
- uv: `uv add univer-use`
- Poetry: `poetry add univer-use`

**Option 2: spreadsheet-use**
- pip: `pip install spreadsheet-use`
- uv: `uv add spreadsheet-use`
- Poetry: `poetry add spreadsheet-use`

> Note: Both `univer-use` and `spreadsheet-use` provide identical functionality. Choose whichever name you prefer.

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
# Both imports work the same way:
# from univer_use import build_graph
from spreadsheet_use import build_graph

async def main():
    graph = await build_graph()
    # Provide initial state. At minimum, include a conversation_id.
    state = {
        "messages": [],
        "conversation_id": "default",
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

**Setup**
- Install dependencies: `uv sync`

**Adding Dependencies**
Simply use standard dependency management commands:

```bash
# Add a runtime dependency
uv add package-name

# Add a development dependency  
uv add --dev package-name
```

**Building & Testing**
- Run tests: `uv run pytest -q`
- Build both packages: `make build-both`

**Available Make Commands**
Run `make help` to see all available commands for development.

**Package Architecture**
- `univer-use`: The main package containing all functionality
- `spreadsheet-use`: A lightweight alias package that depends on `univer-use`

License
MIT. See `LICENSE`.
