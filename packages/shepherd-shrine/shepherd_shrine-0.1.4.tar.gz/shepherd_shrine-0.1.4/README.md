# AIChaosCrazyFish

The Shepherd & The Shrine

This repository contains the Shepherd engine and tooling to generate the Shrine dashboard. It follows modern Python project conventions and includes CI, linting (Ruff), and packaging for the minimal Shepherd launcher.

Getting started (local dev):

- Create and activate a virtual environment (Windows):

```powershell
python -m venv venv
venv\Scripts\activate
```

- Install dev dependencies (formatters, type checking, tests, hooks):

```powershell
pip install -U pip
pip install black isort mypy pytest pre-commit
```

- Configure credentials: keep any service account JSON outside the repo and point to it via environment variables or a secure vault. Do not commit secrets.

Running tests:

```powershell
python -m pytest
```

Packaging & CLI:

- The launcher console script is exposed as `shepherd` and is implemented in `shepherd/shepherd_launch.py`.
- Install locally in editable mode to try the CLI:

```powershell
pip install -e .
shepherd --version
```

Releases:

- TestPyPI publishes on tags like `vX.Y.Z`.
- PyPI final publishes on tags like `vX.Y.Z-final`.
- A helper script `tools/release_tag.py` creates and pushes the correct tags.

Contributing: see `CONTRIBUTING.md` (TODO)

Tagline: "Shepherd: guardian processes that safely submit to the Shrine."
