# -*- coding: utf-8 -*-
"""Python package that wraps ``sphinx`` documentation package for creating HTML documentation.
"""
import os
import pathlib

from typing import List

name: str = "auto-doc"

_pkg_path: str = os.path.join(str(pathlib.Path(os.path.abspath(__file__)).parents[0]))

_MISCDIR: str = os.path.abspath(os.path.join(_pkg_path, "misc"))

_version_file: str = os.path.abspath(os.path.join(_MISCDIR, "version.txt"))

with open(_version_file, "r") as f:
    file_contents: str = f.read()
    _version: str = file_contents.strip("\n")

__author__: str = "Adebayo Braimah"
__maintainer__: str = __author__
__credits__: List[str] = [
    "Adebayo Braimah",
    "Cincinnati Children's Hospital Medical Center",
    "Imaging Research Center",
    "CCHMC Dept. of Radiology",
]
__license__: str = "GPL"
__version__: str = _version
__maintainer__: str = "Adebayo Braimah"
__email__: str = "adebayo.braimah@gmail.com"
__status__: str = "Development"

# NOTE:
#
# More information about organizing author information:
#   * https://stackoverflow.com/questions/1523427/what-is-the-common-header-format-of-python-files
#   * http://epydoc.sourceforge.net/manual-fields.html#module-metadata-variables
