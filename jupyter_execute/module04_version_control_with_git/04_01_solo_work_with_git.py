#!/usr/bin/env python
# coding: utf-8

# # Solo work with Git

# So, we're in our git working directory:

# In[1]:


import os

top_dir = os.getcwd()
git_dir = os.path.join(top_dir, "learning_git")
working_dir = os.path.join(git_dir, "git_example")
os.chdir(working_dir)
working_dir


# ## A first example file
# 
# So let's create an example file, and see how to start to manage a history of changes to it.

#     <my editor> test.md # Type some content into the file.

# In[2]:


get_ipython().run_cell_magic('writefile', 'test.md', 'Mountains in the UK   \n===================   \nEngland is not very mountainous.   \nBut has some tall hills, and maybe a mountain or two depending on your definition.')


# In[3]:


cat test.md


# ## Telling Git about the File
# 
# So, let's tell Git that `test.md` is a file which is important, and we would like to keep track of its history:

# In[4]:


get_ipython().run_cell_magic('bash', '', 'git add test.md')


# Don't forget: Any files in repositories which you want to "track" need to be added with `git add` after you create them.

# ## Our first commit
# 
# Now, we need to tell Git to record the first version of this file in the history of changes:

# In[5]:


get_ipython().run_cell_magic('bash', '', 'git commit -m "First commit of discourse on UK topography"')


# And note the confirmation from Git.
# 
# There's a lot of output there you can ignore for now.

# ## Configuring Git with your editor
# 
# If you don't type in the log message directly with -m "Some message", then an editor will pop up, to allow you
# to edit your message on the fly.

# For this to work, you have to tell git where to find your editor.
# 
# ```bash
# git config --global core.editor vim 
# ```

# You can find out what you currently have with:
# ```bash
# git config --get core.editor
# ```

# To configure Notepad++ on Windows you'll need something like the below, ask a demonstrator to help for your machine.

# ```bash
# git config --global core.editor "'C:/Program Files (x86)/Notepad++/notepad++.exe' -multiInst -nosession -noPlugin"
# ```

# I'm going to be using `vim` as my editor, but you can use whatever editor you prefer. (Windows users could use "Notepad++", Mac users could use "textmate" or "Sublime Text", linux users could use `vim`, `nano` or `emacs`.)

# ## Git log
# 
# Git now has one change in its history:

# In[6]:


get_ipython().run_cell_magic('bash', '', 'git log')


# You can see the commit message, author, and date...

# ## Hash Codes
# 
# The commit "hash code", e.g.
# 
# `06530761f1c3e18917cb67a1d1b0aa156a2231b0`
# 
# is a unique identifier of that particular revision. 
# 
# (This is a really long code, but whenever you need to use it, you can just use the first few characters, however many characters is long enough to make it unique, `06530761` for example. )

# ## Nothing to see here
# 
# Note that git will now tell us that our "working directory" is up-to-date with the repository: there are no changes to the files that aren't recorded in the repository history:

# In[7]:


get_ipython().run_cell_magic('bash', '', 'git status')


# Let's edit the file again:
# 
#     vim test.md

# In[8]:


get_ipython().run_cell_magic('writefile', 'test.md', 'Mountains in the UK   \n===================   \nEngland is not very mountainous.   \nBut has some tall hills, and maybe a mountain or two depending on your definition.\n\nMount Fictional, in Barsetshire, U.K. is the tallest mountain in the world.')


# In[9]:


cat test.md


# ## Unstaged changes

# In[10]:


get_ipython().run_cell_magic('bash', '', 'git status')


# We can now see that there is a change to "test.md" which is currently "not staged for commit". What does this mean? 
# 
# If we do a `git commit` now *nothing will happen*. 
# 
# Git will only commit changes to files that you choose to include in each commit.
# 
# This is a difference from other version control systems, where committing will affect all changed files. 

# We can see the differences in the file with:

# In[11]:


get_ipython().run_cell_magic('bash', '', 'git diff')


# Deleted lines are prefixed with a minus, added lines prefixed with a plus.

# ## Staging a file to be included in the next commit
# 
# To include the file in the next commit, we have a few choices. This is one of the things to be careful of with git: there are lots of ways to do similar things, and it can be hard to keep track of them all.

# In[12]:


get_ipython().run_cell_magic('bash', '', 'git add --update')


# This says "include in the next commit, all files which have ever been included before". 
# 
# Note that `git add` is the command we use to introduce git to a new file, but also the command we use to "stage" a file to be included in the next commit. 

# ## The staging area
# 
# The "staging area" or "index" is the git jargon for the place which contains the list of changes which will be included in the next commit.
# 
# You can include specific changes to specific files with `git add`, commit them, add some more files, and commit them. (You can even add specific changes within a file to be included in the index.)

# ## Message Sequence Charts

# In order to illustrate the behaviour of Git, it will be useful to be able to generate figures in Python
# of a "message sequence chart" flavour.

# There's a nice online tool to do this, called "Message Sequence Charts".

# Have a look at https://www.websequencediagrams.com

# Instead of just showing you these diagrams, I'm showing you in this notebook how I make them.
# This is part of our "reproducible computing" approach; always generating all our figures from code.

# Here's some quick code in the Notebook to download and display an MSC illustration, using the Web Sequence Diagrams API:

# In[13]:


get_ipython().run_cell_magic('writefile', 'wsd.py', 'import requests\nimport re\nimport IPython\n\n\ndef wsd(code):\n    response = requests.post(\n        "http://www.websequencediagrams.com/index.php",\n        data={\n            "message": code,\n            "apiVersion": 1,\n        },\n    )\n    expr = re.compile("(\\?(img|pdf|png|svg)=[a-zA-Z0-9]+)")\n    m = expr.search(response.text)\n    if m == None:\n        print("Invalid response from server.")\n        return False\n\n    image = requests.get("http://www.websequencediagrams.com/" + m.group(0))\n    return IPython.core.display.Image(image.content)')


# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')
from wsd import wsd

wsd("Sender->Recipient: Hello\n Recipient->Sender: Message received OK")


# ## The Levels of Git

# Let's make ourselves a sequence chart to show the different aspects of Git we've seen so far:

# In[15]:


message = """
Working Directory -> Staging Area : git add
Staging Area -> Local Repository : git commit
Working Directory -> Local Repository : git commit -a
"""
wsd(message)


# ## Review of status

# In[16]:


get_ipython().run_cell_magic('bash', '', 'git status')


# In[17]:


get_ipython().run_cell_magic('bash', '', 'git commit -m "Add a lie about a mountain"')


# In[18]:


get_ipython().run_cell_magic('bash', '', 'git log')


# Great, we now have a file which contains a mistake.

# ## Carry on regardless
# 
# In a while, we'll use Git to roll back to the last correct version: this is one of the main reasons we wanted to use version control, after all! But for now, let's do just as we would if we were writing code, not notice our mistake and keep working...

# ```bash
# vim test.md
# ```

# In[19]:


get_ipython().run_cell_magic('writefile', 'test.md', 'Mountains and Hills in the UK   \n===================   \nEngland is not very mountainous.   \nBut has some tall hills, and maybe a mountain or two depending on your definition.\n\nMount Fictional, in Barsetshire, U.K. is the tallest mountain in the world.')


# In[20]:


cat test.md


# ## Commit with a built-in-add

# In[21]:


get_ipython().run_cell_magic('bash', '', 'git commit -am "Change title"')


# This last command, `git commit -a` automatically adds changes to all tracked files to the staging area, as part of the commit command. So, if you never want to just add changes to some tracked files but not others, you can just use this and forget about the staging area!

# ## Review of changes

# In[22]:


get_ipython().run_cell_magic('bash', '', 'git log | head')


# We now have three changes in the history:

# In[23]:


get_ipython().run_cell_magic('bash', '', 'git log --oneline')


# ## Git Solo Workflow

# We can make a diagram that summarises the above story:

# In[24]:


message = """
participant "Jim's repo" as R
participant "Jim's index" as I
participant Jim as J

note right of J: vim test.md

note right of J: git init
J->R: create

note right of J: git add test.md

J->I: Add content of test.md

note right of J: git commit
I->R: Commit content of test.md

note right of J:  vim test.md

note right of J: git add --update
J->I: Add content of test.md
note right of J: git commit -m "Add a lie"
I->R: Commit change to test.md

note right of J:  vim test.md
note right of J: git commit -am "Change title"
J->R: Add and commit change to test.md (and all tracked files)
"""
wsd(message)

