"""Utility functions.
"""
import os
import re

from typing import List, Optional, Tuple, Union


def read_file(infile: str, /, encoding: Optional[str] = "utf-8") -> List[str]:
    """Reads input file into list of strings.

    Args:
        infile: Argument only input file (of text).
        encoding: Encoding standard. Defaults to "utf-8".

    Returns:
        List of strings.
    """
    infile: str = os.path.abspath(infile)
    with open(infile, mode="r", encoding=encoding) as f:
        contents: List[str] = f.readlines()
    return contents


def write_file(
    outfile: str,
    /,
    text: Union[str, List[str]],
    encoding: Optional[str] = "utf-8",
    prepend_char: Optional[str] = None,
    append_char: Optional[str] = None,
    convert_tabs_to_spaces: bool = False,
    num_spaces: Optional[int] = 4,
    mode: str = "a",
) -> None:
    """Writes text to some output file.

    Args:
        outfile: Argument only output file name.
        text: Text to be written to file.
        encoding: Encoding standard. Defaults to "utf-8".
        prepend_char: Characters to be prepended to text. Defaults to None.
        append_char: Characters to be appended to text. Defaults to None.
        convert_tabs_to_spaces: Convert tabs to spaces. Defaults to False.
        num_spaces: Number of spaces to replace tabs with. Only applicable when ``convert_tabs_to_spaces`` is True. Defaults to 4.
        mode: Opening mode option - arguments are the same as python's built-in ``open`` function. Defaults to "a" (append).
    """
    if prepend_char is None:
        prepend_char: str = ""
    else:
        prepend_char: str = str(prepend_char)

    if append_char is None:
        append_char: str = ""
    else:
        append_char: str = str(append_char)

    if isinstance(text, str):
        text: List[str] = [text]

    if convert_tabs_to_spaces:
        text: List[str] = tabs2spaces(text, replacement_spaces=int(num_spaces))

    with open(outfile, mode=mode, encoding=encoding) as f:
        f.writelines([prepend_char + x + append_char for x in text])
    return None


def tabs2spaces(
    text: Union[str, List[str]], /, replacement_spaces: Optional[Union[int, str]] = None
) -> List[str]:
    """Converts tabs to spaces.

    NOTE:
        * The return type of this function is **ALWAYS** a list of strings.
        * Replacement of the tabs to spaces is performed in place (i.e. the list is modified in place).

    Args:
        text: Argument only input string or list of strings that correpond to text.
        replacement_spaces: String **OR** number of replacement spaces to replace tabs. Defaults to None.

    Raises:
        TypeError: Exception that is raised if ``replacement_spaces`` is not an ``int`` or ``str``.

    Returns:
        List of strings with tabs replaced with spaces.
    """
    if isinstance(text, str):
        text: List[str] = [text]

    if replacement_spaces is None:
        replacement_spaces: str = ""
    elif isinstance(replacement_spaces, int):
        n: int = replacement_spaces
        replacement_spaces: str = ""
        for i in range(n):
            replacement_spaces += " "
    elif isinstance(replacement_spaces, str):
        pass
    else:
        raise TypeError(
            f"Input replacement_spaces: {replacement_spaces} is not an integer or string."
        )

    for i, alpha_numerics in enumerate(text):
        text[i] = re.sub(pattern="\t", repl=replacement_spaces, string=alpha_numerics)
    return text


def spaces2tabs(
    text: Union[str, List[str]], /, num_spaces: Optional[Union[int, str]] = None
) -> List[str]:
    """Converts spaces to tabs.

    NOTE:
        * The return type of this function is **ALWAYS** a list of strings.
        * Replacement of the spaces to tabs is performed in place (i.e. the list is modified in place).

    Args:
        text: Argument only input string or list of strings that correpond to text.
        num_spaces: String **OR** number of replacement tabs to replace spaces. Defaults to None.

    Raises:
        TypeError: Exception that is raised if ``num_spaces`` is not an ``int`` or ``str``.

    Returns:
        List of strings with spaces replaced with tabs.
    """
    if isinstance(text, str):
        text: List[str] = [text]

    if num_spaces is None:
        num_spaces: str = ""
    elif isinstance(num_spaces, int):
        n: int = num_spaces
        num_spaces: str = ""
        for i in range(n):
            num_spaces += " "
    elif isinstance(num_spaces, str):
        pass
    else:
        raise TypeError(f"Input num_spaces: {num_spaces} is not an integer or string.")

    for i, alpha_numerics in enumerate(text):
        text[i] = re.sub(pattern=num_spaces, repl="\t", string=alpha_numerics)
    return text


def file_parts(file: str, /) -> Tuple[str, str, str]:
    """Similar to MATLAB's fileparts function.

    Separates input filename into directory path, filename, and file extension.

    Args:
        file: Argument only input file name.

    Returns:
        Tuple of strings that consists of the directory path, filename, and extension.
    """
    file: str = os.path.abspath(file)
    directory, _filename = os.path.split(file)
    _, ext = os.path.splitext(file)
    filename: str = _filename[: -len(ext)]
    return directory, filename, ext
