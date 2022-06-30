# Configuration file for the Sphinx documentation builder.
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
import pathlib

# __file__="conf.py"
_pkg_path: str = str(pathlib.Path(os.path.abspath(__file__)).parents[2])
sys.path.insert(0, _pkg_path)
sys.path.append(_pkg_path)

from commandio import __author__, __version__ 

# -- Project information -----------------------------------------------------

project = "autodoc"
copyright = f"2022, {__author__}"
author = __author__

# The full version, including alpha/beta/rc tags
release = __version__


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
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

    