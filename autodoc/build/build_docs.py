"""Wrapper module to build sphinx documentation.
"""
import os

from commandio.command import Command
from commandio.workdir import WorkDir


def build_docs(outdir: str) -> None:
    """Builds Sphinx HTML documentation locally.

    The output location of the documentation should be: ``<outdir>/doc/build``.

    NOTE:
        ``out_dir`` is assumed to be the main/parent directory of the repository.

    Args:
        outdir: Output parent directory.
    """
    cwd: str = os.getcwd()

    with WorkDir(outdir) as od:
        docdir: str = od.join("doc")

    os.chdir(docdir)

    # make clean
    clean: Command = Command("make clean")
    clean.run()

    # make html
    html: Command = Command("make html")
    html.run()

    os.chdir(cwd)
    return None
