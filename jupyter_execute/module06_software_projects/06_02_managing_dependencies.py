#!/usr/bin/env python
# coding: utf-8

# # Managing Dependencies
# 

# ## Specifying Dependencies
# 
# ### `pip` and requirements.txt
# 
# Probably the most well known and ubiquitous way of specifying and installing dependencies in Python is with a `requirements.txt` file. This is a text file with a list of the names of packages your code relies on, for example:
# 
# ```text
# geopy
# imageio
# matplotlib
# numpy
# requests
# ```
# 
# To install dependencies from a `requirements.txt` file do the following:
# 
# ```bash
# pip install -r requirements.txt
# ```
# 
# `requirements.txt` files are not the only way of specifying dependencies, we'll refer to some others and the differences between them here and later in this module.
# 
# 
# ### Pinning versions
# 
# Different versions of libraries may have different features, behaviour, and interfaces. To ensure our code is reproducible and other users (and ourselves in the future) get the same results from running the code, it's a good idea to specify the version of each dependency that should be installed.
# 
# To pin dependencies to specific versions include them in `requirements.txt` like this:
# 
# ```text
# geopy==2.2.0
# imageio==2.19.3
# matplotlib==3.5.2
# numpy==1.23.0
# requests==2.28.1
# ```
# 
# To automatically generate a `requirements.txt` file like this, containing the versions of all the libraries installed in your current Python environment, you can run:
# 
# ```bash
# pip freeze
# ```
# 
# However, note that `pip freeze` won't output only your direct dependencies, but also
# - the dependencies of your dependencies
# - the dependencies of the dependencies of your dependencies
# - ...
# 
# It may be better to only specify your direct dependencies and let the maintainers of those libraries deal with their own dependencies (but that can also come with future problems and incompatibilities in some cases). 
# 
# ### Version ranges
# 
# You don't have to specify an exact version, you can also use comparisons like `<=`, `!=`, and `>=` to give ranges of package versions that are compatible with your code (see [here](https://peps.python.org/pep-0440/#version-specifiers)).
# 
# An interesting one is `~=`, or "approximately equal to". For example, if we specified the numpy dependency as:
# 
# ```text
# numpy~=1.23.0
# ```
# 
# it allows `pip` to install any (newer) `1.23.x` version of numpy (e.g. `1.23.1` or `1.23.5`), but not versions `1.24.0` or later (which may introduce changes that are incompatible with `1.23.0`).
# 
# 
# ### (How) should you pin dependency versions?
# 
# There are potential caveats and pitfalls with all approaches. At the extremes you have:
# 
# - **Not specifying a version**:
#   - Dependencies are likely to introduce breaking changes in the future that will cause your code to fail or give different results.
# 
# - **Pinning an exact version**:
#   - Specific versions may not be available on all platforms. You (or new users of your code) won't get bug and security fixes in new versions.
# 
# For research code, to ensure you get exactly the same results from repeating an analysis on another system (or a fresh installation on the same system) pinning versions is often the best approach.
# 
# 
# ### Updating dependencies
# 
# Running
# 
# ```bash
# pip list --outdated
# ```
# 
# will show a list of installed packages that have newer versions available. You can upgrade to the latest version by running:
# 
# ```bash
# pip install --upgrade PACKAGE_NAME
# ```
# 
# (and then update `requirements.txt` to reflect the new version you're using, if needed).
# 
# This is quite a manual approach and other tools have more streamlined ways of handling the upgrading process. See [Poetry](https://python-poetry.org/), for example.
# 
# There are also automated tools like [dependabot](https://github.blog/2020-06-01-keep-all-your-packages-up-to-date-with-dependabot/) that can look at the dependencies in your GitHub repo and suggest changes to avoid security vulnerabilities.
# 

# ## Virtual Environments
# 
# Specifying dependency versions may not always be enough to give you a working (and future-proof) set up for yourself and other users of your code. For example, you may have:
# 
# - Different projects on your system requiring different versions of a library, or libraries that are incompatible with each other.
# - Libraries that are only available on some platforms (e.g. Linux only) or have different behaviour on other platforms.
# - Projects requiring different versions of Python itself
# 
# For these reasons we'd recommend using a separate "virtual environment" for each project on your system.
# 
# In a virtual environment all the packages you install are isolated from other environments, so you could have one environment using `Python 3.10` and `numpy 1.23.1`, and another using `Python 3.8` and `numpy 1.20.3`, for example.
# 
# 
# ### venv 
# 
# `venv` is included in the Python standard library and can be used to create virtual environments (see the docs [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)).
# 
# To create a virtual environment:

# In[1]:


get_ipython().run_cell_magic('bash', '', '\npython -m venv myenv\n')


# where `myenv` is the name of the directory that will be created to store the environment's configuration. The initial contents of the `myenv` directory are:

# In[2]:


get_ipython().run_cell_magic('bash', '', '\nls -F myenv/\n')


# The `which` bash command returns the path to an executable on your system. Currently, `which python` will return the path to the environment you're using to run the course notebooks: 

# In[3]:


get_ipython().run_cell_magic('bash', '', '\nwhich python\n')


# To use our new virtual environment instead, we need to "activate" it, as follows:

# In[4]:


get_ipython().run_cell_magic('bash', '', 'source myenv/bin/activate\n\nwhich python\n')


# the path to the `python` executable now points to a location in the `myenv` directory (our separate Python virtual environment).
# 
# We can then install and run libraries without it impacting other Python environments on our system, e.g.:

# In[5]:


get_ipython().run_cell_magic('bash', '', 'source myenv/bin/activate\n\npip install pyjokes\npyjoke\n')


# Note:
# - You only need to `activate` the environment once usually. We need to do it in each cell here because using `%%bash` is like creating a new terminal.
# - If you try `which pip` before and after activating the environment you'll see that the virtual environment uses a different `pip` executable as well

# To leave the virtual environment and return to using your system Python (or the previously activated environment), you need to "deactivate" it:

# In[6]:


get_ipython().run_cell_magic('bash', '', 'source myenv/bin/activate\n\necho "======================"\necho "In myenv, python path:"\nwhich python\npyjoke\necho "======================"\n\ndeactivate\n\necho ""\necho "======================"\necho "Outside myenv, python path:"\nwhich python\npyjoke\necho "======================"\n')


# ### conda
# 
# [conda](https://docs.conda.io/en/latest/) is a virtual environment, dependency, and package manager for multiple languages. There are multiple distributions including [Anaconda](https://anaconda.org/), which comes with many common data science libraries pre-installed, and [Miniconda](https://docs.conda.io/en/latest/miniconda.html), which is `conda` without pre-installed dependencies.
# 
# Advantages of conda include:
# 
# - It has binaries built for multiple platforms, e.g. `conda` packages are usually available on Windows, Mac, and Linux (whereas it's quite common to find packages on PyPI that don't have a Windows build, for example).
# - You can use it to install non-Python dependencies.
# - It's an "all-in-one" tool: You can use it to manage your entire Python workflow.
# 
# Some disadvantages:
# - Other users of your code may not have or want to use conda (but everyone using Python will have pip available, for example)
# - There's a bit more bloat than other tools, and the dependency resolver can be quite slow.
# 
# `conda` environments a specified in the YAML format, typically in a file called `environment.yml`, and look like this:
# 
# ```yaml
# name: myenv
# 
# dependencies:
#   - python=3.9
#   - geopy=2.2.0
#   - imageio=2.19.3
#   - matplotlib=3.5.2
#   - numpy=1.23.0
#   - requests=2.28.1
# ```
# 
# Note that a version of Python itself is specified in the dependencies - you can install any version of Python in a conda environment.
# 
# To create the environment:
# 
# ```bash
# conda env create -f environment.yml
# ```
# 
# And to use it:
# 
# ```bash
# conda activate myenv
# 
# # work in the environment
# 
# conda deactivate
# ```
# 

# ## Which to choose?
# 
# There's a large ecosystem of different Python (and general) dependency, environment, and packaging tools, many more than we've seen here. A few other notable ones are:
# 
# - [Docker](https://www.docker.com) - creates isolated "containers" which are whole virtual systems, allowing you to configure everything including the operating system to use. This is a "maximally reproducible" solution that ensures future users of your code get a complete and identical environment from the ground up.
# - [pyenv](https://github.com/pyenv/pyenv) - install and manage different versions of Python 
# - [Poetry](https://python-poetry.org/) - create virtual environments and Python packages, and improved dependency management
# - [setuptools](https://setuptools.pypa.io/en/latest/userguide/quickstart.html) - for creating Python packages (we'll be looking at this later)
# 
# Which are best for your project depends on what you're trying to achieve and personal preference. It's also likely that you'll be using multiple tools as they all have different priorities and features.
# 
# This table gives a rough summary of what the tools mentioned in this course can be used for, loosely ordered from most flexibility (but perhaps most involved setup) at the top, to simpler, single-usecase tools at the botom: 
# 
# |       | Virtual environments | Install non-Python dependencies | Install Python versions | Manage Python dependencies | Create Python packages |
# | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
# | Docker      |  ✅  |  ✅   |  ✅  |  ❌  |  ❌  |
# | conda       |  ✅  |  ✅   |  ✅  |  ✅  |  ✅  |  
# | Poetry      |  ✅  |  ❌  |  ❌  |  ✅  |  ✅  | 
# | pyenv      |  ✅  |  ❌  |  ✅  |   ❌  |  ❌  |
# | setuptools      |  ❌  |  ❌  |  ❌  |  ✅  |  ✅  |
# | venv      |  ✅  |  ❌  |  ❌  |  ❌  |  ❌  |
# | pip      |  ❌  |  ❌  |  ❌  |  ✅  |  ❌  |
# 
# 

# In[ ]:




