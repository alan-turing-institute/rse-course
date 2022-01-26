#!/usr/bin/env python
# coding: utf-8

# # Fixing mistakes

# We're still in our git working directory:

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(working_dir)
working_dir


# ## Referring to changes with HEAD and ~
# 
# The commit we want to revert to is the one before the latest.
# 
# `HEAD` refers to the latest commit. That is, we want to go back to the change before the current `HEAD`. 
# 
# We could use the hash code (e.g. 73fbeaf) to reference this, but you can also refer to the commit before the `HEAD` as `HEAD~`, the one before that as `HEAD~~`, the one before that as `HEAD~3`.

# ## Reverting
#  
# Ok, so now we'd like to undo the nasty commit with the lie about Mount Fictional.

# In[2]:


get_ipython().run_cell_magic('bash', '', 'git revert HEAD~')


# An editor may pop up, with some default text which you can accept and save. 

# ## Conflicted reverts
# 
# You may, depending on the changes you've tried to make, get an error message here. 
# 
# If this happens, it is because git could not automagically decide how to combine the change you made after the change you want to revert, with the attempt to revert the change: this could happen, for example, if they both touch the same line. 
# 
# If that happens, you need to manually edit the file to fix the problem. Skip ahead to the section on resolving conflicts, or ask a demonstrator to help.

# ## Review of changes
# 
# The file should now contain the change to the title, but not the extra line with the lie. Note the log:

# In[3]:


get_ipython().run_cell_magic('bash', '', 'git log --date=short')


# ## Antipatch
# 
# Notice how the mistake has stayed in the history.
# 
# There is a new commit which undoes the change: this is colloquially called an "antipatch". 
# This is nice: you have a record of the full story, including the mistake and its correction.

# ## Rewriting history
# 
# It is possible, in git, to remove the most recent change altogether, "rewriting history". Let's make another bad change, and see how to do this.

# ## A new lie

# In[4]:


get_ipython().run_cell_magic('writefile', 'test.md', 'Mountains and Hills in the UK   \n===================   \nEngerland is not very mountainous.   \nBut has some tall hills, and maybe a\nmountain or two depending on your definition.')


# In[5]:


get_ipython().run_cell_magic('bash', '', 'cat test.md')


# In[6]:


get_ipython().run_cell_magic('bash', '', 'git diff')


# In[7]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add a silly spelling"')


# In[8]:


get_ipython().run_cell_magic('bash', '', 'git log --date=short')


# ## Using reset to rewrite history

# In[9]:


get_ipython().run_cell_magic('bash', '', 'git reset HEAD~')


# In[10]:


get_ipython().run_cell_magic('bash', '', 'git log --date=short')


# ## Covering your tracks
# 
# The silly spelling *is no longer in the log*. This approach to fixing mistakes, "rewriting history" with `reset`, instead of adding an antipatch with `revert`, is dangerous, and we don't recommend it. But you may want to do it for small silly mistakes, such as to correct a commit message.

# ## Resetting the working area
# 
# When `git reset` removes commits, it leaves your working directory unchanged -- so you can keep the work in the bad change if you want. 

# In[11]:


get_ipython().run_cell_magic('bash', '', 'cat test.md')


# If you want to lose the change from the working directory as well, you can do `git reset --hard`. 
# 
# I'm going to get rid of the silly spelling, and I didn't do `--hard`, so I'll reset the file from the working directory to be the same as in the index:

# In[12]:


get_ipython().run_cell_magic('bash', '', 'git checkout test.md')


# In[13]:


get_ipython().run_cell_magic('bash', '', 'cat test.md')


# We can add this to our diagram:

# In[14]:


message = """
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
Local Repository -> Working Directory : git checkout
Local Repository -> Staging Area : git reset
Local Repository -> Working Directory: git reset --hard
"""
from wsd import wsd

get_ipython().run_line_magic('matplotlib', 'inline')
wsd(message)


# We can add it to Jim's story:

# In[15]:


message = """
participant "Jim's repo" as R
participant "Jim's index" as I
participant Jim as J

note right of J: git revert HEAD~

J->R: Add new commit reversing change
R->I: update staging area to reverted version
I->J: update file to reverted version



note right of J: vim test.md
note right of J: git commit -am "Add another mistake"
J->I: Add mistake
I->R: Add mistake

note right of J: git reset HEAD~

J->R: Delete mistaken commit
R->I: Update staging area to reset commit

note right of J: git checkout test.md

I->J: Update file to reverted version


"""
wsd(message)

