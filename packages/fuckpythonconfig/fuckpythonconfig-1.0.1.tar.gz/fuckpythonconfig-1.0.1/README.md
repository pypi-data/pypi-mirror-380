# fuckPythonConfig

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](./LICENSE) [![Python >= 3.11](https://img.shields.io/badge/Python-%3E%3D3.11-3776AB?logo=python&logoColor=white)](#installation) [![Ruff](https://img.shields.io/badge/Lint-Ruff-46A3FF)](https://docs.astral.sh/ruff/)

English | [简体中文](./README.zh-CN.md)

A zero-boilerplate config loader for Python. It auto-discovers a TOML config file and a .env file located next to your running script, then resolves placeholders like ${VAR} and ${VAR:default} recursively across dicts/lists. It uses python-dotenv under the hood for robust .env behavior.

> Goal: in small-to-medium scripts/services, get a ready-to-use config with one call to `load_config()`, without writing path plumbing and env-var glue code.

## Features

- Auto discovery: by default, finds the first .toml and .env next to the caller script
- Placeholder resolution:
  - ${VAR} uses the environment variable
  - ${VAR:default} uses default when the variable is missing
  - Recursively resolves across dicts/lists
- .env compatibility: powered by python-dotenv (merge/override/interpolate, etc.)
- Clear errors:
  - FileNotFoundError (custom, more friendly info)
  - TOMLReadError
  - EnvVarNotFoundError (when no default provided)
- Minimal deps: only python-dotenv (plus stdlib tomllib)

## Installation

Requires: Python >= 3.11

- pip

```cmd
pip install fuckpythonconfig
```

- uv (optional)

```cmd
uv add fuckpythonconfig
```

- from source

```cmd
pip install git+https://github.com/JGG0sbp66/fuckPythonConfig.git@dev
```

## Quick Start

Project layout (example):

```text
your-project/
  app.py           # your script calling load_config()
  config.toml      # config file
  .env             # environment variables (dev)
```

config.toml:

```toml
[database]
host = "127.0.0.1"
port = 5432
username = "${DB_USER:postgres}"
password = "${DB_PASS}"  # will raise EnvVarNotFoundError if missing
```

.env:

```dotenv
DB_USER=local_user
DB_PASS=secret123
```

app.py:

```python
from fuckpythonconfig import load_config

cfg = load_config()  # auto-discovers .toml and .env next to app.py
print(cfg["database"]["username"])  # => "local_user"
```

Explicit parameters (optional):

```python
from fuckpythonconfig import load_config

cfg = load_config(
    file_path="./config.toml",   # specify TOML path
    dotenv_path="./.env",        # specify .env path
    verbose=True,                 # passthrough to python-dotenv
    override=False,               # override existing env vars
    interpolate=True,             # allow .env interpolation
)
```

## Placeholder rules

- Syntax:
  - ${VAR} → use env var VAR
  - ${VAR:default} → use default literal if VAR is missing
- Scope: recursively applied to all string values in dict/list
- Match: only replaced when a value is exactly a placeholder
  - i.e. "${VAR}" is replaced; "prefix ${VAR}" is not (current limitation)
- Types:
  - replaced value is a string (from env/default)
  - non-placeholder TOML types remain unchanged (int/bool/array, etc.)
- Missing variable: raises EnvVarNotFoundError if no default provided

## API

### load_config(

file_path: str | None = None,
dotenv_path: str | None = None,
stream: IO[str] | None = None,
verbose: bool = False,
override: bool = False,
interpolate: bool = True,
encoding: str | None = "utf-8",
) -> dict

Purpose:

- Read TOML → load .env → resolve placeholders → return a merged dict

Details:

- When not specified, it searches the caller script directory for the first .toml and .env
- .env loading is handled by python-dotenv; parameters are passed through

Exceptions:

- FileNotFoundError (missing .toml/.env/dir)
- TOMLReadError (syntax or read failure)
- EnvVarNotFoundError (placeholder var missing without default)

## Limitations

- Only replaces values that are exactly a placeholder (no partial replacement in long strings)
- If multiple .toml/.env files exist, the first one enumerated by the filesystem is used
- Python >= 3.11 (due to stdlib tomllib)

## Development

Ruff is used for linting/formatting.

```cmd
uv sync
```

Contributions are welcome (placeholder improvements, type casting, cross-file refs, etc.).

## Acknowledgments

- python-dotenv for the robust .env handling

## License

MIT License. See `LICENSE` for details.
