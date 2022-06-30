"""Module for documenting shell/command line code.
"""
import os
from typing import Optional, Set

from commandio.fileio import File
from commandio.workdir import WorkDir
from autodoc.utils.docshell import document_shell_script, _auto_detect as auto_detect


def write_script_docs(
    pkg_dir: str,
    outdir: str,
    convert_tabs_to_spaces: bool = True,
    num_spaces: Optional[int] = 4,
) -> Set[str]:
    """Writes reStructered Text files (shell) scripts.

    NOTE:
        * ``out_dir`` is assumed to be the main/parent directory of the repository.
        * If any reStructered Text files of package scripts exist in the output source directory, then those files will be overwritten.

    Args:
        pkg_dir: Path to package/repository.
        outdir: Path to output directory.
        convert_tabs_to_spaces: Convert tabs to spaces. Defaults to True.
        num_spaces: Number of spaces to replace tabs with. Only applicable when ``convert_tabs_to_spaces`` is True. Defaults to 4.

    Returns:
        Set of strings that corresponds to output  reStructered Text files
    """
    scripts: Set[str] = file_search(pkg_dir=pkg_dir)
    rsts: Set[str] = set()

    with WorkDir(outdir) as od:
        srcdir: str = od.join("doc", "source")

        with WorkDir(srcdir) as sd:

            for script in scripts:
                with File(script) as scr:
                    _, fname, _ = scr.file_parts()
                    outfile: str = sd.join(f"{fname}.rst")

                if not os.path.exists(outfile):
                    document_shell_script(
                        file=script,
                        outfile=outfile,
                        convert_tabs_to_spaces=convert_tabs_to_spaces,
                        num_spaces=num_spaces,
                    )
                else:
                    print(
                        f"\n{fname}: Script documentation already exists. Remove {outfile} if script/code documentation needs to be updated.\n"
                    )

                rsts.add(outfile)
    return rsts


def file_search(pkg_dir: str) -> Set[str]:
    """File search for shell/scripting files.

    Args:
        pkg_dir: Package path.

    Returns:
        Set of strings.
    """
    files: Set[str] = set()

    for root, _, filenames in os.walk(pkg_dir, topdown=True, followlinks=True):
        if len(filenames) > 0:
            for file in filenames:
                fname: str = os.path.join(root, file)
                if auto_detect(infile=fname) is not None:
                    files.add(fname)
    return files
