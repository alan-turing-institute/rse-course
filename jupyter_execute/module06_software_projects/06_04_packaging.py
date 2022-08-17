#!/usr/bin/env python
# coding: utf-8

# # Packaging

# 
# Once we've made a working program, we'd like to be able to use it across our system and to share it with others. To do this we need to create our own Python package.
# 
# As an example, we'll create a package from the `greeter.py` and `command.py` files from the previous notebook. But we'll delete the files created last time first, to start from a clean slate:

# In[1]:


# Tidy up files created by previous notebook
import os

files = ["greeter.py", "command.py"]
for f in files:
    if os.path.exists(f):
        os.remove(f)


# ## Laying out a project

# 
# When planning to package a project for distribution, defining a suitable
# project layout is essential. We have a typical example of a package layout in the `Greetings` directory, which looks like this:
# 
# 
# 

# ```
# Greetings                 <--- Parent directory for your project (your git repo)
# ├── greetings             <--- Directory containing the code for your package
# │  ├── __init__.py        <--- Tells Python to treat the directory as a package
# │  ├── command.py
# │  └── greeter.py
# ├── LICENSE.md            <--- License to describe how others can use your package
# ├── pyproject.toml        <--- Configuration and metadata for your package
# ├── README.md             <--- Homepage to briefly describe how to install and use your package
# └── tests                 <--- Tests for your package's functionality
#    └── test_greeter.py
# ```

# ## The package directory

# All your library source code should be in a single directory tree under the parent project directory. Libraries are usually structured with multiple files, perhaps one for each class.
# 
# The source code directory (and sub-directories) should contain an `__init__.py` file, which makes Python treat it as a module. **The `__init__.py` file can be empty**.
# 
# With the file layout above, `import greetings`, `import greetings.command`, and `import greetings.greeter` will all be possible after installing the package.
# 
# If we added a sub-directory, to provide functionality for multiple languages for example, with this structure:
# 
# ```
# ├── greetings
# │  ├── __init__.py
# │  ├── command.py
# │  ├── greeter.py
# │  └── languages
# │     ├── __init__.py
# │     ├── english.py
# │     └── italian.py
# ```
# 
# then `import greetings.languages`, `import greetings.languages.english`, and `import greetings.languages.italian` would become available. This is a way to group together related functionality/features in your package.
# 
# **⚠️ Advanced topic:** The contents of the `__init__.py` file(s) is executed when you import a package. A common use case for non-empty `__init__.py` files is to "shortcut" imports for convenience. For example, to import the main `greet` function we'd currently need to do:
# 
# ```python
# from greetings.greeter import greet
# ```
# 
# If we added that import code as a line in `greetings/__init__.py`, it will then be possible to do:
# 
# ```python
# from greetings import greet
# ```

# ## Build systems and config files
# 
# To install your package you need to define a "build system", the tool that will do the work of creating the package, and to provide a configuration file to specify how your package should be built.
# 
# The three most common package config files are:
# 
# - `pyproject.toml` **(preferred)**
# - `setup.cfg`  (may be deprecated in the future)
# - `setup.py`  (may be needed for packages with complex build requirements)
# 
# You'll find a lot of projects that use `setup.py` (which used to be the standard), but for new projects it's recommended to use `pyproject.toml`. [TOML](https://toml.io/en/) is a modern file format for configuration files.
# 
# 
# There are multiple "build systems" that can interpret `pyproject.toml` files and build your package. The original and most ubiquitous is [setuptools](https://setuptools.pypa.io/en/latest/index.html), which we'll use here.
# 
# Other options include [Poetry](https://python-poetry.org/), [Flit](https://flit.pypa.io/en/latest/) and [Hatch](https://hatch.pypa.io/latest/). We'd recommend looking at Poetry as an option for managing dependencies, virtual environments, and packaging together. The structure of `pyproject.toml` will differ depending on the tool you're using.
# 

# ## Using setuptools and pyproject.toml

# ### Specifying the build system
# 
# The `[build-system]` section gives the details the tool that should be used to create the package from our code, in this case `setuptools`:
# 
# ```toml
# [build-system]
# requires = ["setuptools"]  # the build tool to use
# build-backend = "setuptools.build_meta"  # the function to use to build the package
# ```
# 

# ### Specifying project metadata
# 
# The `[project]` section contains metadata about your package, at minimum this should include your package's name (usually the name of your package directory) and a version number:
# 
# ```toml
# [project]
# name = "greetings"
# version = "0.0.1"
# ```

# ### Specifying dependencies
# 
# Rather than in a `requirements.txt` file, your package's dependencies should be specified in `pyproject.toml`. These are passed as a list in the `[project]` section (in this case we only have one dependency, `colorama`):
# 
# ```toml
# [project]
# dependencies = ["colorama ~= 0.4.4"]
# ```

# #### Python version
# 
# If our package requires a certain Python version to work, that can also be specified:
# 
# ```toml
# [project]
# requires-python = ">=3.6"
# ```
# 
# #### Optional dependencies
# 
# Sometimes a package may have extra optional features, with extra dependencies, that not all users need. A common example is development dependencies (e.g. for running tests, building documentation, checking code quality, and similar) that a normal user won't need. Optional dependencies can be specified in the `[project.optional-dependencies]` section:
# 
# ```toml
# [project.optional-dependencies]
# dev = ["pytest ~= 7.1.2"]
# ```
# 
# `dev` is the name of an optional group of dependencies that can be passed to `pip` when installing the package (see below). We could have multiple groups here with different (arbitrary) names and sets of dependencies.

# ### Make a command-line interface

# In the previous notebook we created a script `command.py` that could be run with `python command.py ...` with configurable arguments using `argparse`. We can include scripts like these in the package installation to create a more intuitive CLI (command-line interface) for our library:
# 
# ```toml
# [project.scripts]
# greet = "greetings.command:process"
# ```
# 
# The syntax above means that after installing the package the command `greet` will become available on our system, and running `greet` will call the `process` function in the `greetings/command.py` file. See below for this in action.

# ### Complete pyproject.toml
# 
# All together this is our complete `pyproject.toml` file:
# 
# ```toml
# [build-system]
# requires = ["setuptools"]
# build-backend = "setuptools.build_meta"
# 
# [project]
# name = "greetings"
# version = "0.0.1"
# requires-python = ">=3.6"
# dependencies = ["colorama ~= 0.4.4"]
# 
# [project.optional-dependencies]
# dev = ["pytest ~= 7.1.2"]
# 
# [project.scripts]
# greet = "greetings.command:process"
# ```
# 
# This is a minimal example but there are many other metadata fields you can include and configuration options. See the [setuptools](https://setuptools.pypa.io/en/latest/userguide/pyproject_config.html) and [Python packaging](https://packaging.python.org/en/latest/specifications/declaring-project-metadata/) docs for details.

# ## Installing the package

# 
# 
# 
# We can now install this code with
# 

# In[2]:


get_ipython().run_cell_magic('bash', '', 'cd Greetings\npip install .\n')


# ### Installing optional dependencies
# 
# To install dependencies specified in `[project.optional-dependencies]`, include the name of the optional group in square brackets, like this:

# ```python
# cd Greetings
# pip install ".[dev]"
# ```

# ### Editable mode

# If you modify your source files, you would now find it appeared as if the program doesn't change.
# 
# That's because pip install **copies** the file elsewhere during installation (the location is system-dependent).
# 
# If you want to install a package, but keep working on it, you can install it in "editable mode".

# ⚠️ As of August 2022, `setuptools` does not support editable installs with `pyproject.toml` (only) packages, so you will need a small `setup.py` file to make this work (see below). But this shouldn't be necessary [in the near future](https://discuss.python.org/t/help-testing-pep-660-support-in-setuptools/16904/34?u=astrojuanlu).

# In[3]:


get_ipython().run_cell_magic('writefile', 'Greetings/setup.py', 'from setuptools import setup\n\nsetup()\n')


# Then to install in editable mode:
# 
# ```python
# cd Greetings
# pip install -e ".[dev]"
# ```

# ### Installing from GitHub
# 
# If we have our code in a (public) git repo anyone can now install our package directly from the git URL:

# ```bash
# pip install git+git://github.com/alan-turing-institute/Greetings
# ```

# ### Uploading to PyPI
# 
# We could now submit "greeter" to PyPI so everyone could `pip install greetings` directly. For details see the [Python packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives).
# 
# Note there is very little approval/review process - you can put pretty much anything on PyPI. Keep that in mind and be wary about installing unknown packages!

# ## Using the Package

# 
# The package is now available to use everywhere on the system.
# 
# ⚠️ You may need to restart your Jupyter notebook kernel for the newly installed package to be recognised.
# 

# In[4]:


from greetings.greeter import greet

print(greet("James", "Hetherington"))


# 
# And the scripts are now available as command line commands:
# 
# 
# 

# In[5]:


get_ipython().run_cell_magic('bash', '', 'greet --help\n')


# In[6]:


get_ipython().run_cell_magic('bash', '', 'greet James Hetherington\ngreet --polite James Hetherington\ngreet James Hetherington --title Dr\n')


# Of course, there's more to do when taking code from a quick script and turning it into a proper module. We'll continue to look at this in the rest of the course, but here are some initial ideas:

# ## Write some unit tests

# Contents of `Greetings/tests/test_greeter.py`:

# ```python
# from greetings.greeter import greet
# 
# 
# def test_greeter():
#     inputs = [
#         {"personal": "James", "family": "Hetherington"},
#         {"personal": "James", "family": "Hetherington", "polite": True},
#         {"personal": "James", "family": "Hetherington", "title": "Dr"},
#     ]
#     outputs = [  # codes like \x1b[32m are colours
#         "\x1b[40m\x1b[33mHey, \x1b[47m\x1b[1m\x1b[31mJames Hetherington",
#         "\x1b[40m\x1b[33mHow do you do, \x1b[47m\x1b[1m\x1b[31mJames Hetherington",
#         "\x1b[40m\x1b[33mHey, \x1b[44m\x1b[37mDr \x1b[47m\x1b[1m\x1b[31mJames Hetherington",
#     ]
#     for inp, out in zip(inputs, outputs):
#         assert greet(**inp) == out
# ```

# In[7]:


get_ipython().run_cell_magic('bash', '', 'cd Greetings\npytest\n')


# ## Write a README file

# e.g.:

# In[8]:


get_ipython().run_cell_magic('writefile', 'Greetings/README.md', '\nGreetings!\n==========\n\nThis is a very simple example package used as part of the Turing\n[Research Software Engineering with Python](https://alan-turing-institute.github.io/rse-course) course.\n\nUsage:\n    \nInvoke the tool with greet <FirstName> <Secondname>\n')


# ## Write a license file

# e.g.:

# In[9]:


get_ipython().run_cell_magic('writefile', 'Greetings/LICENSE.md', '\n(C) The Alan Turing Institute 2021\n\nThis "greetings" example package is granted into the public domain.\n')


# ## Write a citation file

# e.g.:

# In[10]:


get_ipython().run_cell_magic('writefile', 'Greetings/CITATION.md', '\nIf you wish to refer to this course, please cite the URL\nhttps://alan-turing-institute.github.io/rse-course\n\nPortions of the material are taken from Software Carpentry\nhttp://swcarpentry.org\n')


# You may well want to formalise this using the [codemeta.json](https://codemeta.github.io/) standard - this doesn't have wide adoption yet, but we recommend it.

# ## Documentation

# This documentation string explains how to use the function; don't worry about this for now, we'll consider
# this next time.

# ```python
# def greet(personal, family, title="", polite=False):
#     """Generate a greeting string for a person.
# 
#     Parameters
#     ----------
#     personal: str
#         A given name, such as Will or Jean-Luc
#     family: str
#         A family name, such as Riker or Picard
#     title: str
#         An optional title, such as Captain or Reverend
#     polite: bool
#         True for a formal greeting, False for informal.
# 
#     Returns
#     -------
#     string
#         An appropriate greeting
#     """
# 
#     greeting = "How do you do, " if polite else "Hey, "
#     greeting = Fore.GREEN + greeting
#     if title:
#         greeting += Fore.BLUE + title + " "
# 
#     greeting += Fore.RED + personal + " " + family + "."
#     return greeting
# ```

# In[11]:


import greetings

help(greetings.greeter.greet)

