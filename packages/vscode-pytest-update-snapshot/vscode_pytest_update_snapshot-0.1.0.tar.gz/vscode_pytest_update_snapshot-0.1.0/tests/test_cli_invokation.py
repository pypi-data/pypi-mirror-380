import sys
from textwrap import dedent
from typer.testing import CliRunner

from vscode_pytest_update_snapshot.__main__ import app

runner = CliRunner()

def test_cli_builds_correct_command(tmp_path, monkeypatch):
    # Arrange: create a test file with a single test
    f = tmp_path/"test_basic.py"
    f.write_text(dedent("""
        def test_one():
            assert True
    """), encoding="utf-8")

    # Fake subprocess.call to capture args without running pytest
    called = {}
    def fake_call(cmd):
        called["cmd"] = cmd
        return 0
    monkeypatch.setattr("vscode_pytest_update_snapshot.__main__.subprocess.call", fake_call)

    # Act
    result = runner.invoke(app, [str(f), "2", "--python", sys.executable])
    print(result.output, str(f))

    # Assert
    assert result.exit_code == 0
    cmd = called["cmd"]
    # Uses given interpreter and -m pytest
    assert cmd[:3] == [sys.executable, "-m", "pytest"]
    # Nodeid is posix
    assert cmd[3].endswith("test_basic.py::test_one")
    assert "/" in cmd[3]
    # Has the inline-snapshot flag
    assert "--inline-snapshot=fix" in cmd
