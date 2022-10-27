#!/usr/bin/env python
# coding: utf-8

# # 4.0 Introduction to version control

# *Estimated time to complete this notebook: 10 minutes*

# ## What's version control?
# 
# Version control is a tool for __managing changes__ to a set of files.
# 
# There are many different __version control systems__:
# 
# - Git
# - Mercurial (`hg`)
# - CVS
# - Subversion (`svn`)
# - ...

# ## Why use version control?
# 
# - Better kind of __backup__.
# - Review __history__ ("When did I introduce this bug?").
# - Restore older __code versions__.
# - Ability to __undo mistakes__.
# - Maintain __several versions__ of the code at a time.

# Git is also a __collaborative__ tool:
# 
# - "How can I share my code?"
# - "How can I submit a change to someone else's code?"
# - "How can I merge my work with Sue's?"

# ## Git != GitHub
# 
# - __Git__: version control system tool to manage source code history.
# - __GitHub__: hosting service for Git repositories.

# ## How do we use version control?
# 
# Do some programming, then commit our work:
# 
# `my_vcs commit`
# 
# Program some more.
# 
# Spot a mistake:
# 
# `my_vcs rollback`
# 
# Mistake is undone.

# ## What is version control? (Team version)
# 
# Sue                | James
# ------------------ |------
# `my_vcs commit`    | ...
# ...                | Join the team
# ...                | `my_vcs checkout`
# ...                | Do some programming
# ...                | `my_vcs commit`
# `my_vcs update`    | ...
# Do some programming|Do some programming
# `my_vcs commit`    | ...
# `my_vcs update`    | ...
# `my_vcs merge`     | ...
# `my_vcs commit`    | ...

# ## Scope
# 
# This course will use the `git` version control system, but much of what you learn will be valid with other version control tools you may encounter, including subversion (`svn`) and mercurial (`hg`).

# # 4.0.1 Practising with Git

# ## Example Exercise
# 
# In this course, we will use, as an example, the development of a few text files containing a description of a topic of your choice.
# 
# This could be your research, a hobby, or something else. In the end, we will show you how to display the content of these files as a very simple website. 

# ## Programming and documents
# 
# The purpose of this exercise is to learn how to use Git to manage program code you write, not simple text website content, but we'll just use these text files instead of code for now, so as not to confuse matters with trying to learn version control while thinking about programming too.
# 
# In later parts of the course, you will use the version control tools you learn today with actual Python code.

# ## Markdown
# 
# The text files we create will use a simple "wiki" markup style called [markdown](http://daringfireball.net/projects/markdown/basics) to show formatting.
# This is the convention used in this file, too.
# 
# You can view the content of this file in the way Markdown renders it by looking on the [web](https://github.com/alan-turing-institute/rse-course/blob/main/module04_version_control_with_git/04_00_introduction.html), and compare the [raw text](https://raw.githubusercontent.com/alan-turing-institute/rse-course/main/module04_version_control_with_git/04_00_introduction.ipynb).

# ## Displaying Text in this Tutorial
# 
# This tutorial is based on use of the Git command line. So you'll be typing commands in the shell.

# To make it easy for me to edit, I've built it using Jupyter notebook.

# Commands you can type will look like this, using the %%bash "magic" for the notebook.
# 
# If you are running the notebook on windows you'll have to use %%cmd.

# In[1]:


get_ipython().run_cell_magic('bash', '', 'echo some output\n')


# with the results you should see below. 

# In this document, we will show the new content of an edited document like this:

# In[2]:


get_ipython().run_cell_magic('writefile', 'somefile.md', 'Some content here\n')


# But if you are following along, you should edit the file using a text editor.
# On windows, we recommend [Notepad++](https://notepad-plus-plus.org).
# On mac, we recommend [Atom](https://atom.io)

# ## Setting up somewhere to work

# In[3]:


get_ipython().run_cell_magic('bash', '', "rm -rf learning_git/git_example # Just in case it's left over from a previous class; you won't need this\nmkdir -p learning_git/git_example\ncd learning_git/git_example\n")


# I just need to move this Jupyter notebook's current directory as well:

# In[4]:


import os

top_dir = os.getcwd()
top_dir


# In[5]:


git_dir = os.path.join(top_dir, "learning_git")
git_dir


# In[6]:


working_dir = os.path.join(git_dir, "git_example")


# In[7]:


os.chdir(working_dir)


# # 4.0.2 Solo work
# 
# ## Configuring Git with your name and email
# 
# First, we should configure Git to know our name and email address:
# 
# ```bash
# git config --global user.name "YOUR NAME HERE"
# git config --global user.email "yourname@example.com"
# ```
# 
# Note that by using the `--global` flag, we are setting these options for all projects. To set them just for this project, use `--local` instead.

# Now check that this worked

# In[8]:


get_ipython().run_cell_magic('bash', '', 'git config --get user.name\n')


# In[9]:


get_ipython().run_cell_magic('bash', '', 'git config --get user.email\n')


# ## Initialising the repository
# 
# Now, we will tell Git to track the content of this folder as a git "repository".

# In[10]:


get_ipython().run_cell_magic('bash', '', 'pwd # Note where we are standing-- MAKE SURE YOU INITIALISE THE RIGHT FOLDER\ngit init --initial-branch=main\n')


# As yet, this repository contains no files:

# In[11]:


get_ipython().run_cell_magic('bash', '', 'ls\n')


# In[12]:


get_ipython().run_cell_magic('bash', '', 'git status\n')

