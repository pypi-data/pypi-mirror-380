Contributing to Univer Use
==========================

Thanks for helping improve Univer Use! This guide is streamlined around the Makefile tasks.

Prerequisites
- Python 3.11+
- uv (recommended): https://docs.astral.sh/uv/
- Optional: `langgraph-cli` for local graph dev (installed via dev deps)

Quick Start
- Install deps: `make setup`
- Run tests: `make test`
- Run local graph: `make dev-graph`

Common Tasks (Makefile)
- setup: install deps (incl. dev) with uv
  - `make setup`
- test: run pytest
  - `make test`
- dev-graph: start local LangGraph dev server
  - `make dev-graph`
- clean: remove build/test artifacts
  - `make clean`
- build: build sdist/wheel; check: verify metadata
  - `make build && make check`
- tag: create annotated tag (VCS-based versioning)
  - `make tag VERSION=0.1.0a1`
- preview-upload: upload to PyPI (pre-releases allowed; set TWINE env vars)
  - `make preview-upload`
- release-upload: upload to PyPI (set TWINE env vars)
  - `make release-upload`

Project Structure
- Core library: `univer_use/` (agents, tools, prompts, graph, state, model)
- Prompts: `univer_use/prompts/` (packaged in the wheel)
- Tests: `tests/` (`pytest`, `pytest-asyncio` for async)
- Example config: `examples/sheet_edit/`

Env Vars
- Use a `.env` or shell vars (no secrets in repo):
  - `OPENROUTER_API_KEY`, `UNIVER_API_KEY`
  - See `examples/sheet_edit/.env` for a template.

Coding Style
- Python 3.11+ with type hints; docstrings for public APIs
- 4-space indentation, ~100-char lines
- Imports: stdlib, third-party, local (grouped, blank line between)
- Keep functions small and composable

Testing Guidelines
- Files: `tests/test_*.py`; functions: `test_*`
- Async tests: `@pytest.mark.asyncio`
- Add tests for new features and bug fixes

Commits & PRs
- Conventional Commits: `feat: …`, `fix: …`, `docs: …`, `test: …`, `refactor: …`, `chore: …`
- Keep PRs focused and small; include steps to verify and link issues
- Before PR: `make test` and update docs if needed

Publishing (Maintainers)
- VCS-based versioning (hatch-vcs): versions come from git tags
- Pre-release and stable versions are both published to PyPI
  - Preview: `make tag VERSION=0.1.0a1 && make build && make check && make preview-upload`
  - Stable: `make tag VERSION=0.1.0 && make build && make check && make release-upload`

Security
- Never commit secrets or `.env` files
- Validate credentials locally before running examples
