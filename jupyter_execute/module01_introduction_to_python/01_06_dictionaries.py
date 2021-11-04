#!/usr/bin/env python
# coding: utf-8

# # Dictionaries

# ## The Python Dictionary

# Python supports a container type called a dictionary.

# This is also known as an "associative array", "map" or "hash" in other languages.

# In a list, we use a number to look up an element:

# In[1]:


names = "Martin Luther King".split(" ")


# In[2]:


names[1]


# In a dictionary, we look up an element using **another object of our choice**:

# In[3]:


me = {"name": "James", "age": 39, "Jobs": ["Programmer", "Teacher"]}


# In[4]:


me


# In[5]:


me["Jobs"]


# In[6]:


me["age"]


# In[7]:


type(me)


# ### Keys and Values

# The things we can use to look up with are called **keys**:

# In[8]:


me.keys()


# The things we can look up are called **values**:

# In[9]:


me.values()


# When we test for containment on a `dict` we test on the **keys**:

# In[10]:


"Jobs" in me


# In[11]:


"James" in me


# In[12]:


"James" in me.values()


# ### Immutable Keys Only

# The way in which dictionaries work is one of the coolest things in computer science:
# the "hash table". The details of this are beyond the scope of this course, but we will consider some aspects in the section on performance programming. 
# 
# One consequence of this implementation is that you can only use **immutable** things as keys.

# In[13]:


good_match = {
    ("Lamb", "Mint"): True,
    ("Bacon", "Chocolate"): False
}


# but:

# In[14]:


illegal = {
    ["Lamb", "Mint"]: True,
    ["Bacon", "Chocolate"]: False
}


# Remember -- square brackets denote lists, round brackets denote `tuple`s.

# ### No guarantee of order

# 
# Another consequence of the way dictionaries work is that there's no guaranteed order among the
# elements:
# 
# 
# 

# In[15]:


my_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4}
print(my_dict)
print(my_dict.values())


# ## Sets

# A set is a `list` which cannot contain the same element twice.
# We make one by calling `set()` on any sequence, e.g. a list or string.

# In[16]:


name = "James Hetherington"
unique_letters = set(name)


# In[17]:


unique_letters


# Or by defining a literal like a dictionary, but without the colons:

# In[18]:


primes_below_ten = {2, 3, 5, 7}


# In[19]:


type(unique_letters)


# In[20]:


type(primes_below_ten)


# In[21]:


unique_letters


# This will be easier to read if we turn the set of letters back into a string, with `join`:

# In[22]:


"".join(unique_letters)


# A set has no particular order, but is really useful for checking or storing **unique** values.

# Set operations work as in mathematics:

# In[23]:


x = set("Hello")
y = set("Goodbye")


# In[24]:


x & y  # Intersection


# In[25]:


x | y  # Union


# In[26]:


y - x  # y intersection with complement of x: letters in Goodbye but not in Hello


# Your programs will be faster and more readable if you use the appropriate container type for your data's meaning.
# Always use a set for lists which can't in principle contain the same data twice, always use a dictionary for anything
# which feels like a mapping from keys to values.
