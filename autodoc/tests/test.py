import os
import pathlib
import sys

_pkg_path: str = os.path.join(str(pathlib.Path(os.path.abspath(__file__)).parents[2]))
sys.path.append(_pkg_path)

from autodoc.documentation.initialize import doc_init
from autodoc.documentation.write import write
from autodoc.documentation.build import build_docs

outdir: str = "/Users/adebayobraimah/Desktop/projects/auto-doc/autodoc/tests/test.1"
pkg: str = "/Users/adebayobraimah/Desktop/projects/auto-doc/autodoc"

doc_init(outdir=outdir, pkg=pkg)
write(outdir=outdir, pkg=pkg)
build_docs(outdir=outdir)
