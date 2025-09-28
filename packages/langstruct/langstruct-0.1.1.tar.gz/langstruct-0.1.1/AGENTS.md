# Repository Guidelines

## Project Structure & Module Organization
- `langstruct/`: Core library code
  - `api.py`: Public `LangStruct` API
  - `core/`: Extraction, validation, chunking, grounding, refinement
  - `optimizers/`: DSPy-based optimizers (MIPRO, bootstrap, metrics)
  - `providers/`: Model/provider adapters
  - `visualization/`: HTML visualization utilities
- `tests/`: Pytest suite (unit, integration, performance)
- `examples/`: End-to-end usage samples
- `docs/`: Documentation site (pnpm-based)

## Architecture Overview
- Pipeline: chunking → extraction → validation → aggregation/refinement
- DSPy Signatures define tasks; modules in `core/modules.py` implement the pipeline
- Optimization: MIPROv2 and bootstrap in `optimizers/` improve prompts and demos
- Schemas: Pydantic models in `core/schemas.py` enforce types and validation
- Grounding: character-level source spans in `core/grounding.py` and HTML viz
- Providers: model abstraction in `providers/` (OpenAI, Anthropic, Gemini, Ollama)

## Build, Test, and Development Commands
- Setup (base): `uv sync`
- Setup (dev): `uv sync --extra dev`
- Run tests: `uv run pytest` (coverage: `uv run pytest --cov=langstruct`)
- Lint/format: `uv run black . && uv run isort .`
- Type check: `uv run mypy langstruct/`
- Pre-commit: `uv run pre-commit install && uv run pre-commit run -a`
- Editable install: `uv pip install -e .`
- Docs: `cd docs && pnpm install && pnpm dev` (build: `pnpm build`)

## Coding Style & Naming Conventions
- Formatting: Black (line length 88) and isort (profile=black)
- Python: 4-space indent, type hints for public APIs, Google-style docstrings
- Naming: `snake_case` functions/vars, `PascalCase` classes, `UPPER_SNAKE_CASE` constants
- Keep module boundaries clean; prefer small, composable functions in `core/`

## Testing Guidelines
- Framework: Pytest (+ pytest-cov)
- Location/naming: place tests in `tests/`; files as `test_*.py`; functions `test_*`
- Run fast by default; mock external API calls. Mark real calls with `@pytest.mark.integration` and run via `uv run pytest -m integration`
- Aim to keep or improve coverage for changed code paths

## Commit & Pull Request Guidelines
- Commits: short, imperative mood (e.g., "fix import error", "add query parsing tests"). Group related changes.
- PRs must include:
  - Clear description, rationale, and scope
  - Linked issues (e.g., `Closes #123`)
  - Test updates or justification for none
  - Screenshots/artefacts for docs/visual changes
  - Passing CI, `black`/`isort`/`mypy` clean

## Security & Configuration Tips
- Configure providers via env vars: `GOOGLE_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`
- Never hardcode secrets or commit sample keys; avoid logging sensitive values
- Prefer unit tests with mocks; run integration tests only when keys are set

## Release Notes
- Version in `pyproject.toml`; update `CHANGELOG.md`
- Tags trigger releases (e.g., `git tag v0.x.y && git push origin v0.x.y`)
