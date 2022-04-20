#!/usr/bin/env python
# coding: utf-8

# # Construction

# ## Construction

# 
# Software *design* gets a lot of press (Object orientation, UML, design patterns).
# 
# In this session we're going to look at advice on software *construction*.
# 

# ### Construction vs Design

# 
# For a given piece of code, there exist several different ways one could write it:
# 
# * Choice of variable names
# * Choice of comments
# * Choice of layout
# 
# The consideration of these questions is the area of Software Construction.
# 

# ### Low-level design decisions

# 
# We will also look at some of the lower-level software design decisions in the context of this section:
# 
# * Division of code into subroutines
# * Subroutine access signatures
# * Choice of data structures for readability
# 

# ### Algorithms and structures

# 
# We will not, in discussing construction, be looking at decisions as to how design questions impact performance:
# 
# * Choice of algorithms
# * Choice of data structures for performance
# * Choice of memory layout
# 
# We will consider these in a future discussion of performance programming.
# 

# ### Architectural design

# 
# We will not, in this session, be looking at the large-scale questions of how program components interact,
# the stategic choices that govern how software behaves at the large scale:
# 
# * Where do objects get made?
# * Which objects own or access other objects?
# * How can I hide complexity in one part of the code from other parts of the code?
# 
# We will consider these in a future session.
# 

# ### Construction

# 
# So, we've excluded most of the exciting topics. What's left is the bricks and mortar of software:
# how letters and symbols are used to build code which is readable.
# 

# ### Literate programming

# 
# In literature, books are enjoyable for different reasons:
# 
# * The beauty of stories
# * The beauty of plots
# * The beauty of characters
# * The beauty of paragraphs
# * The beauty of sentences
# * The beauty of words
# 
# Software has beauty at these levels too: stories and characters correspond to architecture and object design,
# plots corresponds to algorithms, but the rhythm of sentences and the choice of words corresponds
# to software construction.
# 

# ### Programming for humans

# 
# * Remember you're programming for humans as well as computers
# * A program is the best, most rigorous way to describe an algorithm
# * Code should be pleasant to read, a form of scholarly communication
# 
# Read Steve McConnell's [Code Complete](https://en.wikipedia.org/wiki/Code_Complete) [[UCL library](https://ucl-new-primo.hosted.exlibrisgroup.com/primo-explore/fulldisplay?docid=UCL_LMS_DS21156385750004761&context=L)].
# 
# 
# 
# 
# 

# ### Setup

# This notebook is based on a number of fragments of code, with an implicit context.
# We've made a library to set up the context so the examples work.

# In[1]:


get_ipython().run_cell_magic('writefile', 'context.py', 'from unittest.mock import Mock, MagicMock\n\n\nclass CompMock(Mock):\n    def __sub__(self, b):\n        return CompMock()\n\n    def __lt__(self, b):\n        return True\n\n    def __abs__(self):\n        return CompMock()\n\n\narray = []\nagt = []\nws = []\nagents = []\ncounter = 0\nx = MagicMock()\ny = None\nagent = MagicMock()\nvalue = 0\nbird_types = ["Starling", "Hawk"]\nimport numpy as np\n\naverage = np.mean\nhawk = CompMock()\nstarling = CompMock()\nsEntry = "2.0"\nentry = "2.0"\niOffset = 1\noffset = 1\nanothervariable = 1\nflag1 = True\nvariable = 1\nflag2 = False\n\n\ndef do_something():\n    pass\n\n\nchromosome = None\nstart_codon = None\nsubsequence = MagicMock()\ntranscribe = MagicMock()\nribe = MagicMock()\nfind = MagicMock()\ncan_see = MagicMock()\nmy_name = ""\nyour_name = ""\nflag1 = False\nflag2 = False\nstart = 0.0\nend = 1.0\nstep = 0.1\nbirds = [MagicMock()] * 2\nresolution = 100\npi = 3.141\nresult = [0] * resolution\nimport numpy as np\nimport math\n\ndata = [math.sin(y) for y in np.arange(0, pi, pi / resolution)]\nimport yaml\nimport os\n')

