#!/usr/bin/env python
# coding: utf-8

# # Git Theory
# 
# ## The revision Graph
# 
# Revisions form a **GRAPH**

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(working_dir)


# In[2]:


get_ipython().run_cell_magic('bash', '', 'git log --graph --oneline')


# ## Git concepts
# 
# * Each revision has a parent that it is based on
# * These revisions form a graph
# * Each revision has a unique hash code
#   * In Sue's copy, revision 43 is ab3578d6
#   * Jim might think that is revision 38, but it's still ab3579d6
# * Branches, tags, and HEAD are *labels* pointing at revisions
# * Some operations (like fast forward merges) just move labels.

# ## The levels of Git

# There are four **Separate** levels a change can reach in git:

# * The Working Copy
# * The **index** (aka **staging area**)
# * The local repository
# * The remote repository

# Understanding all the things `git reset` can do requires a good
# grasp of git theory.

# * `git reset <commit> <filename>` : Reset index and working version of that file to the version in a given commit
# * `git reset --soft <commit>`: Move local repository branch label to that commit, leave working dir and index unchanged
# * `git reset <commit>`: Move local repository and index to commit ("--mixed")
# * `git reset --hard <commit>`: Move local repostiory, index, and working directory copy to that state
