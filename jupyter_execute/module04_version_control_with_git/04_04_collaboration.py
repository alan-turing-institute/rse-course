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


get_ipython().run_cell_magic('bash', '', 'pwd\nrm -rf github-example # cleanup after previous example\nrm -rf partner_dir # cleanup after previous example\n')


# Next, the collaborator needs to find out the URL of the repository: they should go to the leader's repository's GitHub page, and note the URL on the top of the screen.
# 
# As before, we're using `SSH` to connect - to do this you'll need to make sure the `ssh` button is pushed, and check that the URL begins with `git@github.com`. 
# 
# Copy the URL into your clipboard by clicking on the icon to the right of the URL, and then:

# In[3]:


get_ipython().run_cell_magic('bash', '', 'pwd\ngit clone git@github.com:alan-turing-institute/github-example.git partner_dir\n')


# In[4]:


partner_dir = os.path.join(git_dir, "partner_dir")
os.chdir(partner_dir)


# In[5]:


get_ipython().run_cell_magic('bash', '', 'pwd\nls\n')


# Note that your partner's files are now present on your disk:

# In[6]:


get_ipython().run_cell_magic('bash', '', 'cat lakeland.md\n')


# ## Nonconflicting changes
# 
# Now, both of you should make some changes. To start with, make changes to *different* files. This will mean your work doesn't "conflict". Later, we'll see how to deal with changes to a shared file.

# Both of you should commit, but not push, your changes to your respective files:

# E.g., the leader:

# In[7]:


os.chdir(working_dir)


# In[8]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Tryfan\n* Yr Wyddfa\n')


# In[9]:


get_ipython().run_cell_magic('bash', '', 'ls\n')


# In[10]:


get_ipython().run_cell_magic('bash', '', 'git add Wales.md\ngit commit -m "Add wales"\n')


# And the partner:

# In[11]:


os.chdir(partner_dir)


# In[12]:


get_ipython().run_cell_magic('writefile', 'Scotland.md', 'Mountains In Scotland\n==================\n\n* Ben Eighe\n* Cairngorm\n')


# In[13]:


get_ipython().run_cell_magic('bash', '', 'ls\n')


# In[14]:


get_ipython().run_cell_magic('bash', '', 'git add Scotland.md\ngit commit -m "Add Scotland"\n')


# One of you should now push with `git push`:

# In[15]:


get_ipython().run_cell_magic('bash', '', 'git push\n')


# ## Rejected push

# The other should then attempt to push, but should receive an error message:

# In[16]:


os.chdir(working_dir)


# In[17]:


get_ipython().run_cell_magic('bash', '', 'git push || echo "Push failed"\n')


# Do as it suggests:

# In[18]:


get_ipython().run_cell_magic('bash', '', 'git pull\n')


# ## Merge commits
# 
# A window may pop up with a suggested default commit message. This commit is special: it is a *merge* commit. It is a commit which combines your collaborator's work with your own.

# Now, push again with `git push`. This time it works. If you look on GitHub, you'll now see that it contains both sets of changes.

# In[19]:


get_ipython().run_cell_magic('bash', '', 'git push\n')


# The partner now needs to pull down that commit:

# In[20]:


os.chdir(partner_dir)


# In[21]:


get_ipython().run_cell_magic('bash', '', 'git pull\n')


# In[22]:


get_ipython().run_cell_magic('bash', '', 'ls\n')


# ## Nonconflicted commits to the same file
# 
# Go through the whole process again, but this time, both of you should make changes to a single file, but make sure that you don't touch the same *line*. Again, the merge should work as before:

# In[23]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Tryfan\n* Snowdon\n')


# In[24]:


get_ipython().run_cell_magic('bash', '', 'git diff\n')


# In[25]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Translating from the Welsh"\n')


# In[26]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline\n')


# In[27]:


os.chdir(working_dir)


# In[28]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Yr Wyddfa\n')


# In[29]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add a beacon"\n')


# In[30]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline\n')


# In[31]:


get_ipython().run_cell_magic('bash', '', 'git push\n')


# Switching back to the other partner...

# In[32]:


os.chdir(partner_dir)


# In[33]:


get_ipython().run_cell_magic('bash', '', 'git push || echo "Push failed"\n')


# In[34]:


get_ipython().run_cell_magic('bash', '', 'git pull\n')


# In[35]:


get_ipython().run_cell_magic('bash', '', 'git push\n')


# In[36]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline --graph\n')


# In[37]:


os.chdir(working_dir)


# In[38]:


get_ipython().run_cell_magic('bash', '', 'git pull\n')


# In[39]:


get_ipython().run_cell_magic('bash', '', 'git log --graph --oneline\n')


# In[40]:


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

# In[41]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Fan y Big\n')


# In[42]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add another Beacon"\ngit push\n')


# In[43]:


os.chdir(partner_dir)


# In[44]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Glyder Fawr\n')


# In[45]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Add Glyder"\n')


# In[46]:


get_ipython().run_cell_magic('bash', '', 'git push || echo "Push failed"\n')


# When you pull, instead of offering an automatic merge commit message, it says:

# In[47]:


get_ipython().run_cell_magic('bash', '', 'git pull || echo "Pull failed"\n')


# ## Resolving conflicts
# 
# Git couldn't work out how to merge the two different sets of changes.
# 
# You now need to manually resolve the conflict.
# 
# It has marked the conflicted area:

# In[48]:


get_ipython().run_cell_magic('bash', '', 'cat Wales.md\n')


# Manually edit the file, to combine the changes as seems sensible and get rid of the symbols:

# In[49]:


get_ipython().run_cell_magic('writefile', 'Wales.md', 'Mountains In Wales\n==================\n\n* Pen y Fan\n* Tryfan\n* Snowdon\n* Fan y Big\n* Glyder Fawr\n')


# ## Commit the resolved file
# 
# Now commit the merged result:

# In[50]:


get_ipython().run_cell_magic('bash', '', 'git commit -a --no-edit # I added a No-edit for this non-interactive session. You can edit the commit if you like.\n')


# In[51]:


get_ipython().run_cell_magic('bash', '', 'git push\n')


# In[52]:


os.chdir(working_dir)


# In[53]:


get_ipython().run_cell_magic('bash', '', 'git pull\n')


# In[54]:


get_ipython().run_cell_magic('bash', '', 'cat Wales.md\n')


# In[55]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline --graph\n')


# ## Distributed VCS in teams with conflicts

# In[56]:


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

# In[57]:


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
