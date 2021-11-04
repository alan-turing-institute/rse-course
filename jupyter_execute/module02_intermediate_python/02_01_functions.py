#!/usr/bin/env python
# coding: utf-8

# # Functions 

# # Definition

# 
# We use `def` to define a function, and `return` to pass back a value:
# 
# 
# 

# In[1]:


def double(x):
    return x * 2


print(double(5), double([5]), double("five"))


# # Default Parameters

# We can specify default values for parameters:

# In[2]:


def jeeves(name="Sir"):
    return "Very good, {}".format(name)


# In[3]:


jeeves()


# In[4]:


jeeves("James")


# If you have some parameters with defaults, and some without, those with defaults **must** go later.

# If you have multiple default arguments, you can specify neither, one or both:

# In[5]:


def jeeves(greeting="Very good", name="Sir"):
    return "{}, {}".format(greeting, name)


# In[6]:


jeeves()


# In[7]:


jeeves("Hello")


# In[8]:


jeeves(name="James")


# In[9]:


jeeves(greeting="Suits you")


# In[10]:


jeeves("Hello", "Sailor")


# # Side effects

# Functions can do things to change their **mutable** arguments,
# so `return` is optional.
# 
# This is pretty awful style, in general, functions should normally be side-effect free.
# 
# Here is a contrived example of a function that makes plausible use of a side-effect

# In[11]:


def double_inplace(vec):
    vec[:] = [element * 2 for element in vec]


z = list(range(4))
double_inplace(z)
print(z)


# In[12]:


letters = ["a", "b", "c", "d", "e", "f", "g"]
letters[:] = []


# In this example, we're using `[:]` to access into the same list, and write it's data.
# 
#     vec = [element*2 for element in vec]
# 
# would just move a local label, not change the input.

# But I'd usually just write this as a function which **returned** the output:

# In[13]:


def double(vec):
    return [element * 2 for element in vec]


# Let's remind ourselves of the behaviour for modifying lists in-place using `[:]` with a simple array:

# In[14]:


x = 5
x = 7
x = ["a", "b", "c"]
y = x


# In[15]:


x


# In[16]:


x[:] = ["Hooray!", "Yippee"]


# In[17]:


y


# ## Early Return

# 
# Return without arguments can be used to exit early from a function
# 
# 
# 

# Here's a slightly more plausibly useful function-with-side-effects to extend a list with a specified padding datum.

# In[18]:


def extend(to, vec, pad):
    if len(vec) >= to:
        return  # Exit early, list is already long enough.

    vec[:] = vec + [pad] * (to - len(vec))


# In[19]:


x = list(range(3))
extend(6, x, "a")
print(x)


# In[20]:


z = list(range(9))
extend(6, z, "a")
print(z)


# ## Unpacking arguments

# In[21]:


def arrow(before, after):
    return str(before) + " -> " + str(after)


arrow(1, 3)


# 
# If a function that takes multiple arguments is given an iterable object prepended with '*',
# each element of that object is taken in turn and used to fill the function's arguments one-by-one.
# 
# 
# 

# In[22]:


x = [1, -1]
arrow(*x)


# 
# 
# 
# This can be quite powerful:
# 
# 
# 

# In[23]:


charges = {"neutron": 0, "proton": 1, "electron": -1}
for particle in charges.items():
    print(arrow(*particle))


# ## Sequence Arguments

# Similiarly, if a `*` is used in the **definition** of a function, multiple
# arguments are absorbed into a list **inside** the function:

# In[24]:


def doubler(*sequence):
    return [x * 2 for x in sequence]


# In[25]:


doubler(1, 2, 3)


# In[26]:


doubler(5, 2, "Wow!")


# ## Keyword Arguments

# If two asterisks are used, named arguments are supplied inside the function as a dictionary:

# In[27]:


def arrowify(**args):
    for key, value in args.items():
        print(key + " -> " + value)


arrowify(neutron="n", proton="p", electron="e")


# These different approaches can be mixed:

# In[28]:


def somefunc(a, b, *args, **kwargs):
    print("A:", a)
    print("B:", b)
    print("args:", args)
    print("keyword args", kwargs)


# In[29]:


somefunc(1, 2, 3, 4, 5, fish="Haddock")

