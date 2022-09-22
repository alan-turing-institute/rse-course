#!/usr/bin/env python
# coding: utf-8

# # 2.1 Functions 

# *Estimated time to complete this notebook: 15 minutes*

# ## 2.1.1 Definition

# 
# We use `def` to define a function, and `return` to pass back a value:
# 
# 
# 

# In[1]:


def double(x):
    return x * 2


print(double(5), double([5]), double("five"))


# ## 2.1.2 Default Parameters

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


# ## 2.1.3 Early Return

# 
# Return without arguments can be used to exit early from a function
# 
# 
# 

# Here's a slightly convoluted example of a function which will return early under specific conditions. In this case if a list contains the string 'cat'.

# In[11]:


def are_there_cats(my_input_list):
    
    if "cat" in my_input_list: # If the string "cat" is in the list
        print("There is a cat in here") # print a statement to screen
        return
    
    print("Nothing to see here")


# In[12]:


first_list = ['cat', 'dog', 'hamster', 42]

second_list = ['duck', 17, 'elk']


# In[13]:


are_there_cats(first_list)


# In[14]:


are_there_cats(second_list)


# ## 2.1.4 Scoping

# There are differences in how variables and names are accessed by your code based on where they are defined. 
# 
# Within this notebook any variables that have been defined outside of a function will be available to the rest of the notebook. At this point in the notebook, x has not been defined.

# In[15]:


x


# If we now define x and write and call a function in which uses it; the function can still access x, even if x isn't given as an argument.

# In[16]:


x = 5 # Define x now

def can_we_see_x():
    print(f"x = {x}")
    
can_we_see_x()


# However if we define y locally - in a function - we can access it from within that function:

# In[17]:


def can_we_see_y():
    y = 7 # Define y in the function
    print(f"x = {x}")
    print(f"y = {y}")
    
can_we_see_y()


# However y isn't accessible globally - that is it isn't available outside of the function in which it was defined

# In[18]:


y


# *Note for the two functions above we used syntax for building strings that contain the values of variables. You can read more about it [here](https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36) or in the official documentation for formatted string literals; [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings).*

# ## 2.1.5 Side effects

# Functions can do things to change their **mutable** arguments,
# so `return` is optional.
# 
# This is pretty awful style, in general, functions should normally be side-effect free.
# 
# Here is a contrived example of a function that makes plausible use of a side-effect

# In[19]:


def double_inplace(vec):
    vec[:] = [element * 2 for element in vec]


z = list(range(4))
double_inplace(z)
print(z)


# In[20]:


letters = ["a", "b", "c", "d", "e", "f", "g"]
letters[:] = []


# In this example, we're using `[:]` to access into the same list, and write it's data.
# 
#     vec = [element*2 for element in vec]
# 
# would just move a local label, not change the input.
# 
# See Module 1.5 - Memory and Containers for a refresher 

# But I'd usually just write this as a function which **returned** the output:

# In[21]:


def double(vec):
    return [element * 2 for element in vec]


# Let's remind ourselves of the behaviour for modifying lists in-place using `[:]` with a simple array:

# In[22]:


x = 5
x = 7
x = ["a", "b", "c"]
y = x


# In[23]:


x


# In[24]:


x[:] = ["Hooray!", "Yippee"]


# In[25]:


y


# ## 2.1.6 Unpacking arguments

# In[26]:


def arrow(before, after):
    return str(before) + " -> " + str(after)


arrow(1, 3)


# 
# If a function that takes multiple arguments is given an iterable object prepended with '*',
# each element of that object is taken in turn and used to fill the function's arguments one-by-one.
# 
# 
# 

# In[27]:


x = [1, -1]
arrow(*x)


# 
# 
# 
# This can be quite powerful:
# 
# 
# 

# In[28]:


charges = {"neutron": 0, "proton": 1, "electron": -1}
for particle in charges.items():
    print(arrow(*particle))


# ## 2.1.7 Sequence Arguments

# Similiarly, if a `*` is used in the **definition** of a function, multiple
# arguments are absorbed into a list **inside** the function:

# In[29]:


def doubler(*sequence):
    return [x * 2 for x in sequence]


# In[30]:


doubler(1, 2, 3)


# In[31]:


doubler(5, 2, "Wow!")


# ## 2.1.8 Keyword Arguments

# If two asterisks are used, named arguments are supplied inside the function as a dictionary:

# In[32]:


def arrowify(**args):
    for key, value in args.items():
        print(key + " -> " + value)


arrowify(neutron="n", proton="p", electron="e")


# These different approaches can be mixed:

# In[33]:


def somefunc(a, b, *args, **kwargs):
    print("A:", a)
    print("B:", b)
    print("args:", args)
    print("keyword args", kwargs)


# In[34]:


somefunc(1, 2, 3, 4, 5, fish="Haddock")

