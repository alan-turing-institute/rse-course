#!/usr/bin/env python
# coding: utf-8

# # 6.3 Python outside the notebook

# *Estimated time for this notebook: 15 minutes*

# We will often want to save our Python functions and classes, for use in multiple Notebooks or to interact with them via a terminal.

# ## Writing Python in Text Files

# If you create your own Python files ending in `.py`, then you can import them with `import` just like external libraries.
# 
# It's best to use an editor like [VS Code](https://code.visualstudio.com/) or [PyCharm](https://www.jetbrains.com/pycharm/) to do this. Here we use the `%%writefile` Jupyter "magic" to create files from the notebook.
# 
# Let's create a file `greeter.py` with a function `greet` that prints a welcome message in multiple colours (using the [`colorama`](https://pypi.org/project/colorama/) package):

# In[1]:


get_ipython().run_cell_magic('writefile', 'greeter.py', 'import colorama  # used for creating coloured text\n\n\ndef greet(personal, family, title="", polite=False):\n    greeting = "How do you do, " if polite else "Hey, "\n    greeting = colorama.Back.BLACK + colorama.Fore.YELLOW + greeting\n    if title:\n        greeting += colorama.Back.BLUE + colorama.Fore.WHITE + title + " "\n\n    greeting += (\n        colorama.Back.WHITE\n        + colorama.Style.BRIGHT\n        + colorama.Fore.RED\n        + personal\n        + " "\n        + family\n    )\n    return greeting\n')


# ## Loading Our Function
# 
# We just wrote the file, there is no `greet` function in this notebook yet:

# In[2]:


greet("James", "Hetherington")


# But we can import the functionality from `greeter.py` file that we created:

# In[3]:


import greeter  # note that you don't include the .py extension


print(greeter.greet("James", "Hetherington"))


# Or import the function from the file directly:

# In[4]:


from greeter import greet


print(greet("James", "Hetherington"))


# Note the file we created is in the same directory as this notebook:

# In[5]:


# glob is a library for finding files that match given patterns
from glob import glob

# all files with a .py or .ipynb extension in the current directory
glob("*.py") + glob("*.ipynb")


# Currently we're relying on all the module source code being in our current working directory. We'll want to `import` our modules from notebooks elsewhere on our computer: it would be a bad idea to keep all our Python work in one folder.
# 
# The best way to do this is to learn how to make our code into a proper module that we can install. We'll see more on that in the next notebook.

# ## Command-line Interfaces

# [argparse](https://docs.python.org/3/library/argparse.html) is the standard Python library for building programs with a command-line interface (another popular library is [click](https://click.palletsprojects.com/en/8.1.x/)).
# 
# Here's an example that creates a command-line interface to our `greet` function (in a file named `command.py`):

# In[6]:


get_ipython().run_cell_magic('writefile', 'command.py', 'from argparse import ArgumentParser\n\nfrom greeter import greet\n\n\ndef process():\n    parser = ArgumentParser(description="Generate appropriate greetings")\n\n    # required (positional) arguments\n    parser.add_argument("personal")\n    parser.add_argument("family")\n\n    # optional (keyword) arguments\n    parser.add_argument("--title", "-t")\n    parser.add_argument("--polite", "-p", action="store_true")\n    #   polite will be false unless "--polite" or "-p" given at command-line\n\n    args = parser.parse_args()\n\n    print(greet(args.personal, args.family, args.title, args.polite))\n\n\nif __name__ == "__main__":\n    process()\n')


# We can now run our saved interface with `python command.py` + the arguments we want to specify.
# 
# `argparse` generates some documentation to help us understand how to use it:

# In[7]:


get_ipython().run_cell_magic('bash', '', 'python command.py --help\n')


# A few examples:

# In[8]:


get_ipython().run_cell_magic('bash', '', 'python command.py James Hetherington\n')


# In[9]:


get_ipython().run_cell_magic('bash', '', 'python command.py --polite James Hetherington\n')


# In[10]:


get_ipython().run_cell_magic('bash', '', 'python command.py James Hetherington --title Dr\n')


# Having to type `python command.py ...` is not very intuitive, and we're still relying on our files being in the same directory. In the next notebook we'll see a better way to include command-line interfaces as part of a package.

# ## `if __name__ == "__main__"`
# 
# In the `command.py` script above you may have noticed the strange `if __name__ == "__main__"` line. This is generally used when you have a file that can be used both as a script and as a module in a package.
# 
# Let's create a simplified version of `greeter.py` that prints the name of the special `__name__` variable when it is called:

# In[11]:


get_ipython().run_cell_magic('writefile', 'greeter.py', 'print("executing greeter.py, __name__ is", __name__)\n\n\ndef greet(personal, family):\n    return "Hey, " + personal + " " + family\n\n\nif __name__ == "__main__":\n    print(greet("Laura", "Greeter"))\n')


# If we invoke `greeter.py` directly, Python sets the value of `__name__` to `"__main__"` and the code in the if block runs:

# In[12]:


get_ipython().run_cell_magic('bash', '', 'python greeter.py\n')


# Now let's create a simplified `command.py` that also prints `__name__`, and imports the `greet` function from `greeter.py` as before:

# In[13]:


get_ipython().run_cell_magic('writefile', 'command.py', 'print("executing command.py, __name__ is", __name__)\n\nfrom argparse import ArgumentParser\nfrom greeter import greet\n\n\ndef process():\n    parser = ArgumentParser(description="Generate appropriate greetings")\n    parser.add_argument("personal")\n    parser.add_argument("family")\n    args = parser.parse_args()\n    print(greet(args.personal, args.family))\n\n\nif __name__ == "__main__":\n    process()\n')


# And run the command script:

# In[14]:


get_ipython().run_cell_magic('bash', '', 'python command.py Sarah Command\n')


# Note that when we import `greeter.greet` the contents of the whole `greeter.py` file are executed, so the code to print the value of `__name__` still runs. However, `__name__` is now given the value `greeter`. This means when the if statement is executed `__name__ == "__main__"` returns `False`, and we don't see the "Hey, Laura Greeter" output. 
# 
# Without that if statement we would get
# 
# ```bash
# Hey, Laura Greeter
# Hey, Sarah Command
# ```
# 
# which is unlikely to be what we wanted when running `python command.py Sarah Command`.

# In[ ]:




