# AGENTS.md

## Purpose

This repository provides a small CLI for incrementing semantic app versions in two target files:

- iOS `Info.plist` via `CFBundleShortVersionString`
- Android `build.gradle` via `versionName`

The implementation is Python-first. Treat the Python module and `pyproject.toml` as the authoritative sources of behavior and packaging.

## Repository Layout

- `src/increment_app_version.py`: main CLI and version update logic
- `tests/test_increment_version.py`: unit tests for semantic version increments
- `pyproject.toml`: Python packaging, CLI entry point, dev dependencies, pytest and ruff config
- `package.json`: npm wrapper metadata exposing the Python script as a binary
- `README.md`: end-user usage and setup documentation

## Working Assumptions

- Prefer small, direct changes. This is a compact single-purpose project.
- Keep the CLI behavior simple and explicit.
- Preserve Python 3.8 compatibility unless the user explicitly asks to raise the floor.
- Avoid introducing heavy dependencies for straightforward string or file updates.

## Source Of Truth

- Python packaging and CLI entry point live in `pyproject.toml`.
- The executable logic lives in `src/increment_app_version.py`.
- The npm package is secondary metadata. Do not treat `package.json` as the main implementation contract.

If behavior changes, update both code and documentation. If packaging or CLI invocation changes, check whether both `pyproject.toml` and `package.json` need coordinated edits.

## Environment Setup

Use Python tooling first:

```bash
python -m pip install -e ".[dev]"
```

Primary validation commands:

```bash
pytest
ruff check .
pre-commit run --all-files
```

If a command is unavailable in the environment, say so explicitly in your handoff.

## Code Conventions

- Follow the existing straightforward procedural style unless a refactor is justified by the task.
- Keep functions focused and easy to test.
- Raise clear exceptions for malformed inputs or missing version strings.
- Prefer standard-library facilities where practical. The only current runtime dependency is `packaging`.
- When changing file parsing logic, preserve existing file contents as much as possible outside the targeted version field.

## Testing Expectations

- Add or update tests for any behavior change in version parsing or increment logic.
- Start with unit tests in `tests/test_increment_version.py`.
- For changes to plist or Gradle rewriting behavior, add targeted tests rather than relying only on manual inspection.
- Run `pytest` after code changes when the environment supports it.

## CLI Expectations

The current CLI expects exactly one argument:

- `major`
- `minor`
- `patch`

Keep usage output accurate if argument handling changes.

The script currently targets these project-relative paths:

- `./ios/App/App/Info.plist`
- `./android/app/build.gradle`

If a task changes those assumptions, update tests and docs together.

## Known Project-Specific Pitfalls

- `package.json` is not the primary test runner. Its `test` script is currently a placeholder.
- This repo is not a general multi-platform build system. Avoid overengineering configuration unless requested.
- Be careful when changing module paths or entry points: `pyproject.toml` maps the console script to `increment_app_version:main` and uses `src` as the package dir.
- The Android updater currently relies on matching a `versionName` line with double quotes. If you broaden support, add tests for every new accepted format.

## Documentation Expectations

Update `README.md` when:

- CLI usage changes
- setup steps change
- supported file formats or paths change
- behavior visible to end users changes

Keep examples runnable and aligned with the actual command name: `increment-app-version`.

## Assistant Workflow

Before editing:

- Read `README.md`, `pyproject.toml`, and the relevant source/test files.

When making changes:

- Keep edits minimal and repo-specific.
- Prefer fixing the underlying Python logic over adding wrappers.
- Update tests in the same change when behavior changes.

Before handing off:

- Run the relevant validation commands when possible.
- Summarize code changes, tests run, and any commands you could not execute.
