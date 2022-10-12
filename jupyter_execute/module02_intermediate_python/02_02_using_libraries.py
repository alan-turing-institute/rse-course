#!/usr/bin/env python
# coding: utf-8

# # 2.2 Using Libraries

# *Estimated time for this notebook: 5 minutes*

# ## 2.2.1 Import

# To use a function or type from a python library, rather than a **built-in** function or type, we have to import the library.

# In[1]:


math.sin(1.6)


# In[2]:


import math


# In[3]:


math.sin(1.6)


# We call these libraries **modules**:

# In[4]:


type(math)


# The tools supplied by a module are *attributes* of the module, and as such, are accessed with a dot.

# In[5]:


dir(math)


# They include properties as well as functions:

# In[6]:


math.pi


# You can always find out where on your storage medium a library has been imported from:

# In[7]:


print(math.__file__[0:50])
print(math.__file__[50:])


# Note that `import` does *not* install libraries. It just makes them available to your current notebook session, assuming they are already installed. Installing libraries is harder, and we'll cover it later.
# So what libraries are available? Until you install more, you might have just the modules that come with Python, the *standard library*.

# **Supplementary Materials**: Review the list of standard library modules: https://docs.python.org/library/

# If you installed via Anaconda, then you also have access to a bunch of modules that are commonly used in research.
# 
# **Supplementary Materials**: Review the list of modules that are packaged with Anaconda by default on different architectures: https://docs.anaconda.com/anaconda/packages/pkg-docs/ (modules installed by default are shown with ticks)
# 
# We'll see later how to add more libraries to our setup.

# ### Why bother?

# Why bother with modules? Why not just have everything available all the time?
# 
# The answer is that there are only so many names available! Without a module system, every time I made a variable whose name matched a function in a library, I'd lose access to it. In the olden days, people ended up having to make really long variable names, thinking their names would be unique, and they still ended up with "name clashes". The module mechanism avoids this.

# ## 2.2.2 Importing from modules

# Still, it can be annoying to have to write `math.sin(math.pi)` instead of `sin(pi)`.
# Things can be imported *from* modules to become part of the current module:

# In[8]:


import math

math.sin(math.pi)


# In[9]:


from math import sin

sin(math.pi)


# Importing one-by-one like this is a nice compromise between typing and risk of name clashes.

# It *is* possible to import **everything** from a module, but you risk name clashes.

# In[10]:


from math import *

sin(pi)


# ###  Import and rename

# You can rename things as you import them to avoid clashes or for typing convenience

# In[11]:


import math as m

m.cos(0)


# In[12]:


pi = 3
from math import pi as realpi

print(sin(pi), sin(realpi))

