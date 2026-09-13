# http://resources.codingthematrix.com/

## Setup & Tests (Windows)

### 1. Install [uv](https://docs.astral.sh/uv/#highlights) (basically npm for python)

Open **PowerShell** and run:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart your terminal, then verify:

```powershell
uv --version
```

### 2. Clone and install dependencies

```powershell
git clone <REPOSITORY_URL>
cd <REPOSITORY_DIRECTORY>
uv sync
```

### 3. Run tests

```powershell
uv run pytest
```

To run all doctests recursively:

```powershell
uv run pytest --doctest-modules . -vv
```
