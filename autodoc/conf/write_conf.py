"""Generate text/information for sphinx configuration file for automated documentation.
"""
from typing import Dict

from commandio.fileio import File
from commandio.workdir import WorkDir


def write_conf(
    outdir: str,
    pkg_path: str,
    project: str,
    copyright: str,
    author: str,
    release: str,
    theme: str,
) -> str:
    """Writes sphinx configuration information to ``conf.py``.

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
    # Helper function args dict
    conf_args: Dict[str, str] = {
        "pkg_path": pkg_path,
        "project": project,
        "copyright": copyright,
        "author": author,
        "release": release,
        "theme": theme,
    }

    with WorkDir(outdir) as od:
        sourcedir: str = od.join("doc", "source")
        with WorkDir(sourcedir) as sd:
            conf_file: str = sd.join("conf.py")
            conf_text: str = _conf_info(**conf_args)
            with File(conf_file) as cf:
                cf.write(conf_text)
    return conf_file


def _conf_info(
    pkg_path: str, project: str, copyright: str, author: str, release: str, theme: str
) -> str:
    """Helper function for sphinx configuration file information.

    This function fills in the details for a sphinx ``conf.py`` file.

    Args:
        pkg_path: Package path information.
        project: Project name.
        copyright: Copyright information.
        author: Author name.
        release: Release/version number/ID.
        theme: Sphinx theme.

    Returns:
        Returns sphinx configuration file text as strings.
    """
    _CONF_TEXT = f"""# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

_pkg_path: str = os.path.abspath("{pkg_path}")
sys.path.insert(0, _pkg_path)


# -- Project information -----------------------------------------------------

project = "{project}"
copyright = "{copyright}"
author = "{author}"

# The full version, including alpha/beta/rc tags
release = "{release}"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinxarg.ext",
    "sphinx_autodoc_typehints",
    "myst_parser",
    "sphinx.ext.intersphinx",
    "sphinx_tabs.tabs",
    "sphinx.ext.viewcode",
    "sphinx-rtd-dark-mode",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# Sphinx-tab configuration
sphinx_tabs_valid_builders = ["linkcheck"]
sphinx_tabs_disable_tab_closing = True
sphinx_tabs_disable_css_loading = False


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "{theme}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

    """
    return _CONF_TEXT
