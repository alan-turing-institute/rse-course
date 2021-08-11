#! /bin/bash

# Build the PDF notes and cleanup the single-page HTML output
make clean
make pdf
jupyter-book clean --html .

# Build the HTML output and link the redirect page
make html
cp docs/index.html _build