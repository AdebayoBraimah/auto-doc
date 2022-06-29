"""Module for documenting shell/command line code.
"""
import os
from typing import Set

from autodoc.utils.docshell import _auto_detect as auto_detect


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
