"""Create/setup make files for shpinx documentation.
"""
from glob import glob
from typing import Tuple

from commandio.fileio import File
from commandio.workdir import WorkDir


def setup_make_file(outdir: str) -> Tuple[str, str]:
    """Copies make file templates (for both UNIX and Windows) for sphinx documentation.

    Args:
        outdir: Output parent directory.

    Returns:
        Tuple of strings that corresponds to the needed make files.
    """
    from autodoc import _MISCDIR

    with WorkDir(_MISCDIR) as md:
        with WorkDir(outdir) as od:
            docdir: str = od.join("doc")
            make_files: Tuple[str] = tuple(glob(md.join("*ake*")))

            for make_file in make_files:
                with File(make_file, assert_exists=True) as mk:
                    mk.copy(docdir)
    return make_files