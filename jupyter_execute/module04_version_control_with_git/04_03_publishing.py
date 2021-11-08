#!/usr/bin/env python
# coding: utf-8

# # Publishing

# We're still in our working directory:

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(working_dir)
working_dir


# ## Sharing your work

# So far, all our work has been on our own computer. But a big part of the point of version control is keeping your work safe, on remote servers. Another part is making it easy to share your work with the world In this example, we'll be using the `GitHub` cloud repository to store and publish our work. 
# 
# If you have not done so already, you should create an account on `GitHub`: go to [https://github.com/](https://github.com/), fill in a username and password, and click on "sign up for free". 

# ## Creating a repository
# 
# Ok, let's create a repository to store our work. Hit "new repository" on the right of the github home screen, or click [here](https://github.com/new). 
# 
# Fill in a short name, and a description. Choose a "public" repository. Don't choose to add a Readme.

# ## Paying for GitHub
# 
# For this course, you should use public repositories in your personal account for your example work: it's good to share! GitHub is free for open source, but in general, charges a fee if you want to keep your work private. 
# 
# In the future, you might want to keep your work on GitHub private. 
# 
# Students can get free private repositories on GitHub, by going to [GitHub Education](https://github.com/edu) and filling in a form (look for the Student Developer Pack). 

# ## Adding a new remote to your repository
# 
# Instructions will appear, once you've created the repository, as to how to add this new "remote" server to your repository.
# In this example we are using pre-authorised `Deploy Keys` to connect using the `SSH` method.
# If you prefer to use username and password/token, these instructions will be slightly different:

# In[2]:


get_ipython().run_cell_magic('bash', '', 'git remote add origin git@github.com:alan-turing-institute/github-example.git')


# Note that the `https` version of this instruction would be something like `git remote add origin https://${YOUR_USERNAME}:${GITHUB_TOKEN}@github.com/alan-turing-institute/github-example.git`

# In[3]:


get_ipython().run_cell_magic('bash', '', 'git remote -v')


# In[4]:


get_ipython().run_cell_magic('bash', '', "git push -uf origin main # Note we use the '-f' flag here to force an update")


# ## Remotes
# 
# The first command sets up the server as a new `remote`, called `origin`. 
# 
# Git, unlike some earlier version control systems is a "distributed" version control system, which means you can work with multiple remote servers. 
# 
# Usually, commands that work with remotes allow you to specify the remote to use, but assume the `origin` remote if you don't. 
# 
# Here, `git push` will push your whole history onto the server, and now you'll be able to see it on the internet! Refresh your web browser where the instructions were, and you'll see your repository!

# Let's add these commands to our diagram:

# In[5]:


message = """
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
Local Repository -> Working Directory : git checkout
Local Repository -> Staging Area : git reset
Local Repository -> Working Directory: git reset --hard
Local Repository -> Remote Repository : git push
"""
from wsd import wsd

get_ipython().run_line_magic('matplotlib', 'inline')
wsd(message)


# ## Playing with GitHub
# 
# Take a few moments to click around and work your way through the GitHub interface. Try clicking on 'test.md' to see the content of the file: notice how the markdown renders prettily.
# 
# Click on "commits" near the top of the screen, to see all the changes you've made. Click on the commit number next to the right of a change, to see what changes it includes: removals are shown in red, and additions in green.

# # Working with multiple files

# ## Some new content
# 
# So far, we've only worked with one file. Let's add another:

# ``` bash
# vim lakeland.md
# ```

# In[6]:


get_ipython().run_cell_magic('writefile', 'lakeland.md', 'Lakeland  \n========   \n  \nCumbria has some pretty hills, and lakes too.  ')


# In[7]:


cat lakeland.md


# ## Git will not by default commit your new file

# In[8]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Try to add Lakeland" || echo "Commit failed"')


# This failed, because we've not told git to track the new file yet.

# ## Tell git about the new file

# In[9]:


get_ipython().run_cell_magic('bash', '', 'git add lakeland.md\ngit commit -am "Add lakeland"')


# Ok, now we have added the change about Cumbria to the file. Let's publish it to the origin repository.

# In[10]:


get_ipython().run_cell_magic('bash', '', 'git push')


# Visit GitHub, and notice this change is on your repository on the server. We could have said `git push origin` to specify the remote to use, but origin is the default.

# # Changing two files at once

# What if we change both files?

# In[11]:


get_ipython().run_cell_magic('writefile', 'lakeland.md', 'Lakeland  \n========   \n  \nCumbria has some pretty hills, and lakes too\n\nMountains:\n* Helvellyn')


# In[12]:


get_ipython().run_cell_magic('writefile', 'test.md', 'Mountains and Lakes in the UK   \n===================   \nEngerland is not very mountainous.\nBut has some tall hills, and maybe a\nmountain or two depending on your definition.')


# In[13]:


get_ipython().run_cell_magic('bash', '', 'git status')


# These changes should really be separate commits. We can do this with careful use of git add, to **stage** first one commit, then the other.

# In[14]:


get_ipython().run_cell_magic('bash', '', 'git add test.md\ngit commit -m "Include lakes in the scope"')


# Because we "staged" only test.md, the changes to lakeland.md were not included in that commit.

# In[15]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add Helvellyn"')


# In[16]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline')


# In[17]:


get_ipython().run_cell_magic('bash', '', 'git push')


# In[18]:


message = """
participant "Jim's remote" as M
participant "Jim's repo" as R
participant "Jim's index" as I
participant Jim as J

note right of J: vim test.md
note right of J: vim lakeland.md

note right of J: git add test.md
J->I: Add *only* the changes to test.md to the staging area

note right of J: git commit -m "Include lakes"
I->R: Make a commit from currently staged changes: test.md only

note right of J: git commit -am "Add Helvellyn"
J->I: Stage *all remaining* changes, (lakeland.md)
I->R: Make a commit from currently staged changes

note right of J: git push
R->M: Transfer commits to Github
"""
wsd(message)

