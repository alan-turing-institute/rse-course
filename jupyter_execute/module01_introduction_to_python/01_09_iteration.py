#!/usr/bin/env python
# coding: utf-8

# # 1.9 Iteration
# *Estimated time to complete this notebook: 10 minutes*

# Our other aspect of control is looping back on ourselves.
# 
# We use `for` ... `in` to "iterate" over lists:

# In[1]:


mylist = [3, 7, 15, 2]


# In[2]:


for whatever in mylist:
    print(whatever ** 2)


# Each time through the loop, the variable in the `value` slot is updated to the **next** element of the sequence.

# ## 1.9.1 Iterables

# 
# Any sequence type is iterable:
# 
# 
# 

# In[3]:


vowels = "aeiou"
sarcasm = []

for letter in "Okay":
    if letter.lower() in vowels:
        repetition = 3
    else:
        repetition = 1

    sarcasm.append(letter * repetition)

"".join(sarcasm)


# The above is a little puzzle, work through it to understand why it does what it does.

# ###  Dictionaries are Iterables

# All sequences are iterables. Some iterables (things you can `for` loop over) are not sequences (things with you can do `x[5]` to), for example sets and dictionaries.

# In[4]:


import datetime

now = datetime.datetime.now()

founded = {"James": 1976, "UCL": 1826, "Cambridge": 1209}

current_year = now.year

for thing in founded:
    print(thing, "is", current_year - founded[thing], "years old.")


# ## 1.9.2 Unpacking and Iteration

# 
# Unpacking can be useful with iteration:
# 
# 
# 

# In[5]:


triples = [[4, 11, 15], [39, 4, 18]]


# In[6]:


for whatever in triples:
    print(whatever)


# In[7]:


for first, middle, last in triples:
    print(middle)


# In[8]:


# A reminder that the words you use for variable names are arbitrary:
for hedgehog, badger, fox in triples:
    print(badger)


# 
# 
# 
# for example, to iterate over the items in a dictionary as pairs:
# 
# 
# 

# In[9]:


things = {
    "James": [1976, "Kendal"],
    "UCL": [1826, "Bloomsbury"],
    "Cambridge": [1209, "Cambridge"],
}

print(things.items())


# In[10]:


for name, year in founded.items():
    print(name, "is", current_year - year, "years old.")


# ## 1.9.3 Break, Continue

# 
# * Continue skips to the next turn of a loop
# * Break stops the loop early
# 
# 
# 

# In[11]:


for n in range(50):
    if n == 20:
        break
    if n % 2 == 0:
        continue
    print(n)


# These aren't useful that often, but are worth knowing about. There's also an optional `else` clause on loops, executed only if you don't `break`, but I've never found that useful.

# In[ ]:




