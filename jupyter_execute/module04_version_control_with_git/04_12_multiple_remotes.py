#!/usr/bin/env python
# coding: utf-8

# # 4.12 Working with multiple remotes
# 

# *Estimated time to complete this notebook: 10 minutes*

# ## Distributed versus centralised
# 
# Older version control systems (cvs, svn) were "centralised"; the history was kept only on a server,
# and all commits required an internet.
# 
# Centralised                    |  Distributed
# -------------------------------|--------------------------
# Server has history             |Every user has full history
# Your computer has one snapshot |  Many local branches
# To access history, need internet| History always available
# You commit to remote server     | Users synchronise histories
# cvs, subversion(svn)            | git, mercurial (hg), bazaar (bzr)

# With modern distributed systems, we can add a second remote. This might be a personal *fork* on github:

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(working_dir)


# In[2]:


get_ipython().run_cell_magic('bash', '', 'git checkout main\ngit remote add jack89roberts git@github.com:jack89roberts/github-example.git\ngit fetch jack89roberts\n')


# Check your remote branches:

# In[3]:


get_ipython().run_cell_magic('bash', '', 'git remote -v\n')


# and ensure that the newly-added remote is up-to-date

# In[4]:


get_ipython().run_cell_magic('bash', '', 'git fetch jack89roberts\n')


# In[5]:


get_ipython().run_cell_magic('writefile', 'Pennines.md', '\nMountains In the Pennines\n========================\n\n* Cross Fell\n* Whernside\n')


# In[6]:


get_ipython().run_cell_magic('bash', '', 'git add Pennines.md\ngit commit -am "Add Whernside"\n')


# We can specify which remote to push to by name:

# In[7]:


get_ipython().run_cell_magic('bash', '', 'git push -uf jack89roberts main || echo "Push failed"\n')


# ... but note that you need to have the correct permissions to do so.

# In[8]:


get_ipython().run_cell_magic('bash', '', 'git push -uf origin main\n')


# ## Referencing remotes
# 
# You can always refer to commits on a remote like this:

# In[9]:


get_ipython().run_cell_magic('bash', '', 'git fetch\ngit log --oneline --left-right jack89roberts/main...origin/main\n')


# To see the differences between remotes, for example.
# 
# To see what files you have changed that aren't updated on a particular remote, for example:

# In[10]:


get_ipython().run_cell_magic('bash', '', 'git diff --name-only origin/main\n')


# When you reference remotes like this, you're working with a cached copy of the last time you interacted with the remote. You can do `git fetch` to update local data with the remotes without actually pulling. You can also get useful information about whether tracking branches are ahead or behind the remote branches they track:

# In[11]:


get_ipython().run_cell_magic('bash', '', 'git branch -vv\n')


# # Hosting Servers
# 
# ## Hosting a local server
# 
# * Any repository can be a remote for pulls
# * Can pull/push over shared folders or ssh
# * Pushing to someone's working copy is dangerous
# * Use `git init --bare` to make a copy for pushing
# * You don't need to create a "server" as such, any 'bare' git repo will do.

# In[12]:


bare_dir = os.path.join(git_dir, "bare_repo")
os.chdir(git_dir)


# In[13]:


get_ipython().run_cell_magic('bash', '', 'mkdir -p bare_repo\nrm -rf bare_repo/*\ncd bare_repo\ngit init --bare --initial-branch=main\n')


# In[14]:


os.chdir(working_dir)


# In[15]:


get_ipython().run_cell_magic('bash', '', 'git remote add local_bare ../bare_repo\ngit push -u local_bare main\n')


# Check your remote branches:

# In[16]:


get_ipython().run_cell_magic('bash', '', 'git remote -v\n')


# You can now work with this local repository, just as with any other git server.
# If you have a colleague on a shared file system, you can use this approach to collaborate through that file system.

# ## Home-made SSH servers
# 
# Classroom exercise: Try creating a server for yourself using a machine you can SSH to:

# ``` bash
# ssh <mymachine>
# mkdir mygitserver
# cd mygitserver
# git init --bare
# exit
# git remote add <somename> ssh://user@host/mygitserver
# git push -u <somename> master
# ```

# # SSH keys and GitHub
# 
# Classroom exercise: If you haven't already, you should set things up so that you don't have to keep typing in your
# password whenever you interact with GitHub via the command line.
# 
# You can do this with an "ssh keypair". You may have created a keypair in the
# Software Carpentry shell training. Go to the [ssh settings
# page](https://github.com/settings/ssh) on GitHub and upload your public key by
# copying the content from your computer. (Probably at .ssh/id_rsa.pub)
# 
# If you have difficulties, the instructions for this are [on the GitHub
# website](https://help.github.com/articles/generating-ssh-keys). 
