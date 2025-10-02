import sys
import os
from pathlib import Path
from textwrap import dedent
from typer.testing import CliRunner
from vscode_pytest_update_snapshot.__main__ import app

runner = CliRunner()

def test_updates_snapshot(tmp_path: Path, monkeypatch):
    # require inline_snapshot for the e2e
    try:
        import inline_snapshot  # noqa: F401
    except Exception:
        import pytest
        pytest.skip("inline_snapshot not installed in test env")

    # project skeleton
    (tmp_path / "tests").mkdir()
    test_file = tmp_path / "tests" / "test_snap.py"
    test_file.write_text(dedent('''
        from inline_snapshot import snapshot
        def add(a,b): return a+b
        def test_add():
            assert add(1,2) == snapshot("WRONG")
    '''), encoding="utf-8")

    # 1) Run CLI to CREATE snapshot (may exit with 1 by design)
    cwd = os.getcwd()
    try:
        os.chdir(tmp_path)
        res = runner.invoke(app, [str(test_file), "4", "--python", sys.executable])
        # inline-snapshot intentionally returns non-zero after create; accept 0 or 1
        assert res.exit_code in (0, 1), res.output
        print(tmp_path)
        print('------CLI OUTPUT------')
        print(res.output_bytes.decode("utf-8"))
        print('----------------------')

        # Confirm file was updated
        text = test_file.read_text(encoding="utf-8")
        print(text)
        assert 'snapshot(3)' in text

        # 2) Verify a clean pytest run (no create flag) now passes
        import subprocess
        code = subprocess.call([sys.executable, "-m", "pytest", "-q"])
        assert code == 0
    finally:
        os.chdir(cwd)
