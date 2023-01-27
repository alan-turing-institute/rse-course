#!/usr/bin/env python
# coding: utf-8

# # 2.3 Working with files

# *Estimated time for this notebook: 15 minutes*

# ## 2.3.1 Background
# Loading data from files

# An important part of this course is about using Python to analyse and visualise data.
# Most data, of course, is supplied to us in various *formats*: spreadsheets, database dumps, or text files in various formats (csv, tsv, json, yaml, hdf5, netcdf)
# It is also stored in some *medium*: on a local disk, a network drive, or on the internet in various ways.
# It is important to distinguish the data format, how the data is structured into a file, from the data's storage, where it is put. 
# 
# We'll look first at the question of data *transport*: loading data from a disk, and at downloading data from the internet.
# Then we'll look at data *parsing*: building Python structures from the data.
# These are related, but separate questions.

# ### An example datafile

# Let's write an example datafile to disk so we can investigate it. We'll just use a plain-text file. Jupyter notebook provides a way to do this: if we put
# `%%writefile` at the top of a cell, instead of being interpreted as python, the cell contents are saved to disk.

# In[1]:


get_ipython().run_cell_magic('writefile', 'mydata.txt', "A poet once said, 'The whole universe is in a glass of wine.'\nWe will probably never know in what sense he meant it, \nfor poets do not write to be understood. \nBut it is true that if we look at a glass of wine closely enough we see the entire universe. \nThere are the things of physics: the twisting liquid which evaporates depending\non the wind and weather, the reflection in the glass;\nand our imagination adds atoms.\nThe glass is a distillation of the earth's rocks,\nand in its composition we see the secrets of the universe's age, and the evolution of stars. \nWhat strange array of chemicals are in the wine? How did they come to be? \nThere are the ferments, the enzymes, the substrates, and the products.\nThere in wine is found the great generalization; all life is fermentation.\nNobody can discover the chemistry of wine without discovering, \nas did Louis Pasteur, the cause of much disease.\nHow vivid is the claret, pressing its existence into the consciousness that watches it!\nIf our small minds, for some convenience, divide this glass of wine, this universe, \ninto parts -- \nphysics, biology, geology, astronomy, psychology, and so on -- \nremember that nature does not know it!\n\nSo let us put it all back together, not forgetting ultimately what it is for.\nLet it give us one more final pleasure; drink it and forget it all!\n   - Richard Feynman\n")


# Where did that go? It went to the current folder, which for a notebook, by default, is where the notebook is on disk.

# In[2]:


import os  # The 'os' module gives us all the tools we need to search in the file system

os.getcwd()  # Use the 'getcwd' function from the 'os' module to find where we are on disk.


# Can we see if it is there?

# In[3]:


import os

[x for x in os.listdir(os.getcwd()) if ".txt" in x]


# Yep! Note how we used a list comprehension to filter all the extraneous files.

# ## 2.4.2 Path independence and `os`

# We can use `dirname` to get the parent folder for a folder, in a platform independent-way.

# In[4]:


os.path.dirname(os.getcwd())


# We could do this manually using `split`:

# In[5]:


"/".join(os.getcwd().split("/")[:-1])


# But this would not work on Windows, where path elements are separated with a `\` instead of a `/`. So it's important 
# to use `os.path` for this stuff.

# **Supplementary Materials**: If you're not already comfortable with how files fit into folders, and folders form a tree,
#     with folders containing subfolders, then look at http://swcarpentry.github.io/shell-novice/02-filedir/index.html. 
# 
# Satisfy yourself that after using `%%writefile`, you can then find the file on disk with Windows Explorer, macOS Finder, or the Linux Shell.

# We can see how in Python we can investigate the file system with functions in the `os` module, using just the same programming approaches as for anything else.

# We'll gradually learn more features of the `os` module as we go, allowing us to move around the disk, `walk` around the
# disk looking for relevant files, and so on. These will be important to master for automating our data analyses.

# ## 2.3.3 The python `file` type

# So, let's read our file:

# In[6]:


myfile = open("mydata.txt")


# In[7]:


type(myfile)


# We can go line-by-line, by treating the file as an iterable:

# In[8]:


[x for x in myfile]


# If we do that again, the file has already finished, there is no more data.

# In[9]:


[x for x in myfile]


# We need to 'rewind' it!

# In[10]:


myfile.seek(0)
[len(x) for x in myfile if "know" in x]


# It's really important to remember that a file is a *different* built in type than a string.

# ## 2.3.4 Reading Files

# We can read one line at a time with `readline`: 

# In[11]:


myfile.seek(0)
first = myfile.readline()


# In[12]:


first


# In[13]:


second = myfile.readline()


# In[14]:


second


# We can read the whole remaining file with `read`:

# In[15]:


rest = myfile.read()


# In[16]:


rest


# Which means that when a file is first opened, read is useful to just get the whole thing as a string:

# In[17]:


open("mydata.txt").read()


# You can also read just a few characters:

# In[18]:


myfile.seek(1335)


# In[19]:


myfile.read(15)


# ## 2.3.5 Converting Strings to Files

# Because files and strings are different types, we CANNOT just treat strings as if they were files:

# In[20]:


mystring = "Hello World\n My name is James"


# In[21]:


mystring


# In[22]:


mystring.readline()


# This is important, because some file format parsers expect input from a **file** and not a string. 
# We can convert between them using the StringIO class of the [io module](https://docs.python.org/3/library/io.html) in the standard library:

# In[23]:


from io import StringIO


# In[24]:


mystringasafile = StringIO(mystring)


# In[25]:


mystringasafile.readline()


# In[26]:


mystringasafile.readline()


# Note that in a string, `\n` is used to represent a newline.

# ## 2.4.6 Closing files

# We really ought to close files when we've finished with them, as it makes the computer more efficient. (On a shared computer,
# this is particularly important)

# In[27]:


myfile.close()


# Because it's so easy to forget this, python provides a **context manager** to open a file, then close it automatically at
# the end of an indented block:

# In[28]:


with open("mydata.txt") as somefile:
    content = somefile.read()

content


# The code to be done while the file is open is indented, just like for an `if` statement.

# You should pretty much **always** use this syntax for working with files.

# ## 2.3.7 Writing files

# We might want to create a file from a string in memory. We can't do this with the notebook's `%%writefile` -- this is
# just a notebook convenience, and isn't very programmable.

# When we open a file, we can specify a 'mode', in this case, 'w' for writing. ('r' for reading is the default.)

# In[29]:


with open("mywrittenfile", "w") as target:
    target.write("Hello")
    target.write("World")


# In[30]:


with open("mywrittenfile", "r") as source:
    print(source.read())


# And we can "append" to a file with mode 'a':

# In[31]:


with open("mywrittenfile", "a") as target:
    target.write("Hello")
    target.write("James")


# In[32]:


with open("mywrittenfile", "r") as source:
    print(source.read())


# If a file already exists, mode `w` will overwrite it.
