"""Creates index.rst files for sphinx documentation.
"""

from commandio.workdir import WorkDir


def _init_index(outdir: str):
    with WorkDir(outdir) as od:
        sourcedir: str = od.join("source")
        with WorkDir(sourcedir) as sd:
            idx: str = sd.join("index.rst")
