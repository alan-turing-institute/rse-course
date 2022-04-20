#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python

# ## Introduction

# ### Why teach Python?

# 
# * In this first session, we will introduce [Python](http://www.python.org).
# * This course is about programming for data analysis and visualisation in research.
# * It's not mainly about Python.
# * But we have to use some language.
# 

# ### Why Python?

# 
# * Python is quick to program in
# * Python is popular in research, and has lots of libraries for science
# * Python interfaces well with faster languages
# * Python is free, so you'll never have a problem getting hold of it, wherever you go.
# 

# ### Why write programs for research?

# 
# * Not just labour saving
# * Scripted research can be tested and reproduced
# 

# ### Sensible Input  - Reasonable Output

# Programs are a rigorous way of describing data analysis for other researchers, as well as for computers.
# 
# Computational research suffers from people assuming each other's data manipulation is correct. By sharing codes,
# which are much more easy for a non-author to understand than spreadsheets, we can avoid the "SIRO" problem. The old saw "Garbage in Garbage out" is not the real problem for science:
# 
# * Sensible input
# * Reasonable output
# 
# 

# ## Many kinds of Python

# ### The Jupyter Notebook

# The easiest way to get started using Python, and one of the best for research data work, is the Jupyter Notebook.

# In the notebook, you can easily mix code with discussion and commentary, and mix code with the results of that code;
# including graphs and other data visualisations.

# In[1]:


### Make plot
get_ipython().run_line_magic('matplotlib', 'inline')
import math

import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0, 4 * math.pi, 0.1)
eight = plt.figure()
axes = eight.add_axes([0, 0, 1, 1])
axes.plot(0.5 * np.sin(theta), np.cos(theta / 2))


# We're going to be mainly working in the Jupyter notebook in this course. To get hold of a copy of the notebook, follow the setup instructions shown on the course website, or use the installation in Desktop@UCL (available in the teaching cluster rooms or [anywhere](https://www.ucl.ac.uk/isd/services/computers/remote-access/desktopucl-anywhere)).

# Jupyter notebooks consist of discussion cells, referred to as "markdown cells", and "code cells", which contain Python. This document has been created using Jupyter notebook, and this very cell is a **Markdown Cell**. 

# In[2]:


print("This cell is a code cell")


# Code cell inputs are numbered, and show the output below.

# Markdown cells contain text which uses a simple format to achive pretty layout, 
# for example, to obtain:
# 
# **bold**, *italic*
# 
# * Bullet
# 
# > Quote
# 
# We write:
# 
#     **bold**, *italic*
# 
#     * Bullet
# 
#     > Quote
# 
# See the Markdown documentation at [This Hyperlink](http://daringfireball.net/projects/markdown/)

# ### Typing code in the notebook

# When working with the notebook, you can either be in a cell, typing its contents, or outside cells, moving around the notebook.
# 
# * When in a cell, press escape to leave it. When moving around outside cells, press return to enter.
# * Outside a cell:
#   * Use arrow keys to move around.
#   * Press `b` to add a new cell below the cursor.
#   * Press `m` to turn a cell from code mode to markdown mode.
#   * Press `shift`+`enter` to calculate the code in the block.
#   * Press `h` to see a list of useful keys in the notebook.
# * Inside a cell:
#   * Press `tab` to suggest completions of variables. (Try it!)

# *Supplementary material*: Learn more about [Jupyter notebooks](https://jupyter.org/).

# ### Python at the command line

# Data science experts tend to use a "command line environment" to work. You'll be able to learn this at our ["Software Carpentry" workshops](http://rits.github-pages.ucl.ac.uk/software-carpentry/), which cover other skills for computationally based research.

# In[3]:


get_ipython().run_cell_magic('bash', '', '# Above line tells Python to execute this cell as *shell code*\n# not Python, as if we were in a command line\n# This is called a \'cell magic\'\n\npython -c "print(2 * 4)"\n')


# ### Python scripts

# Once you get good at programming, you'll  want to be able to write your own full programs in Python, which work just
# like any other program on your computer. Here are some examples:

# In[4]:


get_ipython().run_cell_magic('bash', '', 'echo "print(2 * 4)" > eight.py\npython eight.py\n')


# We can make the script directly executable (on Linux or Mac) by inserting a [hashbang](https://en.wikipedia.org/wiki/Shebang_(Unix%29)) and [setting the permissions](http://v4.software-carpentry.org/shell/perm.html) to execute.

# In[5]:


get_ipython().run_cell_magic('writefile', 'fourteen.py', '#! /usr/bin/env python\nprint(2 * 7)\n')


# In[6]:


get_ipython().run_cell_magic('bash', '', 'chmod u+x fourteen.py\n./fourteen.py\n')


# ### Python Libraries

# We can write our own python libraries, called modules which we can import into the notebook and invoke:

# In[7]:


get_ipython().run_cell_magic('writefile', 'draw_eight.py', '# Above line tells the notebook to treat the rest of this\n# cell as content for a file on disk.\nimport math\nimport numpy as np\nimport matplotlib.pyplot as plt\n\n\ndef make_figure():\n    theta = np.arange(0, 4 * math.pi, 0.1)\n    eight = plt.figure()\n    axes = eight.add_axes([0, 0, 1, 1])\n    axes.plot(0.5 * np.sin(theta), np.cos(theta / 2))\n    return eight\n')


# In a real example, we could edit the file on disk
# using a program such as [Atom](https://atom.io) or [VS code](https://code.visualstudio.com/).

# In[8]:


import draw_eight  # Load the library file we just wrote to disk


# In[9]:


image = draw_eight.make_figure()


# There is a huge variety of available packages to do pretty much anything. For instance, try `import antigravity`.
# 
# The `%%` at the beginning of a cell is called *magics*. There's a [large list of them available](https://ipython.readthedocs.io/en/stable/interactive/magics.html) and you can [create your own](http://ipython.readthedocs.io/en/stable/config/custommagics.html).
# 
