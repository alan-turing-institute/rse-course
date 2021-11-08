#!/usr/bin/env python
# coding: utf-8

# # Documentation

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
# sphinx-quickstart
# ```

# Which responds:

# ```
# Welcome to the Sphinx 3.4.3 quickstart utility.
# 
# Please enter values for the following settings (just press Enter to
# accept a default value, if one is given in brackets).
# 
# Selected root path: .
# 
# You have two options for placing the build directory for Sphinx output.
# Either, you use a directory "_build" within the root path, or you separate
# "source" and "build" directories within the root path.
# > Separate source and build directories (y/n) [n]:
# ```

# and then look at and adapt the generated config, which in our case is a file called `conf.py` in the `doc/source/` directory of the project. This contains the project's Sphinx configuration, as Python variables, for example:

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

# To proceed with the example, we'll copy a finished `conf.py` into our folder, though normally you'll always use `sphinx-quickstart`
# 

# In[1]:


get_ipython().run_cell_magic('writefile', 'greetings/doc/source/conf.py', '# -- Project information -----------------------------------------------------\n\nproject = u"Greetings"\ncopyright = u"2021, James Hetherington"\nauthor = "James Hetherington"\n\n# The full version, including alpha/beta/rc tags\nrelease = "0.1"\n\n\n# -- General configuration ---------------------------------------------------\n\n# Add any Sphinx extension module names here, as strings. They can be\n# extensions coming with Sphinx (named \'sphinx.ext.*\') or your custom\n# ones.\nextensions = [\n    "sphinx.ext.autodoc",  # Support automatic documentation\n    "sphinx.ext.coverage",  # Automatically check if functions are documented\n    "sphinx.ext.mathjax",  # Allow support for algebra\n    "sphinx.ext.viewcode",  # Include the source code in documentation\n    "numpydoc",  # Support NumPy style docstrings\n]\n\n# Add any paths that contain templates here, relative to this directory.\ntemplates_path = ["_templates"]\n\n# List of patterns, relative to source directory, that match files and\n# directories to ignore when looking for source files.\n# This pattern also affects html_static_path and html_extra_path.\nexclude_patterns = ["Thumbs.db", ".DS_Store"]\n\n# The suffix(es) of source filenames.\n# You can specify multiple suffix as a list of string:\nsource_suffix = ".rst"\n\n# The master toctree document.\nmaster_doc = "index"\n\n# The name of the Pygments (syntax highlighting) style to use.\npygments_style = "sphinx"\n\n\n# -- Options for HTML output -------------------------------------------------\n\n# The theme to use for HTML and HTML Help pages.  See the documentation for\n# a list of builtin themes.\nhtml_theme = "alabaster"\n\n# Add any paths that contain custom static files (such as style sheets) here,\n# relative to this directory. They are copied after the builtin static files,\n# so a file named "default.css" will overwrite the builtin "default.css".\nhtml_static_path = ["_static"]\n\n\n# -- Options for LaTeX output ------------------------------------------------\n\nlatex_elements = {}\n\n# Grouping the document tree into LaTeX files. List of tuples\n# (source start file, target name, title, author,\n#  documentclass [howto, manual, or own class]).\nlatex_documents = [\n    (\n        "index",\n        "Greetings.tex",\n        u"Greetings Documentation",\n        u"James Hetherington",\n        "manual",\n    ),\n]\n\n\n# -- Options for manual page output ------------------------------------------\n\n# One entry per manual page. List of tuples\n# (source start file, name, description, authors, manual section).\nman_pages = [\n    ("index", "greetings", u"Greetings Documentation", [u"James Hetherington"], 1)\n]\n\n# -- Options for Texinfo output ----------------------------------------------\n\n# Grouping the document tree into Texinfo files. List of tuples\n# (source start file, target name, title, author,\n#  dir menu entry, description, category)\ntexinfo_documents = [\n    (\n        "index",\n        "Greetings",\n        u"Greetings Documentation",\n        u"James Hetherington",\n        "Greetings",\n        "One line description of project.",\n        "Miscellaneous",\n    ),\n]')


# ## Define the root documentation page

# 
# Sphinx uses [RestructuredText](http://docutils.sourceforge.net/rst.html) another wiki markup format similar to Markdown.
# 
# You define an `index.rst` file to contain any preamble text you want. The rest is autogenerated by `sphinx-quickstart`
# 
# 
# 
# 
# 
# 

# In[2]:


get_ipython().run_cell_magic('writefile', 'greetings/doc/source/index.rst', 'Welcome to Greetings\'s documentation!\n=====================================\nSimple "Hello, James" module developed to teach research software engineering.\n\n.. toctree::\n   :maxdepth: 2\n   :caption: Contents:\n\n\nFunctions\n=========\n\n.. autofunction:: greetings.greeter.greet\n\n\nIndices and tables\n==================\n\n* :ref:`genindex`\n* :ref:`modindex`\n* :ref:`search`')


# ##  Run sphinx

# 
# We can run Sphinx using:
# 

# In[3]:


get_ipython().run_cell_magic('bash', '', 'cd greetings/\nsphinx-build doc/source doc/output')


# ## Sphinx output

# Sphinx's output is [html](https://alan-turing-institute.github.io/rsd-engineeringcourse/ch04packaging/greetings/doc/index.html). We just created a simple single function's documentation, but Sphinx will create multiple nested pages of documentation automatically for many functions.
