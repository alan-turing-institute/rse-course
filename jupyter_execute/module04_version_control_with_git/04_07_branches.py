#!/usr/bin/env python
# coding: utf-8

# # Branches
# 
# Branches are incredibly important to why `git` is cool and powerful.
# 
# They are an easy and cheap way of making a second version of your software, which you work on in parallel,
# and pull in your changes when you are ready.

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(working_dir)


# In[2]:


get_ipython().run_cell_magic('bash', '', 'git branch # Tell me what branches exist')


# In[3]:


get_ipython().run_cell_magic('bash', '', 'git checkout -b experiment # Make a new branch')


# In[4]:


get_ipython().run_cell_magic('bash', '', 'git branch')


# In[5]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Glyder Fawr\n* Fan y Big\n* Cadair Idris')


# In[6]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add Cadair Idris"')


# In[7]:


get_ipython().run_cell_magic('bash', '', 'git checkout main # Switch to an existing branch')


# In[8]:


get_ipython().run_cell_magic('bash', '', 'cat Wales.md')


# In[9]:


get_ipython().run_cell_magic('bash', '', 'git checkout experiment')


# In[10]:


cat Wales.md


# ## Publishing branches
# 
# To let the server know there's a new branch use:

# In[11]:


get_ipython().run_cell_magic('bash', '', 'git push -u origin experiment')


# We use `--set-upstream origin` (Abbreviation `-u`) to tell git that this branch should be pushed to and pulled from origin per default.
# 
# If you are following along, you should be able to see your branch in the list of branches in GitHub.

# Once you've used `git push -u` once, you can push new changes to the branch with just a git push.

# If others checkout your repository, they will be able to do `git checkout experiment` to see your branch content,
# and collaborate with you **in the branch**.

# In[12]:


get_ipython().run_cell_magic('bash', '', 'git branch -r')


# Local branches can be, but do not have to be, connected to remote branches
# They are said to "track" remote branches. `push -u` sets up the tracking relationship.
# You can see the remote branch for each of your local branches if you ask for "verbose" output from `git branch`:

# In[13]:


get_ipython().run_cell_magic('bash', '', 'git branch -vv')


# ### Find out what is on a branch
# 
# In addition to using `git diff` to compare to the state of a branch,
# you can use `git log` to look at lists of commits which are in a branch
# and haven't been merged yet.

# In[14]:


get_ipython().run_cell_magic('bash', '', 'git log main..experiment')


# Git uses various symbols to refer to sets of commits.
# The double dot `A..B` means "ancestor of B and not ancestor of A"
# 
# So in a purely linear sequence, it does what you'd expect.

# In[15]:


get_ipython().run_cell_magic('bash', '', 'git log --graph --oneline HEAD~9..HEAD~5')


# But in cases where a history has branches,
# the definition in terms of ancestors is important.

# In[16]:


get_ipython().run_cell_magic('bash', '', 'git log --graph --oneline HEAD~5..HEAD')


# If there are changes on both sides, like this:

# In[17]:


get_ipython().run_cell_magic('bash', '', 'git checkout main')


# In[18]:


get_ipython().run_cell_magic('writefile', 'Scotland.md', 'Mountains In Scotland\n==================\n\n* Ben Eighe\n* Cairngorm\n* Aonach Eagach')


# In[19]:


get_ipython().run_cell_magic('bash', '', 'git diff Scotland.md')


# In[20]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Commit Aonach onto main branch"')


# Then this notation is useful to show the content of what's on what branch:

# In[21]:


get_ipython().run_cell_magic('bash', '', 'git log --left-right --oneline main...experiment')


# Three dots means "everything which is not a common ancestor" of the two commits, i.e. the differences between them.

# ## Merging branches

# We can merge branches, and just as we would pull in remote changes, there may or may not be conflicts.

# In[22]:


get_ipython().run_cell_magic('bash', '', 'git branch\ngit merge experiment')


# In[23]:


get_ipython().run_cell_magic('bash', '', 'git log --graph --oneline HEAD~3..HEAD')


# ## Cleaning up after a branch

# In[24]:


get_ipython().run_cell_magic('bash', '', 'git branch  # list branches')


# In[25]:


get_ipython().run_cell_magic('bash', '', 'git branch -d experiment  # delete a branch')


# In[26]:


get_ipython().run_cell_magic('bash', '', 'git branch # current branch')


# In[27]:


get_ipython().run_cell_magic('bash', '', 'git branch --remote  # list remote branches')


# In[28]:


get_ipython().run_cell_magic('bash', '', 'git push --delete origin experiment \n# Remove remote branch. Note that you can also use the GitHub interface to do this.')


# In[29]:


get_ipython().run_cell_magic('bash', '', 'git branch --remote  # list remote branches')


# In[30]:


get_ipython().run_cell_magic('bash', '', 'git push\ngit branch -vv # current local branch and tracking')


# ## A good branch strategy
# 
# * A `production` or `main` branch: the current working version of your code
# * A `develop` branch: where new code can be tested
# * `feature` branches: for specific new ideas
# * `release` branches: when you share code with others
#   * Useful for applying bug fixes to older versions of your code

# ## Grab changes from a branch
# 
# Make some changes on one branch, switch back to another, and use:

# ```bash
# git checkout <branch> <path>
# ```

# to quickly grab a file from one branch into another. This will create a copy of the file as it exists in `<branch>` into your current branch, overwriting it if it already existed.
# For example, if you have been experimenting in a new branch but want to undo all your changes to a particular file (that is, restore the file to its version in the `main` branch), you can do that with:
# 
# ```
# git checkout main test_file
# ```
# 
# Using `git checkout` with a path takes the content of files.
# To grab the content of a specific *commit* from another branch,
# and apply it as a patch to your branch, use:

# ``` bash
# git cherry-pick <commit>
# ```
