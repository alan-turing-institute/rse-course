#!/usr/bin/env python
# coding: utf-8

# # 2.0 Comprehensions

# *Estimated time to complete this notebook: 10 minutes*

# ## 2.0.1 The list comprehension

# If you write a for loop **inside** a pair of square brackets for a list, you magic up a list as defined.
# This can make for concise but hard to read code, so be careful.

# In[1]:


[2 ** x for x in range(10)]


# Which is equivalent to the following code without using comprehensions:

# In[2]:


result = []
for x in range(10):
    result.append(2 ** x)

result


# You can do quite weird and cool things with comprehensions:

# In[3]:


[len(str(2 ** x)) for x in range(10)]


# ## 2.0.2 Selection in comprehensions

# You can write an `if` statement in comprehensions too: 

# In[4]:


[2 ** x for x in range(30) if x % 3 == 0]


# Consider the following, and make sure you understand why it works:

# In[5]:


"".join([letter for letter in "James Hetherington" if letter.lower() not in "aeiou"])


# ## 2.0.3 Comprehensions versus building lists with `append`:

# This code:

# In[6]:


result = []
for x in range(30):
    if x % 3 == 0:
        result.append(2 ** x)
result


# Does the same as the comprehension above. The comprehension is generally considered more readable.

# Comprehensions are therefore an example of what we call 'syntactic sugar': they do not increase the capabilities of the language.

# Instead, they make it possible to write the same thing in a more readable way. 

# Almost everything we learn from now on will be either syntactic sugar or interaction with something other than idealised memory, such as a storage device or the internet. Once you have variables, conditionality, and branching, your language can do anything. (And this can be proved.)

# ## 2.0.4 Nested comprehensions

# If you write two `for` statements in a comprehension, you get a single array generated over all the pairs:

# In[7]:


[x - y for x in range(4) for y in range(4)]


# You can select on either, or on some combination:

# In[8]:


[x - y for x in range(4) for y in range(4) if x >= y]


# If you want something more like a matrix, you need to do *two nested* comprehensions!

# In[9]:


[[x - y for x in range(4)] for y in range(4)]


# Note the subtly different square brackets.

# Note that the list order for multiple or nested comprehensions can be confusing:

# In[10]:


[x + y for x in ["a", "b", "c"] for y in ["1", "2", "3"]]


# In[11]:


[[x + y for x in ["a", "b", "c"]] for y in ["1", "2", "3"]]


# ## 2.0.5 Dictionary Comprehensions

# You can automatically build dictionaries, by using a list comprehension syntax, but with curly brackets and a colon:

# In[12]:


{(str(x)) * 3: x for x in range(3)}


# ## 2.0.6 List-based thinking

# Once you start to get comfortable with comprehensions, you find yourself working with containers, nested groups of lists 
# and dictionaries, as the 'things' in your program, not individual variables. 

# Given a way to analyse some dataset, we'll find ourselves writing stuff like:
# 
#     analysed_data = [analyze(datum) for datum in data]

# There are lots of built-in methods that provide actions on lists as a whole:

# In[13]:


any([True, False, True])


# In[14]:


all([True, False, True])


# In[15]:


max([1, 2, 3])


# In[16]:


sum([1, 2, 3])


# My favourite is `map`, which, similar to a list comprehension, applies one function to every member of a list:

# In[17]:


[str(x) for x in range(10)]


# In[18]:


list(map(str, range(10)))


# So I can write:
#     
#     analysed_data = map(analyse, data)
# 
# We'll learn more about `map` and similar functions when we discuss functional programming later in the course.

# In[ ]:




