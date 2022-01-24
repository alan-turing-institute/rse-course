#!/usr/bin/env python
# coding: utf-8

# # Coding Conventions

# Let's import first the context for this chapter.

# In[1]:


from context import *


# ## One code, many layouts:

# 
# Consider the following fragment of python:
# 
# 
# 

# In[2]:


import species


def AddToReaction(name, reaction):
    reaction.append(species.Species(name))


# 
# 
# 
# this could also have been written:
# 
# 
# 

# In[3]:


from species import Species


def add_to_reaction(a_name, a_reaction):
    l_species = Species(a_name)
    a_reaction.append(l_species)


# ## So many choices

# 
# * Layout
# * Naming
# * Syntax choices
# 

# ## Layout

# In[4]:


reaction = {
    "reactants": ["H", "H", "O"],
    "products": ["H2O"]
}


# 
# 
# 
# 

# In[5]:


reaction2 = {
    "reactants":
    [
        "H",
        "H",
        "O"
    ],
    "products":
    [
        "H2O"
    ]
}


# ## Layout choices

# 
# * Brace style
# * Line length
# * Indentation
# * Whitespace/Tabs
# 
# Inconsistency will produce a mess in your code! Some choices will make your code harder to read, whereas others may affect the code. For example, if you copy/paste code with tabs in a place that's using spaces, they may appear OK in your screen but it will fail when running it.

# ## Naming Conventions

# [Camel case](https://en.wikipedia.org/wiki/Camel_case) is used in the following example, where class name is in UpperCamel, functions in lowerCamel and underscore_separation for variables names:

# In[6]:


class ClassName:
    def methodName(variable_name):
        instance_variable = variable_name


# This example uses `underscore_separation` for all the names:

# In[7]:


class class_name:
    def method_name(a_variable):
        m_instance_variable = a_variable


# The usual Python convention (see [PEP8](https://www.python.org/dev/peps/pep-0008)) is UpperCamel for class names, and underscore_separation for function and variable names:

# In[8]:


class ClassName:
    def method_name(variable_name):
        instance_variable = variable_name


# However, particular projects may have their own conventions (and you will even find Python standard libraries that don't follow these conventions). 

# ## Hungarian Notation

# 
# Prefix denotes *type*:
# 
# 
# 

# In[9]:


fNumber = float(sEntry) + iOffset


# So in the example above we know that we are creating a `f`loat number as a composition of a `s`tring entry and an `i`nteger offset.
# 
# People may find this useful in languages like Python where the type is intrinsic in the variable.

# In[10]:


number = float(entry) + offset


# 
# ## Newlines

# 
# * Newlines make code easier to read
# * Newlines make less code fit on a screen
# 
# Use newlines to describe your code's *rhythm*.
# 

# ## Syntax Choices

# The following two snippets do the same, but the second is separated into more steps, making it more readable.

# In[11]:


anothervariable += 1
if (variable == anothervariable) and flag1 or flag2:
    do_something()


# In[12]:


anothervariable = anothervariable + 1
variable_equality = variable == anothervariable
if (variable_equality and flag1) or flag2:
    do_something()


# We create extra variables as an intermediate step. Don't worry about the performance now, the compiler will do the right thing.
# 
# What about operator precedence? Being explicit helps to remind yourself what you are doing.

# 
# * Explicit operator precedence
# * Compound expressions
# * Package import choices
# 

# ## Coding Conventions

# 
# You should try to have an agreed policy for your team for these matters.
# 
# If your language sponsor has a standard policy, use that. For example:
# 
# - **Python**: [PEP8](https://www.python.org/dev/peps/pep-0008/)
# - **R**: [Google's guide for R](https://google.github.io/styleguide/Rguide.xml), [tidyverse style guide](https://style.tidyverse.org/)
# - **C++**: [Google's style guide](https://google.github.io/styleguide/cppguide.html), [Mozilla's](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Coding_Style)
# - **Julia**: [Official style guide](https://docs.julialang.org/en/v1/manual/style-guide/index.html)
# 

# ## Lint

# 
# There are automated tools which enforce coding conventions and check for common mistakes.
# 
# These are called *linters*:
# 
# E.g. `pip install` [pycodestyle](https://pypi.org/project/pycodestyle/)
# 
# 
# 

# In[13]:


get_ipython().run_cell_magic('bash', '', 'pycodestyle species.py')


# 
# 
# 
# It is a good idea to run a linter before every commit, or include it in your CI tests.
# 
# 

# There are other tools that help with linting that are worth mentioning.
# With `pylint` you can also get other useful information about the quality of your code:
# 
# `pip install` [pylint](https://www.pylint.org/)
# 

# In[14]:


get_ipython().run_cell_magic('bash', '', 'pylint species.py || echo "Note the linting failures"')


# and with [black](https://black.readthedocs.io/) you can fix all the errors at once.
# ```bash
# black species.py
# ```
# These linters can be configured to choose which points to flag and which to ignore.
# 
# Do not blindly believe all these automated tools! Style guides are **guides** not **rules**.

# Finally, there are tools like [editorconfig](https://editorconfig.org/) to help sharing the conventions used within a project, where each contributor uses different IDEs and tools. There are also bots like [pep8speaks](https://pep8speaks.com/) that comments on contributors' pull requests suggesting what to change to follow the conventions for the project.
# 
