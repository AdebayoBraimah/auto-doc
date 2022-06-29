"""Automatically document shell script code.
"""
import os

from typing import Dict, List, Optional, Union

from util import file_parts, read_file, write_file


def document_shell_script(
    file: str,
    outfile: str,
    encoding: Optional[str] = "utf-8",
    convert_tabs_to_spaces: bool = True,
    num_spaces: Optional[int] = 4,
) -> None:
    """Documents shell scripts by writing their code to Restructured text code block.

    NOTE:
        * Input files may also include other types files that can be run from the command line e.g.:
            * ruby
            * perl
            * zsh, etc.
        * ``outfile`` should be a **.rst** file.

    Args:
        file: Input script/file path.
        outfile: Output file path.
        encoding: Encoding standard. Defaults to "utf-8".
        convert_tabs_to_spaces: Convert tabs to spaces. Defaults to True.
        num_spaces: Number of spaces to replace tabs with. Only applicable when ``convert_tabs_to_spaces`` is True. Defaults to 4.
    """
    file: str = os.path.abspath(file)
    script_type: str = _auto_detect(infile=file, encoding=encoding)
    _, fname, ext = file_parts(file)

    title: str = f"""{fname}\n~~~~~~~~~~~~~~~~~~~~~~~\n\n"""
    preamble: str = f"""Documentation/code for ``{fname}`` {script_type}{ext} script shown below: \n\n"""

    text: List[str] = read_file(file, encoding=encoding)
    block: str = f""".. code-block:: {script_type}\n\n"""

    # Write title
    write_file(
        outfile,
        text=title,
        prepend_char=None,
        convert_tabs_to_spaces=convert_tabs_to_spaces,
        num_spaces=num_spaces,
        mode="w",
    )

    # Write preamble/brief statement
    write_file(
        outfile,
        text=preamble,
        prepend_char=None,
        convert_tabs_to_spaces=convert_tabs_to_spaces,
        num_spaces=num_spaces,
        mode="a",
    )

    # Start code block.
    write_file(
        outfile,
        text=block,
        prepend_char=None,
        convert_tabs_to_spaces=convert_tabs_to_spaces,
        num_spaces=num_spaces,
        mode="a",
    )

    # Write script code/information to file
    write_file(
        outfile,
        text=text,
        prepend_char="\t",
        convert_tabs_to_spaces=convert_tabs_to_spaces,
        num_spaces=num_spaces,
        mode="a",
    )
    return None


def _auto_detect(infile: str, encoding: Optional[str] = "utf-8") -> Union[str, None]:
    """Helper function that auto-detects input file type (e.g. bash/shell, ruby, perl script) and returns the shell/file type.

    Args:
        infile: Input file.
        encoding: Encoding standard. Defaults to "utf-8".

    Returns:
        File type as a string **OR** None if the file type cannot be inferred.
    """
    infile: str = os.path.abspath(infile)
    _, _, _ext = file_parts(infile)

    # Dictionary of common shebangs
    shell_dict: Dict[str, str] = {
        "sh": "bash",
        "bash": "bash",
        "zsh": "zsh",
        "ruby": "ruby",
        "rb": "ruby",
        "perl": "perl",
        "pl": "perl",
        "yml": "yaml",
        "yaml": "yaml",
        "json": "json",
    }

    ext: str = _ext[1:].lower()

    # Check file extension to infer file/script type
    if shell_dict.get(ext, None) is not None:
        return shell_dict.get(ext)

    # If file extension is not available - assume
    #   file/script is an executable, check
    #   shebang.
    text: List[str] = read_file(infile, encoding=encoding)

    _shebangs: List[str] = ["bash", "zsh", "ruby", "perl"]

    for shebang in _shebangs:
        if shebang in text[0]:
            return shebang
    return None
