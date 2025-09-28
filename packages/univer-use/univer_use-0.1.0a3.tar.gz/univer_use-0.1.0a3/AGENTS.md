# Repository Guidelines

## Project Structure & Module Organization
- `univer_use/`: Core library (agents, tools, prompts, graph, state, model, MCP config). Prompts live in `univer_use/prompts/`.
- `tests/`: Pytest-based tests (async tests use `pytest-asyncio`).
- `examples/sheet_edit/`: Local dev config (`langgraph.json`) and `.env` example for API keys.

## Build, Test, and Development Commands
- Install deps
  - `uv sync` (recommended)
- Add dependencies
  - `uv add [dependency] --allow-insecure-host pypi.org --allow-insecure-host files.pythonhosted.org --prerelease=allow`
- Run tests
  - `uv run pytest -q`
- Start graph locally (LangGraph CLI)
  - `langgraph dev --config examples/sheet_edit/langgraph.json --debug-port 5678 --allow-blocking`
  - Uses entrypoint `univer_use/graph.py:build_graph`

## Coding Style & Naming Conventions
- Python 3.11+. Use type hints and docstrings for public functions.
- Indentation: 4 spaces; max line length ~100.
- Naming: `snake_case` for functions/vars, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants.
- Imports: standard lib, third-party, local (grouped, blank line between).
- No formatter is pinned; prefer Black/Ruff style if available. Keep functions small and composable.

## Testing Guidelines
- Frameworks: `pytest`, `pytest-asyncio`.
- Test layout: files `tests/test_*.py`, functions `test_*`.
- Async tests: mark with `@pytest.mark.asyncio`.
- Write tests for new behavior and significant bug fixes. Aim for meaningful coverage of core paths.

## Commit & Pull Request Guidelines
- Commits: follow Conventional Commits (seen in history): `feat: …`, `fix: …`, `docs: …`, `test: …`, `refactor: …`, `chore: …` (optionally add scope, e.g., `feat(tools): …`).
- PRs: include a clear description, screenshots/logs if UI/CLI behavior changes, steps to verify, and linked issues (e.g., `Fixes #123`). Keep PRs focused and small when possible.

## Security & Configuration Tips
- Configure env vars via `.env` (loaded with `dotenv`): `OPENROUTER_API_KEY`, `OPENROUTER_ENDPOINT`, `UNIVER_API_KEY`. Example at `examples/sheet_edit/.env`.
- Do not hardcode secrets or commit `.env` files. Validate credentials before running examples.

## Agent/LangGraph Notes
- Graph entrypoint is `build_graph()` in `univer_use/graph.py`.
- Tools live in `univer_use/tools.py`; prompts in `univer_use/prompts/`. When adding tools, document usage briefly and add tests.
