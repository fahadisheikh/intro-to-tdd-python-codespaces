# Intro to TDD (Python + pytest) — FizzBuzz (Codespaces-ready)

This repo is pre-configured for **GitHub Codespaces** via `.devcontainer/devcontainer.json`.

## Quick start (Codespaces)
1) Push this repo to GitHub (or create new repo and upload).
2) Click **Code ▸ Create codespace on main**.
3) Wait for setup to finish (it runs `pip install -r requirements.txt` automatically).
4) Run tests from the terminal:
```bash
pytest
```
or from the **Testing** sidebar in VS Code (pytest is already configured).

### One-click link (optional)
If your repo lives at `github.com/OWNER/REPO`, you can open a codespace directly:
```
https://codespaces.new/OWNER/REPO?quickstart=1
```

## Local dev (optional)
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pytest -q
```

## FizzBuzz kata (inside-out TDD)
- `fizzbuzz(n)` with a simple composable rules engine
- Tests demonstrate Red → Green → Refactor and easy extensibility

## Repo layout
```
.
├─ .devcontainer/
│  └─ devcontainer.json
├─ .vscode/
│  └─ settings.json
├─ tests/
│  ├─ test_fizzbuzz_spec.py
│  └─ test_rules_engine.py
├─ fizzbuzz.py
├─ pytest.ini
└─ requirements.txt
```
