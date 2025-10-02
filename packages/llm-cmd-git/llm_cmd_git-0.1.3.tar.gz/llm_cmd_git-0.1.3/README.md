# llm-cmd-git

Lightweight CLI plugin that uses an LLM to generate commit messages from a staged diff.

This project provides:

- a CLI command `git-llm` (entry point `llm_cmd_git.cli:cli`).
- an llm plugin entry point that integrates with the `llm` ecosystem.
- respectful hook handling: if a `pre-commit` hook exists it will be run before generating a commit message.

## Key behavior

- The tool reads the staged `git` diff and asks the configured LLM to generate a commit message.

## Installation

From the project root (recommended editable install during development):

```bash
python -m pip install -e .
```

This exposes the `git-llm` console script.

## Quick start

1. Stage your changes:

```bash
git add -A
```

2. Generate a commit message from the staged diff:

```bash
git-llm commit
```

The command will:
- run the `pre-commit` hook (if present and executable) and abort on failure,
- stream generation progress to the terminal,
- show the generated commit message and (by default) open an editor to allow edits,
- then commit the staged changes using the generated or edited message.

If you prefer to inspect the generated message only, you can run the command in a
non-interactive shell or adapt the settings (see configuration below).

## Configuration

Configuration is read from several places (in order of precedence):

- explicitly provided settings (CLI options / environment variables as supported by `pydantic-settings`),
- `pyproject.toml` under `[tool.llm-git]`,
- TOML files: `./.llm-git.toml`, `./llm-git.toml`, repository-local toml files (inside the git dir),
  and `~/.config/llm-git/llm-git.toml` (via `llm.user_dir()`).

The settings model supports fields such as `model`, `key`, `options`, `preset`,
`system_prompt_custom`, `user_prompt_template`, `extra_context` and `edit`.

Example minimal `llm-git.toml` (repo root):

```toml
[tool.llm-git]
model = "gpt-xyz"
# key = "..." # or use environment variables
```

Note: repository-local TOML files are discovered using `git rev-parse --git-dir` so
placing a config under the repository `.git` folder (or custom hooks path) will work.

## Development

- Install editable: `python -m pip install -e .`
- Run quick import check:

```bash
python -c "import sys; sys.path.insert(0, 'src'); import llm_cmd_git; print('import ok')"
```

- The codebase aims to be small and easily extended. Helper functions that resolve
  git paths are centralized in `llm_cmd_git.git`.

