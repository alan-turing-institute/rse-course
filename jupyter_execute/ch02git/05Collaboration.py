#!/usr/bin/env python
# coding: utf-8

# # Collaboration
# 
# ## Form a team

# Now we're going to get to the most important question of all with Git and GitHub: working with others.
# 
# Organise into pairs. You're going to be working on the website of one of the two of you, together, so decide who is going to be the leader, and who the collaborator.

# ## Giving permission
# 
# The leader needs to let the collaborator have the right to make changes to his code.
# 
# In GitHub, go to `Settings` on the right, then `Collaborators & teams` on the left.
# 
# Add the user name of your collaborator to the box. They now have the right to push to your repository.

# ## Obtaining a colleague's code
# 
# Next, the collaborator needs to get a copy of the leader's code. For this example notebook,
# I'm going to be collaborating with myself, swapping between my two repositories.
# Make yourself a space to put it your work. (I will have two)

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(git_dir)


# In[2]:


get_ipython().run_cell_magic('bash', '', 'pwd\nrm -rf github-example # cleanup after previous example\nrm -rf partner_dir # cleanup after previous example')


# Next, the collaborator needs to find out the URL of the repository: they should go to the leader's repository's GitHub page, and note the URL on the top of the screen. Make sure the "ssh" button is pushed, the URL should begin with `git@github.com`. 
# 
# Copy the URL into your clipboard by clicking on the icon to the right of the URL, and then:

# In[3]:


get_ipython().run_cell_magic('bash', '', 'pwd\ngit clone https://${GITHUB_TOKEN}@github.com/alan-turing-institute/github-example.git partner_dir')


# In[4]:


partner_dir = os.path.join(git_dir, "partner_dir")
os.chdir(partner_dir)


# In[5]:


get_ipython().run_cell_magic('bash', '', 'pwd\nls')


# Note that your partner's files are now present on your disk:

# In[6]:


get_ipython().run_cell_magic('bash', '', 'cat lakeland.md')


# ## Nonconflicting changes
# 
# Now, both of you should make some changes. To start with, make changes to *different* files. This will mean your work doesn't "conflict". Later, we'll see how to deal with changes to a shared file.

# Both of you should commit, but not push, your changes to your respective files:

# E.g., the leader:

# In[7]:


os.chdir(working_dir)


# In[8]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Tryfan\n* Yr Wyddfa')


# In[9]:


get_ipython().run_cell_magic('bash', '', 'ls')


# In[10]:


get_ipython().run_cell_magic('bash', '', 'git add Wales.md\ngit commit -m "Add wales"')


# And the partner:

# In[11]:


os.chdir(partner_dir)


# In[12]:


get_ipython().run_cell_magic('writefile', 'Scotland.md', 'Mountains In Scotland\n==================\n\n* Ben Eighe\n* Cairngorm')


# In[13]:


get_ipython().run_cell_magic('bash', '', 'ls')


# In[14]:


get_ipython().run_cell_magic('bash', '', 'git add Scotland.md\ngit commit -m "Add Scotland"')


# One of you should now push with `git push`:

# In[15]:


get_ipython().run_cell_magic('bash', '', 'git push')


# ## Rejected push

# The other should then attempt to push, but should receive an error message:

# In[17]:


os.chdir(working_dir)


# ``` Bash
# > git push
# To https://github.com/alan-turing-institute/github-example.git
#  ! [rejected]        master -> master (fetch first)
# error: failed to push some refs
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref. You may want to first integrate the remote changes
# hint: (e.g., 'git pull ...') before pushing again.
# hint: See the 'Note about fast-forwards' in 'git push --help' for details.
# ```

# Do as it suggests:

# In[18]:


get_ipython().run_cell_magic('bash', '', 'git pull')


# ## Merge commits
# 
# A window may pop up with a suggested default commit message. This commit is special: it is a *merge* commit. It is a commit which combines your collaborator's work with your own.

# Now, push again with `git push`. This time it works. If you look on GitHub, you'll now see that it contains both sets of changes.

# In[19]:


get_ipython().run_cell_magic('bash', '', 'git push')


# The partner now needs to pull down that commit:

# In[20]:


os.chdir(partner_dir)


# In[21]:


get_ipython().run_cell_magic('bash', '', 'git pull')


# In[22]:


get_ipython().run_cell_magic('bash', '', 'ls')


# ## Nonconflicted commits to the same file
# 
# Go through the whole process again, but this time, both of you should make changes to a single file, but make sure that you don't touch the same *line*. Again, the merge should work as before:

# In[23]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Tryfan\n* Snowdon')


# In[24]:


get_ipython().run_cell_magic('bash', '', 'git diff')


# In[25]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Translating from the Welsh"')


# In[26]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline')


# In[27]:


os.chdir(working_dir)


# In[28]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Yr Wyddfa')


# In[29]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add a beacon"')


# In[30]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline')


# In[31]:


get_ipython().run_cell_magic('bash', '', 'git push')


# Switching back to the other partner...

# In[32]:


os.chdir(partner_dir)


# ``` bash
# > git push
# To https://github.com/alan-turing-institute/github-example.git
#  ! [rejected]        master -> master (fetch first)
# error: failed to push some refs
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref. You may want to first integrate the remote changes
# hint: (e.g., 'git pull ...') before pushing again.
# hint: See the 'Note about fast-forwards' in 'git push --help' for details.
# ```

# In[33]:


get_ipython().run_cell_magic('bash', '', 'git pull')


# In[34]:


get_ipython().run_cell_magic('bash', '', 'git push')


# In[35]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline --graph')


# In[36]:


os.chdir(working_dir)


# In[37]:


get_ipython().run_cell_magic('bash', '', 'git pull')


# In[38]:


get_ipython().run_cell_magic('bash', '', 'git log --graph --oneline')


# In[39]:


message = """
participant Sue as S
participant "Sue's repo" as SR
participant "Shared remote" as M
participant "Jim's repo" as JR
participant Jim as J

note left of S: git clone
M->SR: fetch commits
SR->S: working directory as at latest commit

note left of S: edit Scotland.md
note right of J: edit Wales.md

note left of S: git commit -am "Add scotland"
S->SR: create commit with Scotland file

note right of J: git commit -am "Add wales"
J->JR: create commit with Wales file

note left of S: git push
SR->M: update remote with changes

note right of J: git push
JR-->M: !Rejected change

note right of J: git pull
M->JR: Pull in Sue's last commit, merge histories
JR->J: Add Scotland.md to working directory

note right of J: git push
JR->M: Transfer merged history to remote

"""
from wsd import wsd

get_ipython().run_line_magic('matplotlib', 'inline')
wsd(message)


# ## Conflicting commits
# 
# Finally, go through the process again, but this time, make changes which touch the same line.

# In[40]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Fan y Big')


# In[41]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add another Beacon"\ngit push')


# In[42]:


os.chdir(partner_dir)


# In[43]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Glyder Fawr')


# In[44]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add Glyder"')


# ``` bash
# > git push
# To git@github.com:alan-turing-institute/github-example.git
#  ! [rejected]        master -> master (fetch first)
# error: failed to push some refs
# hint: Updates were rejected because the remote contains work that you do
# hint: not have locally. This is usually caused by another repository pushing
# hint: to the same ref. You may want to first integrate the remote changes
# hint: (e.g., 'git pull ...') before pushing again.
# hint: See the 'Note about fast-forwards' in 'git push --help' for details.
# ```

# When you pull, instead of offering an automatic merge commit message, it says:

# In[51]:


get_ipython().run_cell_magic('bash', '', 'git pull')


# ## Resolving conflicts
# 
# Git couldn't work out how to merge the two different sets of changes.
# 
# You now need to manually resolve the conflict.
# 
# It has marked the conflicted area:

# In[52]:


get_ipython().run_cell_magic('bash', '', 'cat Wales.md')


# Manually edit the file, to combine the changes as seems sensible and get rid of the symbols:

# In[55]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Fan y Big\n* Glyder Fawr')


# ## Commit the resolved file
# 
# Now commit the merged result:

# In[56]:


get_ipython().run_cell_magic('bash', '', 'git commit -a --no-edit # I added a No-edit for this non-interactive session. You can edit the commit if you like.')


# In[57]:


get_ipython().run_cell_magic('bash', '', 'git push')


# In[58]:


os.chdir(working_dir)


# In[59]:


get_ipython().run_cell_magic('bash', '', 'git pull')


# In[60]:


get_ipython().run_cell_magic('bash', '', 'cat Wales.md')


# In[61]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline --graph')


# ## Distributed VCS in teams with conflicts

# In[62]:


message = """
participant Sue as S
participant "Sue's repo" as SR
participant "Shared remote" as M
participant "Jim's repo" as JR
participant Jim as J

note left of S: edit the same line in wales.md
note right of J: edit the same line in wales.md
    
note left of S: git commit -am "update wales.md"
S->SR: add commit to local repo
    
note right of J: git commit -am "update wales.md"
J->JR: add commit to local repo
    
note left of S: git push
SR->M: transfer commit to remote
    
note right of J: git push
JR->M: !Rejected

note right of J: git pull
M->J: Make conflicted file with conflict markers
    
note right of J: edit file to resolve conflicts
note right of J: git add wales.md
note right of J: git commit
J->JR: Mark conflict as resolved

note right of J: git push
JR->M: Transfer merged history to remote

note left of S: git pull
M->SR: Download Jim's resolution of conflict.
    
"""

wsd(message)


# # The Levels of Git

# In[63]:


message = """
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Local Repository -> Local Repository : git commit -a
Local Repository -> Working Directory : git checkout
Local Repository -> Staging Area : git reset
Local Repository -> Working Directory: git reset --hard
Local Repository -> Remote Repository : git push
Remote Repository -> Local Repository : git fetch
Local Repository -> Working Directory : git merge
Remote Repository -> Working Directory: git pull
"""

wsd(message)


# ## Editing directly on GitHub
# 
# Note that you can also make changes in the GitHub website itself. Visit one of your files, and hit "edit".
# 
# Make a change in the edit window, and add an appropriate commit message.
# 
# That change now appears on the website, but not in your local copy. (Verify this). 

# Now pull, and check the change is now present on your local version. 

# ## GitHub as a social network
# 
# In addition to being a repository for code, and a way to publish code, GitHub is a social network.  
# 
# You can follow the public work of other coders: go to the profile of your collaborator in your browser, and hit the "follow" button. 
# 
# [Here's mine](https://github.com/jamespjh) : if you want to you can follow me.
# 
# Using GitHub to build up a good public profile of software projects you've worked on is great for your CV!
