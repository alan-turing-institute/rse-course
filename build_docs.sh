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
touch _build/html/.nojekyll

# Copy required outputs to the build directory
for SOURCEPATH in module*/*.{png,gif} "module05_testing_your_code/diffusion/htmlcov/index.html"; do
    mkdir -p _build/html/${SOURCEPATH%/*}
    cp $SOURCEPATH _build/html/${SOURCEPATH}
done
