# vscode-pytest-update-snapshot

Run `pytest` on the test under your cursor and update inline snapshots (VSCode-friendly).

## Install / Run (no install with uvx)

```bash
uvx vscode-pytest-update-snapshot tests/test_example.py 12
# ensure it uses your project venv interpreter:
uvx --python ".venv/Scripts/python.exe" vscode-pytest-update-snapshot tests/test_example.py 12
```

Pass extra pytest args after --:

```bash
uvx vscode-pytest-update-snapshot tests/test_example.py 12 -- -q -k "mycase"
```