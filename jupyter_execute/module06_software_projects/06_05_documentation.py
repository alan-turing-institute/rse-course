#!/usr/bin/env python
# coding: utf-8

# # 6.5 Documentation

# *Estimated time for this notebook: 10 minutes*

# ## Documentation is hard

# 
# * Good documentation is hard, and very expensive.
# * Bad documentation is detrimental.
# * Good documentation quickly becomes bad if not kept up-to-date with code changes.
# * Professional companies pay large teams of documentation writers.
# 

# ## Prefer readable code with tests and vignettes

# 
# If you don't have the capacity to maintain great documentation,
# focus on:
# 
# * Readable code
# * Automated tests
# * Small code samples demonstrating how to use the api
# 

# ## Comment-based Documentation tools

# 
# Documentation tools can produce extensive documentation about your code by pulling out comments near the beginning of functions,
# together with the signature, into a web page.
# 
# The most popular is [Doxygen](http://www.stack.nl/~dimitri/doxygen/)
# 
# [Have a look at an example of some Doxygen output](
# http://www.bempp.org/cppref/2.0/group__abstract__boundary__operators.html)
# 
# [Sphinx](http://sphinx-doc.org/) is nice for Python, and works with C++ as well.
# Here's some [Sphinx-generated output](http://www.bempp.org/pythonref/2.0/bempp_visualization2.html)
# and the [corresponding source code](https://github.com/bempp/bempp/blob/master/python/bempp/visualization2.py)
# [Breathe](http://michaeljones.github.io/breathe/ ) can be used to make Sphinx and Doxygen work together.
# 
# [Roxygen](http://www.rstudio.com/ide/docs/packages/documentation) is good for R.
# 

# # Example of using Sphinx

# ## Write some docstrings

# We're going to document our "greeter" example using docstrings with Sphinx.
# 
# There are various conventions for how to write docstrings, but the native sphinx one doesn't look nice when used with
# the built in `help` system.
# 
# In writing Greeter, we used the docstring conventions from NumPy.
# So we use the [numpydoc](https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt) sphinx extension to 
# support these.

# ```python
# """ 
# Generate a greeting string for a person.
# 
# Parameters
# ----------
# personal: str
#     A given name, such as Will or Jean-Luc
# 
# family: str
#     A family name, such as Riker or Picard
# title: str
#     An optional title, such as Captain or Reverend
# polite: bool
#     True for a formal greeting, False for informal.
# 
# Returns
# -------
# string
#     An appropriate greeting
# """
# ```

# ## Set up sphinx

# 
# Invoke the [sphinx-quickstart](http://sphinx-doc.org/tutorial.html) command to build Sphinx's
# configuration file automatically based on questions
# at the command line:
# 

# ``` bash
# sphinx-quickstart docs
# ```

# (`docs` is the name of the directory where the documentation will be stored)
# 
# Which responds:

# ```bash
# Welcome to the Sphinx 4.4.0 quickstart utility.
# 
# Please enter values for the following settings (just press Enter to
# accept a default value, if one is given in brackets).
# 
# Selected root path: docs
# 
# You have two options for placing the build directory for Sphinx output.
# Either, you use a directory "_build" within the root path, or you separate
# "source" and "build" directories within the root path.
# > Separate source and build directories (y/n) [n]: n
# 
# The project name will occur in several places in the built documentation.
# > Project name: greetings
# > Author name(s): The Alan Turing Institute
# > Project release []: 0.0.1
# 
# If the documents are to be written in a language other than English,
# you can select a language here by its language code. Sphinx will then
# translate text that it generates into that language.
# 
# For a list of supported codes, see
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
# > Project language [en]:
# 
# Creating file module06_software_projects/Greetings/docs/conf.py.
# Creating file module06_software_projects/Greetings/docs/index.rst.
# Creating file module06_software_projects/Greetings/docs/Makefile.
# Creating file module06_software_projects/Greetings/docs/make.bat.
# 
# Finished: An initial directory structure has been created.
# 
# You should now populate your master file module06_software_projects/Greetings/docs/index.rst
# and create other documentation source files. Use the Makefile to build the docs, like so:
#    make builder
# where "builder" is one of the supported builders, e.g. html, latex or linkcheck.
# ```

# and then look at and adapt the generated config, which in our case is a file called `conf.py` in the `docs/` directory of the project. This contains the project's Sphinx configuration, as Python variables. Let's populate the `extensions` field with some extensions we'd like to use (see the [extensions documentation](https://www.sphinx-doc.org/en/master/usage/extensions/index.html)):

# ``` python
# #Add any Sphinx extension module names here, as strings. They can be
# #extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
# extensions = [
#     "sphinx.ext.autodoc",  # Support automatic documentation
#     "sphinx.ext.coverage", # Automatically check if functions are documented
#     "sphinx.ext.mathjax",  # Allow support for algebra
#     "sphinx.ext.viewcode", # Include the source code in documentation
#     "numpydoc",            # Support NumPy style docstrings
# ]
# ```

# We've added some other configuration options to `conf.py` the file in the repo too (but normally you'll use `sphinx-quickstart`).
# 

# ## Define the root documentation page

# 
# Sphinx uses [RestructuredText](http://docutils.sourceforge.net/rst.html) another wiki markup format similar to Markdown.
# 
# `sphinx-quickstart` creates a template `index.rst` for us, which can be edited to contain any preamble text you want. Here it is:
# 
# ```rst
# .. greetings documentation master file, created by
#    sphinx-quickstart on Thu Aug  4 11:47:51 2022.
#    You can adapt this file completely to your liking, but it should at least
#    contain the root `toctree` directive.
# 
# Welcome to greetings's documentation!
# =====================================
# 
# .. toctree::
#    :maxdepth: 2
#    :caption: Contents:
# 
# 
# 
# Indices and tables
# ==================
# 
# * :ref:`genindex`
# * :ref:`modindex`
# * :ref:`search`
# ```
# 

# And a lightly modified version:

# In[1]:


get_ipython().run_cell_magic('writefile', 'Greetings/docs/index.rst', 'Welcome to Greetings\'s documentation!\n=====================================\nSimple "Hello, James" module developed to teach research software engineering.\n\n.. toctree::\n   :maxdepth: 2\n   :caption: Contents:\n\n\nFunctions\n=========\n\n.. autofunction:: greetings.greeter.greet\n\n\nIndices and tables\n==================\n\n* :ref:`genindex`\n* :ref:`modindex`\n* :ref:`search`\n')


# ##  Run sphinx

# 
# We can run Sphinx using:
# 

# In[2]:


get_ipython().run_cell_magic('bash', '', 'cd Greetings/\nsphinx-build docs docs/output\n')


# ## Sphinx output

# Sphinx's output is html, if you open the `Greetings/docs/output/index.html` file you'll see a simple documentation page for our `greetings` package has been created. We just created a simple single function's documentation, but Sphinx will create multiple nested pages of documentation automatically for many functions.

# ## Hosting documentation
# 
# If you'd like to make your documentation available online two of the most popular (free) hosting services are [GitHub pages](https://pages.github.com/), and [Read the docs](https://readthedocs.org/). Both can host documentation generated by Sphinx and have ways to automatically build and update your documentation when changes are made.
# 
# We have the example Greetings docs page on GitHub pages here: https://alan-turing-institute.github.io/Greetings/, which is built using [this GitHub Actions workflow](https://github.com/alan-turing-institute/Greetings/blob/main/.github/workflows/docs.yml).
