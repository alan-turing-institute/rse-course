#!/usr/bin/env python
# coding: utf-8

# # Using a debugger
# 
# ## Stepping through the code
# 
# Debuggers are programs that can be used to test other programs. They allow programmers to suspend execution of the target program and inspect variables at that point.
# 
# * Mac - compiled languages:
#   [Xcode](https://developer.apple.com/library/ios/documentation/ToolsLanguages/Conceptual/Xcode_Overview/DebugYourApp/DebugYourApp.html)
# * Windows - compiled languages:
#   [Visual Studio](http://msdn.microsoft.com/en-us/library/bb483011.aspx)
# * Linux: [DDD](https://www.gnu.org/software/ddd/)
# * all platforms: [eclipse](http://www.eclipse.org), [gdb](http://www.sourceware.org/gdb/) (DDD and
#   eclipse are GUIs for gdb)
# * python: [spyder](http://pythonhosted.org/spyder/index.html),
# *          [pdb](https://docs.python.org/3.8/library/pdb.html)
# * R: [RStudio](http://www.rstudio.com/ide/docs/debugging/overview),
#   [debug](http://stat.ethz.ch/R-manual/R-devel/library/base/html/debug.html),
#   [browser](http://stat.ethz.ch/R-manual/R-devel/library/base/html/browser.html)

# **NB.** If you are using the Windows command prompt, you will have to replace all `%%bash` directives in this notebook with `%%cmd` 

# ## Using the python debugger

# Unfortunately this doesn't work nicely in the notebook. But from the command line, you can run a python program with:

# ``` bash
# python -m pdb my_program.py
# ```

# ## Basic navigation:
# 
# Basic command to navigate the code and the python debugger:
# 
# * `help`: prints the help
# * `help n`: prints help about command `n`
# * `n`(ext): executes one line of code. Executes and steps **over** functions.
# * `s`(tep): step into current function in line of code
# * `l`(ist): list program around current position
# * `w`(where): prints current stack (where we are in code)
# * `[enter]`: repeats last command
# * `anypythonvariable`: print the value of that variable
# 
# The python debugger is **a python shell**: it can print and compute values, and even change the values
# of the variables at that point in the program.
# 
# ## Breakpoints
# 
# Break points tell debugger where and when to stop
# We say
# * `b somefunctionname`  

# In[1]:


get_ipython().run_cell_magic('writefile', 'energy_example.py', 'from diffusion.model import energy\n\nprint(energy([5, 6, 7, 8, 0, 1]))')


# The debugger is, of course, most used interactively, but here I'm showing a prewritten debugger script:

# In[2]:


get_ipython().run_cell_magic('writefile', 'commands', 'restart        # restart session\nn\nb energy       # program will stop when entering energy\nc              # continue program until break point is reached\nprint(density) # We are now "inside" the energy function and can print any variable.')


# In[3]:


get_ipython().run_cell_magic('bash', '', 'python -m pdb energy_example.py < commands')


# Alternatively, break-points can be set on files: `b file.py:20` will stop on line 20 of `file.py`.

# ## Post-mortem
# 
# Debugging when something goes wrong:
# 
# 1. Have a crash somewhere in the code
# 1. run `python -m pdb file.py` or run the cell with `%pdb on`
# 
# The program should stop where the exception was raised
# 
# 1. use `w` and `l` for position in code and in call stack
# 1. use `up` and `down` to navigate up and down the call stack
# 1. inspect variables along the way to understand failure

# **Note** Running interactively like in the following example **does** work in the notebook. Try it out!

# ```
# %pdb on
# from diffusion.model import energy
# partial_derivative(energy, [5, 6, 7, 8, 0, 1], 5)
# ```
