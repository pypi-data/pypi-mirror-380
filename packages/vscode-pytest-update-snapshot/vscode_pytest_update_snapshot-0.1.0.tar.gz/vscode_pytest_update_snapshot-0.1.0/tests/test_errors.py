from pathlib import Path
from textwrap import dedent
from typer.testing import CliRunner
from vscode_pytest_update_snapshot.__main__ import app

runner = CliRunner()

def test_no_test_at_line_exits_2(tmp_path: Path):
    f = tmp_path/"test_empty.py"
    f.write_text(dedent("""
        def helper():
            pass
    """), encoding="utf-8")

    res = runner.invoke(app, [str(f), "1"])
    assert res.exit_code == 2  # our code path when no test is found
