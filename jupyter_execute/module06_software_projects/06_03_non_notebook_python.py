#!/usr/bin/env python
# coding: utf-8

# # Python not in the Notebook

# We will often want to save our Python classes, for use in multiple Notebooks.
# We can do this by writing text files with a .py extension, and then `importing` them.

# ## Writing Python in Text Files

# You can use a text editor like [Atom](https://atom.io) for Mac or [Notepad++](https://notepad-plus-plus.org) for windows to do this. If you create your own Python files ending in .py, then you can import them with `import` just like external libraries.

# You can also maintain your library code in a Notebook, and use %%writefile to create your library.

# Libraries are usually structured with multiple files, one for each class.

# We group our modules into packages, by putting them together into a folder. You can do this with explorer, or using a shell, or even with Python:

# In[1]:


import os

if "mazetool" not in os.listdir(os.getcwd()):
    os.mkdir("mazetool")


# In[2]:


get_ipython().run_cell_magic('writefile', 'mazetool/maze.py', 'from .room import Room\nfrom .person import Person\n\n\nclass Maze:\n    def __init__(self, name):\n        self.name = name\n        self.rooms = []\n        self.occupants = []\n\n    def add_room(self, name, capacity):\n        result = Room(name, capacity)\n        self.rooms.append(result)\n        return result\n\n    def add_exit(self, name, source, target, reverse=None):\n        source.add_exit(name, target)\n        if reverse:\n            target.add_exit(reverse, source)\n\n    def add_occupant(self, name, room):\n        self.occupants.append(Person(name, room))\n        room.occupancy += 1\n\n    def wander(self):\n        "Move all the people in a random direction"\n        for occupant in self.occupants:\n            occupant.wander()\n\n    def describe(self):\n        for occupant in self.occupants:\n            occupant.describe()\n\n    def step(self):\n        house.describe()\n        print()\n        house.wander()\n        print()\n\n    def simulate(self, steps):\n        for _ in range(steps):\n            self.step()')


# In[3]:


get_ipython().run_cell_magic('writefile', 'mazetool/room.py', 'from .exit import Exit\n\n\nclass Room:\n    def __init__(self, name, capacity):\n        self.name = name\n        self.capacity = capacity\n        self.occupancy = 0\n        self.exits = []\n\n    def has_space(self):\n        return self.occupancy < self.capacity\n\n    def available_exits(self):\n        return [exit for exit in self.exits if exit.valid()]\n\n    def random_valid_exit(self):\n        import random\n\n        if not self.available_exits():\n            return None\n        return random.choice(self.available_exits())\n\n    def add_exit(self, name, target):\n        self.exits.append(Exit(name, target))')


# In[4]:


get_ipython().run_cell_magic('writefile', 'mazetool/person.py', '\n\nclass Person:\n    def __init__(self, name, room=None):\n        self.name = name\n        self.room = room\n\n    def use(self, exit):\n        self.room.occupancy -= 1\n        destination = exit.target\n        destination.occupancy += 1\n        self.room = destination\n        print(self.name, "goes", exit.name, "to the", destination.name)\n\n    def wander(self):\n        exit = self.room.random_valid_exit()\n        if exit:\n            self.use(exit)\n\n    def describe(self):\n        print(self.name, "is in the", self.room.name)')


# In[5]:


get_ipython().run_cell_magic('writefile', 'mazetool/exit.py', '\n\nclass Exit:\n    def __init__(self, name, target):\n        self.name = name\n        self.target = target\n\n    def valid(self):\n        return self.target.has_space()')


# **(Required for older versions of Python)**: In order to tell Python that our "mazetool" folder is a Python package, we have to make a special file called `__init__.py`. If you import things in there, they are imported as part of the package:

# In[6]:


get_ipython().run_cell_magic('writefile', 'mazetool/__init__.py', 'from .maze import Maze  # Python 3 relative import')


# ## Loading Our Package

# We just wrote the files, there is no "Maze" class in this notebook yet:

# In[7]:


myhouse = Maze("My New House")


# But now, we can import Maze, (and the other files will get imported via the chained Import statements, starting from the `__init__.py` file.

# In[8]:


import mazetool


# In[9]:


mazetool.exit.Exit


# In[10]:


from mazetool import Maze


# In[11]:


house = Maze("My New House")
living = house.add_room("livingroom", 2)


# Note the files we have created are on the disk in the folder we made:

# In[12]:


import os


# In[13]:


os.listdir(os.path.join(os.getcwd(), "mazetool"))


# `.pyc` files are "Compiled" temporary python files that the system generates to speed things up. They'll be regenerated
# on the fly when your `.py` files change.

# ## The Python Path

# We want to `import` these from notebooks elsewhere on our computer:
# it would be a bad idea to keep all our Python work in one folder.

# **Supplementary material** The best way to do this is to learn how to make our code
# into a proper module that we can install. We'll see more on that in a few lectures' time.

# Alternatively, we can add a folder to the "Python Path", where python searches for modules:

# In[14]:


import sys

print(sys.path[-3])
print(sys.path[-2])
print(sys.path[-1])


# In[15]:


sys.path.append("/home/jamespjh/devel/libraries/python")


# In[16]:


print(sys.path[-1])


# I've thus added a folder to the list of places searched. If you want to do this permanently, you should set the PYTHONPATH Environment Variable,
# which you can learn about in a shell course, or can read about online for your operating system.
