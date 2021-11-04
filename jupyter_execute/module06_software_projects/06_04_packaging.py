#!/usr/bin/env python
# coding: utf-8

# # Packaging

# ## Packaging

# 
# Once we've made a working program, we'd like to be able to share it with others.
# 
# A good cross-platform build tool is the most important thing: you can always
# have collaborators build from source.
# 

# ## Distribution tools

# Distribution tools allow one to obtain a working copy of someone else's package.
# 
# Language-specific tools: PyPI, Ruby Gems, CPAN, CRAN
# Platform specific packagers e.g. brew, apt/yum
# 
# Until recently windows didn't have anything like `brew install` or `apt-get`
# You had to build an 'installer', but now there is https://chocolatey.org

# ## Laying out a project

# 
# When planning to package a project for distribution, defining a suitable
# project layout is essential.
# 
# 
# 

# In[1]:


get_ipython().run_cell_magic('bash', '', '#%%cmd (windows)\ntree --charset ascii greetings -I "doc|build|Greetings.egg-info|dist|*.pyc"')


# We can start by making our directory structure

# In[2]:


get_ipython().run_cell_magic('bash', '', 'mkdir -p greetings/greetings/test/fixtures')


# ## Using setuptools

# 
# To make python code into a package, we have to write a `setupfile`:
# 
# 
# 
# 
# 
# 

# In[3]:


get_ipython().run_cell_magic('writefile', 'greetings/setup.py', 'from setuptools import setup, find_packages\n\nsetup(\n    name="Greetings",\n    version="0.1.0",\n    packages=find_packages(exclude=["*test"]),\n    entry_points={"console_scripts": ["greet = greetings.command:process"]},\n)')


# 
# 
# 
# We can now install this code with
# 

# ```
# cd greetings
# pip install .
# ```

# 
# And the package will be then available to use everywhere on the system.
# 

# In[4]:


from greetings.greeter import greet

greet("James", "Hetherington")


# In[5]:


from greetings.greeter import *


# 
# And the scripts are now available as command line commands:
# 
# 
# 

# In[6]:


get_ipython().run_cell_magic('bash', '', 'greet --help')


# In[7]:


get_ipython().run_cell_magic('bash', '', 'greet James Hetherington\ngreet --polite James Hetherington\ngreet James Hetherington --title Dr')


# ## Installing from GitHub

# 
# We could now submit "greeter" to PyPI for approval, so everyone could `pip install` it.
# 
# However, when using git, we don't even need to do that: we can install directly from any git URL:
# 

# ```
# pip install git+git://github.com/jamespjh/greeter
# ```

# In[8]:


get_ipython().run_cell_magic('bash', '', 'greet Humphry Appleby --title Sir')


# ## Convert the script to a module

# 
# Of course, there's more to do when taking code from a quick script and turning it into a proper module:
# 
# 
# 
# 
# 
# 

# In[9]:


get_ipython().run_cell_magic('writefile', 'greetings/greetings/greeter.py', 'def greet(personal, family, title="", polite=False):\n    """Generate a greeting string for a person.\n\n    Parameters\n    ----------\n    personal: str\n        A given name, such as Will or Jean-Luc\n    family: str\n        A family name, such as Riker or Picard\n    title: str\n        An optional title, such as Captain or Reverend\n    polite: bool\n        True for a formal greeting, False for informal.\n\n    Returns\n    -------\n    string\n        An appropriate greeting\n    """\n\n    greeting = "How do you do, " if polite else "Hey, "\n    if title:\n        greeting += title + " "\n\n    greeting += personal + " " + family + "."\n    return greeting')


# In[10]:


import greetings

help(greetings.greeter.greet)


# 
# 
# 
# The documentation string explains how to use the function; don't worry about this for now, we'll consider
# this next time.
# 

# ## Write an executable script

# In[11]:


get_ipython().run_cell_magic('writefile', 'greetings/greetings/command.py', 'from argparse import ArgumentParser\nfrom .greeter import greet  # Note python 3 relative import\n\n\ndef process():\n    parser = ArgumentParser(description="Generate appropriate greetings")\n\n    parser.add_argument("--title", "-t")\n    parser.add_argument("--polite", "-p", action="store_true")\n    parser.add_argument("personal")\n    parser.add_argument("family")\n\n    arguments = parser.parse_args()\n\n    print(\n        greet(arguments.personal, arguments.family, arguments.title, arguments.polite)\n    )\n\n\nif __name__ == "__main__":\n    process()')


# ## Specify dependencies

# We use the setup.py file to specify the packages we depend on:

# ```python
# setup(
#     name = "Greetings",
#     version = "0.1.0",
#     packages = find_packages(exclude=['*test']),
#     install_requires = ['argparse']
# )
# ```

# ## Specify entry point

# In[12]:


get_ipython().run_cell_magic('writefile', 'greetings/setup.py', '\nfrom setuptools import setup, find_packages\n\nsetup(\n    name="Greetings",\n    version="0.1.0",\n    packages=find_packages(exclude=["*test"]),\n    install_requires=["argparse"],\n    entry_points={"console_scripts": ["greet = greetings.command:process"]},\n)')


# ## Write a readme file

# e.g.:

# In[13]:


get_ipython().run_cell_magic('writefile', 'greetings/README.md', '\nGreetings!\n==========\n\nThis is a very simple example package used as part of the Turing\n[Research Software Engineering with Python](https://alan-turing-institute.github.io/rsd-engineeringcourse) course.\n\nUsage:\n    \nInvoke the tool with greet <FirstName> <Secondname>')


# ## Write a license file

# e.g.:

# In[14]:


get_ipython().run_cell_magic('writefile', 'greetings/LICENSE.md', '\n(C) The Alan Turing Institute 2021\n\nThis "greetings" example package is granted into the public domain.')


# ## Write a citation file

# e.g.:

# In[15]:


get_ipython().run_cell_magic('writefile', 'greetings/CITATION.md', '\nIf you wish to refer to this course, please cite the URL\nhttps://alan-turing-institute.github.io/rsd-engineeringcourse\n\nPortions of the material are taken from Software Carpentry\nhttp://swcarpentry.org')


# You may well want to formalise this using the [codemeta.json](https://codemeta.github.io/) standard - this doesn't have wide adoption yet, but we recommend it.

# ## Define packages and executables

# In[16]:


get_ipython().run_cell_magic('bash', '', 'touch greetings/greetings/test/__init__.py\ntouch greetings/greetings/__init__.py')


# ## Write some unit tests

# 
# Separating the script from the logical module made this possible:
# 
# 
# 
# 
# 
# 

# In[17]:


get_ipython().run_cell_magic('writefile', 'greetings/greetings/test/test_greeter.py', 'import yaml\nimport os\nfrom ..greeter import greet\n\n\ndef test_greeter():\n    with open(\n        os.path.join(os.path.dirname(__file__), "fixtures", "samples.yaml")\n    ) as fixtures_file:\n        fixtures = yaml.safe_load(fixtures_file)\n        for fixture in fixtures:\n            answer = fixture.pop("answer")\n            assert greet(**fixture) == answer')


# 
# 
# 
# Add a fixtures file:
# 
# 
# 
# 
# 
# 

# In[18]:


get_ipython().run_cell_magic('writefile', 'greetings/greetings/test/fixtures/samples.yaml', '- personal: James\n  family: Hetherington\n  answer: "Hey, James Hetherington."\n- personal: James\n  family: Hetherington\n  polite: True\n  answer: "How do you do, James Hetherington."\n- personal: James\n  family: Hetherington\n  title: Dr\n  answer: "Hey, Dr James Hetherington."')


# In[19]:


get_ipython().run_cell_magic('bash', '', 'py.test')


# ## Developer Install

# 
# If you modify your source files, you would now find it appeared as if the program doesn't change.
# 
# That's because pip install **copies** the file.
# 
# (On my system to /Library/Python/2.7/site-packages/: this is operating
# system dependent.)
# 
# If you want to install a package, but keep working on it, you can do
# 

# ```
# cd greetings
# pip install -e .
# ```

# ## Distributing compiled code

# 
# If you're working in C++ or Fortran, there is no language specific repository.
# You'll need to write platform installers for as many platforms as you want to
# support.
# 
# Typically:
# 
# * `dpkg` for `apt-get` on Ubuntu and Debian
# * `rpm` for `yum` on Redhat and Fedora
# * `homebrew` on OSX (Possibly `macports` as well)
# * An executable `msi` installer for Windows.
# 

# ## Homebrew

# 
# Homebrew: A ruby DSL, you host off your own webpage
# 
# See my [installer for the cppcourse example](http://github.com/jamespjh/homebrew-reactor)
# 
# If you're on OSX, do:
# 

# ```
# brew tap jamespjh/homebrew-reactor
# brew install reactor
# ```
