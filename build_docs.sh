#! /bin/bash

# Build the PDF notes and cleanup the single-page HTML output
make clean
make pdf
jupyter-book clean --html .

# Build the HTML output and link the redirect page
make html
cp docs/index.html _build

# Add the .nojekyll directive to stop GitHub Pages excluding directories with underscores
# See https://docs.github.com/en/pages/getting-started-with-github-pages/about-github-pages#static-site-generators
touch _build/.nojekyll
