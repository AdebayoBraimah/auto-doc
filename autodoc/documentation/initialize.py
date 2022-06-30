"""Initialize documentation directory.
"""
from typing import Dict, Optional, Tuple

from commandio.workdir import WorkDir

from autodoc.initdocs.mkfile import setup_make_file
from autodoc.initdocs.config import conf_setup
from autodoc.initdocs.index import write_index


def doc_init(
    outdir: str,
    pkg: str,
    project: Optional[str] = None,
    copyright: Optional[str] = None,
    author: Optional[str] = None,
    release: Optional[str] = None,
    theme: Optional[str] = None,
) -> None:
    """Initializes documentation setup.

    This is done by:
        * Writing the make and requirement files to the output documentation parent directory.
        * Writing the ``index.rst`` file.
        * Writing the ``conf.py`` file.

    NOTE:
        * The ``conf.py`` may require further editing if many of the optional arguments are not provided.

    Args:
        outdir: Parent output directory.
        pkg: Package path to directory.
        project: Project name. Defaults to None.
        copyright: Copyright information. Defaults to None.
        author: Author name. Defaults to None.
        release: Release/version number/ID. Defaults to None.
        theme: Sphinx theme. Defaults to None.
    """
    _: Tuple[str] = setup_make_file(outdir=outdir)
    idx: str = write_index(outdir=outdir, pkg=pkg)

    with WorkDir(pkg) as pk:
        pkg_path: str = pk.relpath(idx)

    # Args dict
    conf_args: Dict[str, str] = {
        "pkg_path": pkg_path,
        "project": project,
        "copyright": copyright,
        "author": author,
        "release": release,
        "theme": theme,
    }

    _: str = conf_setup(outdir=outdir, **conf_args)
    return None
