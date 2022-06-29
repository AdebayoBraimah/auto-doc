"""Wrapper for ``sphinx-apidoc`` command line tool.
"""
import os
from commandio.command import Command
from commandio.workdir import WorkDir


def sphinx_apidoc(outdir: str, pkg_path: str) -> None:
    """Wrapper function for ``sphinx-apidoc``.

    Args:
        outdir: Output parent directory.
        pkg_path: Package path.
    """
    cwd: str = os.getcwd()
    with WorkDir(outdir) as od:
        docdir: str = od.join("doc")
    os.chdir(docdir)
    sphinx: Command = Command(f"sphinx-apidoc -o source {pkg_path}")
    sphinx.run()
    os.chdir(cwd)
    return None
