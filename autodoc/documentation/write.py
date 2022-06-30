"""Write reStructured Text files to write Sphinx documentation.
"""

from typing import Optional, Set
from autodoc.doccode.sphinxapi import sphinx_apidoc
from autodoc.doccode.shell import write_script_docs


def write(
    outdir: str,
    pkg: str,
    convert_tabs_to_spaces: bool = True,
    num_spaces: Optional[int] = 4,
) -> None:
    """Write reStructured Text (.rst) files for python packages/modules, and script libraries.

    NOTE:
        ``outdir`` is assumed to be the same as used in :py:func: autodoc.documentation.initialize.doc_init

    Args:
        outdir: Path to output directory.
        pkg: Path to package/repository.
        convert_tabs_to_spaces: Convert tabs to spaces. Defaults to True.
        num_spaces: Number of spaces to replace tabs with. Only applicable when ``convert_tabs_to_spaces`` is True. Defaults to 4.
    """
    _: Set[str] = write_script_docs(
        outdir=outdir,
        pkg_dir=pkg,
        convert_tabs_to_spaces=convert_tabs_to_spaces,
        num_spaces=num_spaces,
    )
    sphinx_apidoc(outdir=outdir, pkg_path=pkg)
    return None
