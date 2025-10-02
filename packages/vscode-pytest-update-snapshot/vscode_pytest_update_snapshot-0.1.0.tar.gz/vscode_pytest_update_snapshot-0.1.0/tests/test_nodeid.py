from pathlib import Path
from textwrap import dedent

from vscode_pytest_update_snapshot.__main__ import _build_nodeid


def write(p: Path, text: str) -> Path:
    p.write_text(dedent(text), encoding="utf-8")
    return p

def test_nodeid_function(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    f = write(tmp_path/"test_sample.py", """
        def helper():
            pass

        def test_foo():
            assert 1
    """)
    print(f)

    # Line number inside test_foo
    line = 5
    nodeid = _build_nodeid(f, line)
    # relative to CWD (pytest nodeid wants posix)
    print(nodeid)
    assert nodeid.endswith("test_sample.py::test_foo")
    assert "\\" not in nodeid

def test_nodeid_class_method(tmp_path: Path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    f = write(tmp_path/"test_sample2.py", """
        class TestGroup:
            def test_bar(self):
                assert 1
    """)
    line = 3
    nodeid = _build_nodeid(f, line)
    assert nodeid.endswith("test_sample2.py::TestGroup::test_bar")

def test_nodeid_in_subdir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    (tmp_path / "tests").mkdir()
    f = write(tmp_path / "tests" / "test_sub.py", """
        def test_bar():
            assert 1
    """)

    nodeid = _build_nodeid(f, line=2)
    assert nodeid == "tests/test_sub.py::test_bar"
    assert "\\" not in nodeid
