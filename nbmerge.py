#!/usr/bin/env python
# From https://gist.github.com/fperez/e2bbc0a208e82e450f69
# Note, updated version of 
# https://github.com/ipython/ipython-in-depth/blob/master/tools/nbmerge.py
"""
usage:
python nbmerge.py A.ipynb B.ipynb C.ipynb > merged.ipynb
"""
from __future__ import print_function

import io
import os
import sys

from nbformat import read as nb_read
from nbformat import writes as nb_write

def merge_notebooks(filenames, outfile):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nb_read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            # TODO: add an optional marker between joined notebooks
            # like an horizontal rule, for example, or some other arbitrary
            # (user specified) markdown cell)
            merged.cells.extend(nb.cells)
    if not hasattr(merged.metadata, 'name'):
        merged.metadata.name = ''
    merged.metadata.name += "_merged"
    result = nb_write(merged)
    with io.open(outfile, 'w', encoding='utf-8') as out:
        out.write(result)

if __name__ == '__main__':
    notebooks = sys.argv[1:-1]
    outfile = sys.argv[-1]
    if not notebooks:
        print(__doc__, file=sys.stderr)
        sys.exit(1)

    merge_notebooks(notebooks, outfile)
