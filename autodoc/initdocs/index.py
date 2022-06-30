"""Creates index.rst files for sphinx documentation.
"""
import os

from commandio.workdir import WorkDir
from autodoc.utils.util import write_file


def write_index(outdir: str, pkg: str) -> str:
    """Creates index.rst file for sphinx.

    NOTE:
        ``out_dir`` is assumed to be the main/parent directory of the repository.

    Args:
        outdir: Output parent directory.
        pkg: Package name.

    Returns:
        Index.rst absolute file path.
    """
    _IDX_TEXT: str = f""".. {pkg} documentation main file.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive.

Welcome to {pkg}'s documentation!
==================================

.. toctree::
   :maxdepth: 3

    .. # ADD RST FILES HERE

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
    """

    idx: str = _init_index(outdir=outdir)

    if not os.path.exists(idx):
        write_file(idx, text=_IDX_TEXT, num_spaces=4, mode="a")
    else:
        print(f"\n{idx}: Already exists in output directory.\n")

    return idx


def _init_index(outdir: str) -> str:
    """Helper function that creates index.rst file for sphinx.

    NOTE:
        ``out_dir`` is assumed to be the main/parent directory of the repository.

    Args:
        outdir: Output parent directory.

    Returns:
        Index.rst absolute file path.
    """
    with WorkDir(outdir) as od:
        sourcedir: str = od.join("doc", "source")
        with WorkDir(sourcedir) as sd:
            idx: str = sd.join("index.rst")
    return idx
