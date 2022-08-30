#!/usr/bin/env python
# coding: utf-8

# # 1.2 Variables
# *Estimated time to complete this notebook: 10 minutes*

# ## 1.2.1 Variable Assignment

# When we generate a result, the answer is displayed, but not kept anywhere.

# In[1]:


2 * 3


# If we want to get back to that result, we have to store it. We put it in a box, with a name on the box. This is a **variable**.

# In[2]:


six = 2 * 3


# In[3]:


print(six)


# If we look for a variable that hasn't ever been defined, we get an error. 

# In[4]:


print(seven)


# That's **not** the same as an empty box, well labeled:

# In[5]:


nothing = None


# In[6]:


print(nothing)


# In[7]:


type(None)


# (None is the special python value for a no-value variable.)

# *Supplementary Materials*: There's more on variables at http://swcarpentry.github.io/python-novice-inflammation/01-numpy/index.html 

# Anywhere we could put a raw number, we can put a variable label, and that works fine:

# In[8]:


print(5 * six)


# In[9]:


scary = six * six * six


# In[10]:


print(scary)


# ## 1.2.2 Reassignment and multiple labels

# But here's the real scary thing: it seems like we can put something else in that box:

# In[11]:


scary = 25


# In[12]:


print(scary)


# Note that **the data that was there before has been lost**. 

# No labels refer to it any more - so it has been "Garbage Collected"! We might imagine something pulled out of the box, and thrown on the floor, to make way for the next occupant.

# In fact, though, it is the **label** that has moved. We can see this because we have more than one label refering to the same box:

# In[13]:


name = "James"


# In[14]:


nom = name


# In[15]:


print(nom)


# In[16]:


print(name)


# And we can move just one of those labels:

# In[17]:


nom = "Hetherington"


# In[18]:


print(name)


# In[19]:


print(nom)


# So we can now develop a better understanding of our labels and boxes: each box is a piece of space (an *address*) in computer memory.
# Each label (variable) is a reference to such a place.

# When the number of labels on a box ("variables referencing an address") gets down to zero, then the data in the box cannot be found any more.

# After a while, the language's "Garbage collector" will wander by, notice a box with no labels, and throw the data away, **making that box
# available for more data**.

# Old fashioned languages like C and Fortran don't have Garbage collectors. So a memory address with no references to it
# still takes up memory, and the computer can more easily run out.

# So when I write:

# In[20]:


name = "Jim"


# The following things happen:

# 1. A new text **object** is created, and an address in memory is found for it.
# 1. The variable "name" is moved to refer to that address.
# 1. The old address, containing "James", now has no labels.
# 1. The garbage collector frees the memory at the old address.

# **Supplementary materials**: There's an online python tutor which is great for visualising memory and references. Try the [scenario we just looked at](http://www.pythontutor.com/visualize.html#code=name+%3D+%22James%22%0Anom+%3D+name%0Aprint+nom%0Aprint+name%0Anom+%3D+%22Hetherington%22%0Aprint+nom%0Aprint+name%0Aname%3D+%22Jim%22%0Aprint+nom%0Aprint+name&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0)
# 
# Labels are contained in groups called "frames": our frame contains two labels, 'nom' and 'name'.

# ## 1.2.3 Objects and types

# An object, like `name`, has a type. In the online python tutor example, we see that the objects have type "str".
# `str` means a text object: Programmers call these 'strings'. 

# In[21]:


type(name)


# Depending on its type, an object can have different *properties*: data fields Inside the object.

# Consider a Python complex number for example:

# In[22]:


z = 3 + 1j


# We can see what properties and methods an object has available using the `dir` function:

# In[23]:


dir(z)


# You can see that there are several methods whose name starts and ends with `__` (e.g. `__init__`): these are special methods that Python uses internally, and we will discuss some of them later on in this course. The others (in this case, `conjugate`, `img` and `real`) are the methods and fields through which we can interact with this object.

# In[24]:


type(z)


# In[25]:


z.real


# In[26]:


z.imag


# A property of an object is accessed with a dot.

# The jargon is that the "dot operator" is used to obtain a property of an object.

# When we try to access a property that doesn't exist, we get an error:

# In[27]:


z.wrong


# ## 1.2.4 Reading error messages.

# It's important, when learning to program, to develop an ability to read an error message and find, from in amongst
# all the confusing noise, the bit of the error message which tells you what to change!

# We don't yet know what is meant by `AttributeError`, or "Traceback".

# In[28]:


z2 = 5 - 6j
print("Gets to here")
print(z.wrong)
print("Didn't get to here")


# But in the above, we can see that the error happens on the **third** line of our code cell.

# We can also see that the error message: 
# > 'complex' object has no attribute 'wrong' 
# 
# ...tells us something important. Even if we don't understand the rest, this is useful for debugging!

# ## 1.2.5 Variables and the notebook kernel

# When I type code in the notebook, the objects live in memory between cells.

# In[29]:


number = 0


# In[30]:


print(number)


# If I change a variable:

# In[31]:


number = number + 1


# In[32]:


print(number)


# It keeps its new value for the next cell.

# But cells are **not** always evaluated in order.

# If I now go back to input cell reading `number = number + 1`, and run it again, with shift-enter. Number will change from 2 to 2, then from 2 to 3, then from 3 to 4... Try it!

# So it's important to remember that if you move your cursor around in the notebook, it doesn't always run top to bottom.

# **Supplementary material**: (1) https://jupyter-notebook.readthedocs.io/en/latest/ 
