# dmos-search

A lightweight command-line interface that lets you search the web without opening google.com. It uses the `ddgs` library to talk to DuckDuckGo under the hood and presents results directly in your terminal, optionally opening a selected link in your browser.

## Prerequisites

Install [uv](https://docs.astral.sh/uv/) (0.8.0 or newer). uv manages the Python runtime,
virtual environment, dependencies, and packaging workflow for this project.

## Installation (development)

Sync the project into a local virtual environment managed by uv:

```bash
uv sync
```

This creates `.venv/` (ignored by git) and installs all declared dependencies plus the project
package in editable mode. uv automatically downloads a compatible Python version if your system one
does not satisfy the `requires-python` constraint.

## Usage

Invoke the CLI through uv so that the managed environment is used:

```bash
uv run dmos-search rust async runtimes
```

### Options

- `-l, --limit` — number of results to display (default: 10)
- `--region` — locale code such as `us-en`, `uk-en`, `de-de`
- `--safesearch` — `off`, `moderate`, or `strict`
- `--timeout` — HTTP timeout in seconds (default: 10)
- `--json-output` — emit the raw JSON response
- `--open N` — open the N-th result in your default browser after printing
- `--no-browser` — suppress browser opening even when `--open` is supplied

### Examples

Show five results and open the top hit automatically:

```bash
uv run dmos-search "postgres vector" -l 5 --open 1
```

Emit raw JSON for piping into other scripts:

```bash
uv run dmos-search --json-output "kubernetes pod restart policies"
```

Use a different locale and strict safe-search:

```bash
uv run dmos-search "best museums" --region uk-en --safesearch strict
```

## Scripts

Common project tasks are collected in the `scripts/` folder and invoke uv under the hood:

- `./scripts/lint` — run Ruff checks
- `./scripts/fmt` — apply Ruff formatting
- `./scripts/typecheck` — execute mypy
- `./scripts/test` — run pytest
- `./scripts/check` — run lint, typecheck, and tests sequentially
- `./scripts/build` — build source and wheel distributions via `uv build`
- `./scripts/publish` — publish to PyPI with `uv publish`
- `./scripts/publish-test` — publish to TestPyPI (`uv publish --repository testpypi`)

These scripts assume `uv sync` has been run. Development dependencies live in the `dev` dependency
group, which is enabled by default through `pyproject.toml`.

## Dependency management

- Add a runtime dependency: `uv add requests`
- Add a dev dependency: `uv add --group dev pytest`
- Remove one: `uv remove requests`
- Refresh the environment from the lockfile: `uv sync`

The `uv.lock` file captures exact versions to ensure reproducible installs.

## Packaging & publishing

Build distributions:

```bash
./scripts/build
```

Publish to PyPI (requires an API token in `UV_PUBLISH_TOKEN` or `UV_PUBLISH_PASSWORD`):

```bash
./scripts/publish
```

Test uploads go to TestPyPI:

```bash
./scripts/publish-test
```

## Notes

- DuckDuckGo limits searches to around 200 results per query; this CLI caps the request at 50 for usability.
- Opening a result uses Python's `webbrowser` module, which respects your system's default browser configuration.
- On systems with older SSL stacks (for example, Python 3.9 builds without TLS 1.3), the tool warns when it falls back to disabling certificate verification. Upgrade Python/OpenSSL to restore strict verification.

## uvx usage

Because the PyPI project name now matches the console script, the zero-flag invocation works once published:

```bash
uvx dmos-search "your query"
```
