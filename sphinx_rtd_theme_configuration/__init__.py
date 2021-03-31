# -*- coding: utf-8 -*-
"""
"""

import os
from pathlib import Path

import sphinx.application
from sphinx.util.fileutil import copy_asset

static = Path(__file__, "..", "_static").resolve()
assert static.exists()
assert static.is_absolute()


def copy_asset_files(app, exc):
    # https://github.com/sphinx-doc/sphinx/issues/1379#issuecomment-809006086
    asset_files = [str(i) for i in static.rglob("*")]
    if exc is None:  # build succeeded
        for path in asset_files:
            copy_asset(path, os.path.join(app.outdir, '_static'))


def setup(app: sphinx.application.Sphinx):
    app.setup_extension("sphinx_rtd_theme")
    app.add_css_file("more-theme.css")
    app.connect('build-finished', copy_asset_files)
