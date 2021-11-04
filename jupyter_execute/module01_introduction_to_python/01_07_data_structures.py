#!/usr/bin/env python
# coding: utf-8

# # Data structures

# ## Nested Lists and Dictionaries

# In research programming, one of our most common tasks is building an appropriate *structure* to model our complicated
# data. Later in the course, we'll see how we can define our own types, with their own attributes, properties, and methods. But probably the most common approach is to use nested structures of lists, dictionaries, and sets to model our data. For example, an address might be modelled as a dictionary with appropriately named fields:

# In[1]:


UCL = {"City": "London", "Street": "Gower Street", "Postcode": "WC1E 6BT"}


# In[2]:


James = {"City": "London", "Street": "Waterson Street", "Postcode": "E2 8HH"}


# A collection of people's addresses is then a list of dictionaries:

# In[3]:


addresses = [UCL, James]


# In[4]:


addresses


# A more complicated data structure, for example for a census database, might have a list of residents or employees at each address:

# In[5]:


UCL["people"] = ["Clare", "James", "Owain"]


# In[6]:


James["people"] = ["Sue", "James"]


# In[7]:


addresses


# Which is then a list of dictionaries, with keys which are strings or lists.

# We can go further, e.g.:

# In[8]:


UCL["Residential"] = False


# And we can write code against our structures:

# In[9]:


leaders = [place["people"][0] for place in addresses]
leaders


# This was an example of a 'list comprehension', which have used to get data of this structure, and which we'll see more of in a moment...

# ## Exercise: a Maze Model.

# Work with a partner to design a data structure to represent a maze using dictionaries and lists.

# * Each place in the maze has a name, which is a string.
# * Each place in the maze has one or more people currently standing at it, by name.
# * Each place in the maze has a maximum capacity of people that can fit in it.
# * From each place in the maze, you can go from that place to a few other places, using a direction like 'up', 'north', 
# or 'sideways'

# Create an example instance, in a notebook, of a simple structure for your maze:

# * The front room can hold 2 people. James is currently there. You can go outside to the garden, or upstairs to the bedroom, or north to the kitchen.
# * From the kitchen, you can go south to the front room. It fits 1 person.
# * From the garden you can go inside to front room. It fits 3 people. Sue is currently there.
# * From the bedroom, you can go downstairs to the front room. You can also jump out of the window to the garden. It fits 2 people.

# Make sure that your model:
# 
# * Allows empty rooms
# * Allows you to jump out of the upstairs window, but not to fly back up.
# * Allows rooms which people can't fit in.

# ```python
# house = [ "Your answer here" ]
# ```
