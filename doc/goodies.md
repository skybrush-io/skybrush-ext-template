# Optional goodies in the generated repository

These are not mandatory; feel free to use them if you want to or remove them if you
use other conventions.

## Linter and formatter

The default repository layout pre-configures `ruff` to the conventions used in the
code of Skybrush Server. You can check your code for linter errors with the following
command:

```sh
uv run ruff check
```

The code can also be auto-formatted with:

```sh
uv run ruff format
```

## Type checker

The default repository layout pre-configures `ty` to the conventions used in Skybrush
Server. You can run a full type check of the extension with the following commands:

```sh
uv run ty check
```

## Pre-commit hooks

We provide a set of pre-commit hooks in `.pre-commit-config.yaml`. You can
install `prek` and then run them with `prek run --all-files`. The default set of
pre-commit hooks ensures that you are using idiomatic Python 3.10 syntax, fixes
end-of-line characters and trailing whitespace, checks for linter errors, formats the
code and updates the `uv` lockfile.

Again, you do not need to use these hooks if you do not want to, they are provided for
your convenience only.
