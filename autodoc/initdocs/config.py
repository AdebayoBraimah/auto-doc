"""Configuration file and documentation setup.
"""
from typing import Optional, Dict
from commandio.workdir import WorkDir

from autodoc.conf.write_conf import write_conf


def conf_setup(
    outdir: str,
    pkg_path: str,
    project: Optional[str] = None,
    copyright: Optional[str] = None,
    author: Optional[str] = None,
    release: Optional[str] = None,
    theme: Optional[str] = None,
) -> str:
    """Sets up source directory structure and writes sphinx configuration file.

    NOTE:
        ``out_dir`` is assumed to be the main/parent directory of the repository.

    Args:
        outdir: Parent output directory.
        pkg_path: Package path information.
        project: Project name. Defaults to None.
        copyright: Copyright information. Defaults to None.
        author: Author name. Defaults to None.
        release: Release/version number/ID. Defaults to None.
        theme: Sphinx theme. Defaults to None.

    Returns:
        Path to sphinx configuration file.
    """
    # Args dict
    conf_args: Dict[str, str] = {
        "pkg_path": pkg_path,
        "project": project,
        "copyright": copyright,
        "author": author,
        "release": release,
        "theme": theme,
    }

    _doc_dir_setup(outdir=outdir)
    conf_file: str = write_conf(outdir=outdir, **conf_args)
    return conf_file


def _doc_dir_setup(outdir: str) -> None:
    """Helper function to set up docuemnt source sub-directories.

    NOTE:
        ``out_dir`` is assumed to be the main/parent directory of the repository.

    Args:
        outdir: Output parent directory.
    """
    with WorkDir(outdir) as od:
        _static: str = od.join("doc", "source", "_static")
        _template: str = od.join("doc", "source", "_template")

        with WorkDir(_static) as _:
            with WorkDir(_template) as _:
                # WorkDir class creates these directories
                pass
