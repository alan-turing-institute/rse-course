#!/usr/bin/env python
# coding: utf-8

# # 5.6 Continuous Integration

# *Estimated time for this notebook: 15 minutes*

# ## Getting past "but it works on my machine..."
# 
# Try running the code below:

# In[1]:


get_ipython().run_cell_magic('bash', '', 'rm -rf continuous_int\nmkdir continuous_int\ntouch continuous_int/__init__.py\n')


# In[2]:


get_ipython().run_cell_magic('writefile', 'continuous_int/test_demo.py', 'import sys\nimport re\n\ndef test_platform():\n    assert re.search("\\d", sys.platform)\n\ndef test_replace():\n    assert "".replace("", "A", 2) == "A"\n')


# In[3]:


get_ipython().run_cell_magic('bash', '', 'cd continuous_int\npytest || echo "tests complete"\n')


# The example above is a trival, and deliberate, example of code that will behave differently on different computers.
# 
# Much more subtle instances can occur in real-life, which if allowed to propergate, they can result in bugs and errors that are difficult to trace, let alone fix.
# 
# One mitigation for this problem is to use a process of "Continuous Integration (CI)". This is a process of drawing together all developer contributions as early as possible and freaquently running the automated tests. Typically this involves the use of CI servers, which provide a common and reliable environment to run our tests. (This is not the only use of CI servers - we will touch on other use cases in later modules)

# ## Options for CI Servers
# 
# There are many different open-source or propritory CI Servers available. In some cases it might be appropriate to have [on-permise CI Servers](https://en.wikipedia.org/wiki/Comparison_of_continuous_integration_software) at your organisation.
# 
# There are also a number of Continuous-Integration-Server-as-a-Service products that can be use free-of-charge for open source projects. Here we will expand on ["GitHub Actions"](https://docs.github.com/en/actions) which is a Continuous-Integration-Server-as-a-Service, which is one component of the wider GitHub ecosystem.
# 

# ## Objectives
# 
# We would like to test our code on
# 
# * different operating systems
# * different versions of python
# * each commit to a pull request
# 
# 

# In[4]:


get_ipython().run_cell_magic('bash', '', 'mkdir -p continuous_int/.github/workflows\n')


# In[5]:


get_ipython().run_cell_magic('writefile', 'continuous_int/.github/workflows/ci-tests.yml', '# This workflow will install Python dependencies, run tests with a variety of Python versions, on Windows and Linux\n# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions\n\nname: Unit tests\n\non:\n  pull_request:\n    branches:\n      - main\n  push:\n\njobs:\n  build:\n    strategy:\n      # We use `fail-fast: false` for teaching purposess. This ensure that all combinations of the matrix\n      # will run even if one or more fail. \n      fail-fast: false\n      matrix:\n        python-version: [3.8, 3.9, "3.10"]\n        os: [ubuntu-latest, windows-latest]\n    \n    runs-on: ${{ matrix.os }}\n\n    steps:\n    - uses: actions/checkout@v2\n    - name: Set up Python ${{ matrix.python-version }}\n      uses: actions/setup-python@v1\n      with:\n        python-version: ${{ matrix.python-version }}\n    \n    # Yes we have to explictly install pytest. In a "real" example this could be included in a \n    # requirement.txt or environment.yml to setup your environment\n    - name: Install PyTest\n      run: |\n        python -m pip install pytest\n    # Now run the tests\n    - name: Test with pytest\n      run: |\n        pytest\n')


# ## Apply this to the personal github repo you made in module 04"
# 
# * Create a new branch in your repo.
# * Copy the files in the `continuous_int` directory into your local clone . Note that the `.yml` file must exist in the directory `.github/workflows`, which must be in the root of your repo. (The `.` prefixed to teh `.github`
# * Commit your changes and push them
# * Create a Pull Request to the `main` branch of your own repo.
# 

# When succesfully applied to your repo, you should see that a number of tests are completed on every commit pushed, on every pull request.
# 
# These tests have been designed that they will both pass only if they are run on Windows and on Python v3.9 or higher, in order to demostrate the matrix workings of GH Actions. In a more more realistic senario, you should aim to have your test pass in all contexts.
# 
# ## Futher reading:
# 
# * There can be cases where is it propriate to expect different behaviour on different platforms. [PyTest](https://docs.pytest.org/en/6.2.x/skipping.html) has features that allow for cases.
# * GitHub Actions themselves can be difficult to debug because of the need to commit and push every minor change. "[Act](https://github.com/nektos/act)" provides a tool to help debug some GH Actions locally.
# 
# 
