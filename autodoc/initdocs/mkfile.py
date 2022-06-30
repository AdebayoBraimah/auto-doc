"""Create/setup make files for shpinx documentation.
"""
import os

from glob import glob
from typing import List, Tuple

from commandio.fileio import File
from commandio.workdir import WorkDir


def setup_make_file(outdir: str) -> Tuple[str, str]:
    """Copies make file templates (for both UNIX and Windows) for sphinx documentation.

    NOTE:
        ``out_dir`` is assumed to be the main/parent directory of the repository.

    Args:
        outdir: Output parent directory.

    Returns:
        Tuple of strings that corresponds to the needed make files.
    """
    from autodoc import _MISCDIR

    _files: List[str] = []

    with WorkDir(_MISCDIR) as md:
        with WorkDir(outdir) as od:
            docdir: str = od.join("doc")

            with WorkDir(docdir) as dd:

                _make_files: List[str] = glob(md.join("*ake*"))
                _make_files.append(md.join("requirements.txt"))
                make_files: Tuple[str] = tuple(_make_files)

                for make_file in make_files:
                    with File(make_file, assert_exists=True) as mk:
                        _, fname, ext = mk.file_parts()
                        out: str = dd.join(f"{fname}{ext}")

                        if not os.path.exists(out):
                            mk.copy(out)
                        else:
                            print(f"\n{fname}: Already exists in output directory.\n")

                        _files.append(out)

    files: Tuple[str] = tuple(_files)

    return files
