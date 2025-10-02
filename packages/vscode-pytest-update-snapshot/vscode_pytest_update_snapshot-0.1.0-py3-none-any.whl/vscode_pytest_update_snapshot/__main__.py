from __future__ import annotations
import ast
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional
import typer

app = typer.Typer(add_completion=False, rich_markup_mode="markdown")


def _find_python_from_env(cwd: Path) -> Optional[Path]:
    venv = os.environ.get("VIRTUAL_ENV")
    if venv:
        exe = "python.exe" if os.name == "nt" else "python"
        cand = Path(venv) / ("Scripts" if os.name == "nt" else "bin") / exe
        if cand.exists():
            return cand
    dotvenv = cwd / ".venv"
    exe = "python.exe" if os.name == "nt" else "python"
    cand = dotvenv / ("Scripts" if os.name == "nt" else "bin") / exe
    if cand.exists():
        return cand
    return None


class _EnclosingFinder(ast.NodeVisitor):
    def __init__(self, target_line: int) -> None:
        self.target_line = target_line
        self.class_stack: List[str] = []
        self.enclosing_func: Optional[str] = None
        self.enclosing_class: Optional[str] = None

    def _covers(self, node: ast.AST) -> bool:
        start = getattr(node, "lineno", None)
        end = getattr(node, "end_lineno", None) or start
        return bool(start and start <= self.target_line <= end)

    def visit_ClassDef(self, node: ast.ClassDef):
        if self._covers(node):
            self.class_stack.append(node.name)
            self.generic_visit(node)
            self.class_stack.pop()
        else:
            self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):
        if self._covers(node):
            self.enclosing_func = node.name
            if self.class_stack:
                self.enclosing_class = self.class_stack[-1]
        self.generic_visit(node)

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        self.visit_FunctionDef(node)


def _build_nodeid(file_path: Path, line: int) -> str:
    src = file_path.read_text(encoding="utf-8")
    tree = ast.parse(src, filename=str(file_path))
    finder = _EnclosingFinder(line)
    finder.visit(tree)
    if not finder.enclosing_func:
        raise typer.Exit(code=2)
    cwd = Path.cwd()
    try:
        # Python 3.12+: keeps relative if possible
        rel = file_path.relative_to(cwd, walk_up=True).as_posix()
    except Exception:
        import os as _os

        rel = _os.path.relpath(str(file_path), start=str(cwd)).replace("\\", "/")
    parts = [rel]
    if finder.enclosing_class:
        parts.append(finder.enclosing_class)
    parts.append(finder.enclosing_func)
    return "::".join(parts)


@app.command(
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def cli(
    file: Path = typer.Argument(
        ..., exists=True, readable=True, help="Path to test file"
    ),
    line: int = typer.Argument(..., help="1-based cursor line number"),
    python: Optional[Path] = typer.Option(
        None, "--python", "-p", help="Project interpreter/venv"
    ),
    mode: str = typer.Option("fix", "--mode", help="Snapshot mode: create or fix"),
    ctx: typer.Context = typer.Option(None),
) -> None:
    """Run pytest on the test at the cursor line and update inline snapshots."""
    inline_flag = (
        "--inline-snapshot=create" if mode == "create" else "--inline-snapshot=fix"
    )
    extra_pytest_args: List[str] = ctx.args[:] if ctx and ctx.args else []
    nodeid = _build_nodeid(file, line)
    py_exe = python or _find_python_from_env(Path.cwd()) or Path(sys.executable)
    cmd = [str(py_exe), "-m", "pytest", nodeid, inline_flag, *extra_pytest_args]
    print("Running:", " ".join(cmd), flush=True)
    raise typer.Exit(subprocess.call(cmd))


if __name__ == "__main__":
    app()
