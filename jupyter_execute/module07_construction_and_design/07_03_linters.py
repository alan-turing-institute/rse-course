#!/usr/bin/env python
# coding: utf-8

# # 7.3 Linting

# *Estimated time for this notebook: 15 minutes*

# 
# There are automated tools which enforce coding conventions and check for common mistakes. These are called *linters*.
# 

# Do not blindly believe all these automated tools! Style guides are **guides** not **rules**.

# ## Linters Starter Pack
# 
# A good starting point for any Python project is to use `flake8`, `black`, and `isort`. All three should improve the style and consistency of your code whilst requiring minimal setup, and generally they are not opinionated about the way your code is designed, only the way it is formatted and syntax or convention errors.

# ### [flake8](https://flake8.pycqa.org/en/latest/index.html)
# 
# Combines two main tools:
# - [PyFlakes](https://github.com/PyCQA/pyflakes) - checks Python code for syntax errors
# - [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) - checks whether Python code is compliant with PEP8 conventions
# 
# `flake8` only checks code and flags any syntax/style errors, it does not attempt to fix them.
# 
# For example, in the `flake8_example.py` file (in the same directory as this notebook) you'll find this code:

# ```python
# from constants import e
# 
# def circumference(r):
#     return 2 * pi * r
# ```

# Running `flake8` on it gives the following warnings:

# In[1]:


get_ipython().system(' flake8 flake8_example.py')


# The first warning tells us we have imported a variable called `e` but not used it, and the last that we're trying to use a variable called `pi` but haven't defined it anywhere. The 2nd warning indicates that in the [PEP8](https://peps.python.org/pep-0008/#blank-lines) conventions there should be two blank lines before a function definition, but we only have 1.
# 
# ```{admonition} Running on multiple files
# All the examples here run a linter on a single file, but they can be run on all the files in a project at once as well (e.g. by just running `flake8` without a filename).
# ```

# ### [black](https://black.readthedocs.io/)
# 
# A highly opinionated code formatter, which enforces control of minutiae details of your code.
# 
# For example, in the `black_example.py` file (in the same directory as this notebook) you'll find this code:
# 
# ```python
# import numpy as np
# 
# def my_complex_function(important_argument_1,important_argument_2,optional_argument_3 = 3,optional_argument_4 = 4):
#     return np.random.random()*important_argument_1*important_argument_2*optional_argument_3*optional_argument_4
# 
# def hello(name,greet='Hello',end="!"):
#     print(greet,    name,    end)
# ```
# 
# After running black on the file:

# In[2]:


get_ipython().system(' black black_example.py')


# Its contents become:
# 
# ```python
# import numpy as np
# 
# 
# def my_complex_function(
#     important_argument_1,
#     important_argument_2,
#     optional_argument_3=3,
#     optional_argument_4=4,
# ):
#     return (
#         np.random.random()
#         * important_argument_1
#         * important_argument_2
#         * optional_argument_3
#         * optional_argument_4
#     )
# 
# 
# def hello(name, greet="Hello", end="!"):
#     print(greet, name, end)
# ```
# 
# Changes made by `black`:
# - Ensured there are two blank lines before and after function definitions
# - Wrapped long lines intelligently
# - Removed excess whitespace (e.g. between the arguments in the print statement on the last line)
# - Used double quotes `"` for all strings (rather than a mix of `'` and `"`)
# 
# Note that `black` will automatically fix most of the whitespace-related warnings picked up by `flake8` (but it would not fix the import or undefined name errors in the `flake8` example above).

# ```{admonition} Line length
# `black` is not compliant with PEP8 in one way - by default it uses a maximum line length of 88 characters (PEP8 suggests 79 characters). [This is discussed in the black documentation](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#line-length).
# ```

# ### [isort](https://pycqa.github.io/isort/)
# 
# "Sorts" imports alphabetically in groups in the following order:
# 
# 1. standard library imports (_e.g._ `import os`).
# 1. third-party imports (_e.g._ `import pandas`).
# 1. local application/library specific imports (_e.g._ `from .my_python_file import MyClass`).
# 
# with a blank line between each group.
# 
# For example in the file `isort_example.py` (in the same directory as this notebook) we have the following imports:
# 
# ```python
# import pandas as pd
# import os
# from matplotlib import pyplot as plt
# import black_example
# import numpy as np
# import json
# ```
# 
# If we run isort:

# In[3]:


get_ipython().system(' isort isort_example.py')


# It becomes:
# 
# ```python
# import json
# import os
# 
# import numpy as np
# import pandas as pd
# from matplotlib import pyplot as plt
# 
# import black_example
# ```

# Note that `from` imports are placed at the bottom of each group.

# ## Other Linters

# ### [mypy](https://mypy.readthedocs.io/en/stable/)
# 
# If you use type annotations in your code, `mypy` can check it for errors that may result from variables being assigned the wrong type. For example, in the file `mypy_example.py` we have this code:
# 
# ```python
# def hello(name: str, greet: str = "Hello", rep: int = 1) -> str:
#     message: str = ""
#     for _ in range(rep):
#         message += f"{greet} {name}\n"
#     return message
# 
# 
# print(hello("Bob", 5))
# ```
# 
# If we run `mypy` on it:

# In[4]:


get_ipython().system(' mypy mypy_example.py')


# The error tells us we have passed an `int` as the 2nd argument to `hello`, but in the function definition the second argument (`greet`) is defined to be a `str`. We probably meant to write `hello("Bob", rep=5)`.

# ### [pylint](https://www.pylint.org/)
# 
# `pylint` analyses your code for errors, coding standards, and makes suggestions around where code could be refactored. It checks for a much wider range of code quality issues than `flake8` but is also much more likely to pick up _false positives_, i.e. `pylint` is more likely to give you warnings about things you don't want to change.
# 
# Let's run it on the file we used for a `flake8` example earlier:
# 
# ```python
# from constants import e
# 
# def circumference(r):
#     return 2 * pi * r
# ```

# In[5]:


get_ipython().system(' pylint flake8_example.py')


# Compared to `flake8`, in this case `pylint` also warns us that:
# - The `circumference` function doesn't have a docstring
# - The `constants` library we try to import is not available on our system
# - The variable name `r` doesn't follow conventions (single letter variables are discouraged by convention, we could use `radius` instead)

# ### [nbqa](https://nbqa.readthedocs.io/en/latest/index.html)
# 
# `nbqa` allows you to run many Python quality tools (including all the ones we've introduced here) on jupyter notebooks. For example:

# In[6]:


get_ipython().system(' nbqa flake8 07_02_coding_conventions.ipynb')


# ### [pylama](https://klen.github.io/pylama/)
# 
# `pylama` wraps many code quality tools (including `isort`, `mypy`, `pylint` and much of `flake8`) in a single command.

# In[7]:


get_ipython().system(' pylama --linters isort,mccabe,mypy,pycodestyle,pydocstyle,pyflakes,pylint flake8_example.py')


# ## Setup

# ### Compatibility between linters
# 
# If you're using multiple linters in your project you may need to configure them to be compatible with each other. For example, `flake8` warns about lines longer than 79 characters (the PEP8 convention) but `black` will allow lines up to 88 characters by default.
# 
# [This repository](https://github.com/alan-turing-institute/Python-quality-tools) has an example setup for using `black`, `isort`, and `flake8` together. The `.flake8` and `pyproject.toml` configuration files set `flake8` and `isort` to run in modes compatible with `black`.

# ### Ignoring lines of code or linting rules
# 
# There will be times where a linter warns you about something in your code but there's a valid reason it's structured that way and you don't want to change it. Most linters can be configured to ignore specific warnings, either by the type of warning, by file, or by individual code line. For example, adding a `# noqa` comment to a line will make `flake8` ignore it.
# 
# Each linter does this differently so check their documentation (e.g. [flake8](https://flake8.pycqa.org/en/3.1.1/user/ignoring-errors.html), [isort](https://pycqa.github.io/isort/docs/configuration/options.html), [mypy](https://mypy.readthedocs.io/en/stable/config_file.html), [pylint](https://pylint.pycqa.org/en/latest/user_guide/messages/message_control.html)).

# ### Running Linters
# 
# It's a good idea to run linters regularly, or even better to have them setup to run automatically so you don't have to remember. There are various tools to help with that:
# 

# #### IDE Integration
# 
# Many editors/IDEs have integrations with common linters or have their own built-in. This can include highlighting problems inline, or automatically running linters when files are saved, for example. Here is the [VS Code documentation for linting in Python](https://code.visualstudio.com/docs/python/linting).
# 
# There are also tools like [editorconfig](https://editorconfig.org/) to help sharing the conventions used within a project, where each contributor uses different IDEs and tools.

# #### [pre-commit](https://pre-commit.com/) 
# 
# pre-commit is a manager for creating git "hooks" - scripts that run before making a commit. If a hook errors the commit won't be made, and you'll be prompted to fix the problems first. There are `pre-commit` plugins for all the linters discussed here, and it's a good way to ensure all code committed to your repo has had a level of quality control applied to it.

# #### CI
# 
# As well as automating unit tests on a CI system like GitHub Actions it's a good idea to configure them to run linters on your code too.
# 
# [Here is an example](https://github.com/alan-turing-institute/AIrsenal/blob/main/.github/workflows/main.yml) from a repo using `isort`, `flake8` and `black` in a GitHub Action. Note that in a CI setup tools that usually change your code, like `black` and `isort`, will be configured to only check whether there are changes that need to be made.
