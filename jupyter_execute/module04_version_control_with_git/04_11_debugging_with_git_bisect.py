#!/usr/bin/env python
# coding: utf-8

# # 4.11 Debugging With git bisect
# 

# *Estimated time to complete this notebook: 5 minutes*

# You can use
# 
# ``` bash
# git bisect
# ```
# 
# to find out which commit caused a bug.

# ## An example repository
# 
# In a nice open source example, I found an arbitrary exemplar on github

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
os.chdir(git_dir)


# In[2]:


get_ipython().run_cell_magic('bash', '', 'rm -rf bisectdemo\ngit clone https://github.com/shawnsi/bisectdemo.git\n')


# In[3]:


bisect_dir = os.path.join(git_dir, "bisectdemo")
os.chdir(bisect_dir)


# In[4]:


get_ipython().run_cell_magic('bash', '', 'python squares.py 2 # 4\n')


# This has been set up to break itself at a random commit, and leave you to use
# bisect to work out where it has broken:

# In[5]:


get_ipython().run_cell_magic('bash', '', './breakme.sh > break_output\n')


# Which will make a bunch of commits, of which one is broken, and leave you in the broken final state

# In[6]:


python squares.py 2 # Error message


# ## Bisecting manually

# In[7]:


get_ipython().run_cell_magic('bash', '', 'git bisect start\ngit bisect bad # We know the current state is broken\ngit checkout master\ngit bisect good # We know the master branch state is OK\n')


# Bisect needs one known good and one known bad commit to get started

# ## Solving Manually

# ``` bash
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # Crash
# git bisect bad
# python squares.py 2 # Crash
# git bisect bad
# python squares.py 2 # Crash
# git bisect bad
# python squares.py 2 #Crash
# git bisect bad
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# python squares.py 2 # 4
# git bisect good
# ```
# 

# And eventually:

# ``` bash
# git bisect good
#     Bisecting: 0 revisions left to test after this (roughly 0 steps)
# 
# python squares.py 2
#     4
# 
# git bisect good
# 2777975a2334c2396ccb9faf98ab149824ec465b is the first bad commit
# commit 2777975a2334c2396ccb9faf98ab149824ec465b
# Author: Shawn Siefkas <shawn.siefkas@meredith.com>
# Date:   Thu Nov 14 09:23:55 2013 -0600
# 
#     Breaking argument type
# 
# ```

# ``` bash
# git bisect end
# ```

# ## Solving automatically
# 
# If we have an appropriate unit test, we can do all this automatically:

# In[8]:


get_ipython().run_cell_magic('bash', '', 'git bisect start\ngit bisect bad HEAD # We know the current state is broken\ngit bisect good master #\xa0We know master is good\ngit bisect run python squares.py 2\n')


# Boom!
