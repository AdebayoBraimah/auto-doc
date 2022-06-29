"""Configuration file and documentation setup.
"""
from typing import Dict
from commandio.workdir import WorkDir

from autodoc.conf.write_conf import write_conf


def conf_setup(
    outdir: str,
    pkg_path: str,
    project: str,
    copyright: str,
    author: str,
    release: str,
    theme: str,
) -> str:
    """Sets up source directory structure and writes sphinx configuration file.

    NOTE:
        ``out_dir`` is assumed to be the main/parent directory of the repository.

    Args:
        outdir: Parent output directory.
        pkg_path: Package path information.
        project: Project name.
        copyright: Copyright information.
        author: Author name.
        release: Release/version number/ID.
        theme: Sphinx theme.

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

        with WorkDir(_static) as sd:
            with WorkDir(_template) as td:
                # WorkDir class creates these directories
                pass
