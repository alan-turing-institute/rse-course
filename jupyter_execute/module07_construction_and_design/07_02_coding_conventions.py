#!/usr/bin/env python
# coding: utf-8

# # Coding Conventions

# ## One code, many layouts:

# Consider the following fragment of python:
# 
# ```python
# import species
# 
# 
# def AddToReaction(name, reaction):
#     reaction.append(species.Species(name))
# ```

# this could also have been written:
# 
# 
# ```python
# from species import Species
# 
# 
# def add_to_reaction(a_name, a_reaction):
#     l_species = Species(a_name)
#     a_reaction.append(l_species)
# ```

# ## So many choices

# 
# * Layout
# * Naming
# * Syntax choices
# 

# ## Layout

# In[1]:


reaction = {
    "reactants": ["H", "H", "O"],
    "products": ["H2O"]
}


# 
# 
# 
# 

# In[2]:


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

# In[3]:


class ClassName:
    def methodName(variable_name):
        instance_variable = variable_name


# This example uses `underscore_separation` for all the names:

# In[4]:


class class_name:
    def method_name(a_variable):
        m_instance_variable = a_variable


# The usual Python convention (see [PEP8](https://www.python.org/dev/peps/pep-0008)) is UpperCamel for class names, and underscore_separation for function and variable names:

# In[5]:


class ClassName:
    def method_name(variable_name):
        instance_variable = variable_name


# However, particular projects may have their own conventions (and you will even find Python standard libraries that don't follow these conventions). 

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

# In[6]:


big = True
fast = False
color = "brown"
cheap = True

if color == "red" and fast or big and cheap:
    print("Vrroom!")


# In[7]:


exciting = color == "red" and fast
practical = big and cheap

if exciting or practical:
    print("Vrroom!")


# We create extra variables as an intermediate step. Don't worry about the performance now, the compiler will do the right thing.
# 
# What about operator precedence? Being explicit helps to remind yourself what you are doing.

# 
# * Explicit operator precedence
# * Compound expressions
# * Package import choices
# 

# ## Type Annotations
# 
# Python is _dynamically_ typed, which means if a variable `x` is an integer:

# In[8]:


x = 32


# it is valid in Python to make it into a string or any other type later:

# In[9]:


x = "bananas"


# This is not the case in a _statically_ typed language, like C++ or Java. Having this flexibility in Python can be convenient but it can also lead to unexpected, and potentially difficult to diagnose, mistakes if variables in your code have different types to what was expected.
# 
# For example, consider the following function:

# In[10]:


def repeat(x, y, times=2):
    return (x + y) * times


repeat("dog", "woof")


# It looks like a function that repeats its inputs a number of times, but what if the inputs are numbers?

# In[11]:


repeat(2, 3, times=3)


# Ah, that's not what we wanted (we were hoping for 232323).
# 
# To help us remember how the function is supposed to be used, we can add type annotations (or type "hints"):

# In[12]:


def repeat(x: str, y: str, times: int = 3) -> str:
    return (x + y) * times


# The syntax `variable_name: type` indicates the type each parameter should have (`x` and `y` are strings, and `times` is an integer), and the arrow syntax in `function_name(...) -> type` indicates the type of data the function returns (a string for the `repeat` function above).

# Note that type annotating your code will not change it's behaviour (Python does not enforce variables to be their annotated types):

# In[13]:


repeat(2, 3, times=3)


# But they form a kind of documentation to help us understand how the function should be used, and there are tools that can use them to diagnose issues in your code (see the "Linters" section).
# 
# In this case we could do this to get what we expected originally:

# In[14]:


int(repeat("2", "3", times=3))


# See the [Python documentation](https://docs.python.org/3/library/typing.html) for more details on type annotations and the `typing` library. 

# ## Coding Conventions

# 
# You should try to have an agreed policy for your team for these matters.
# 
# If your language or project has a standard policy, use that. For example:
# 
# - **Python**: [PEP8](https://www.python.org/dev/peps/pep-0008/)
# - **R**: [Google's guide for R](https://google.github.io/styleguide/Rguide.xml), [tidyverse style guide](https://style.tidyverse.org/)
# - **C++**: [Google's style guide](https://google.github.io/styleguide/cppguide.html), [Mozilla's](https://developer.mozilla.org/en-US/docs/Mozilla/Developer_guide/Coding_Style)
# - **Julia**: [Official style guide](https://docs.julialang.org/en/v1/manual/style-guide/index.html)
# 
