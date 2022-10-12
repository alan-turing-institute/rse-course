#!/usr/bin/env python
# coding: utf-8

# # 1.3 Using Functions

# *Estimated time for this notebook: 20 minutes*

# ## 1.3.1 Calling functions

# We often want to do things to our objects that are more complicated than just assigning them to variables.

# In[1]:


len("pneumonoultramicroscopicsilicovolcanoconiosis")


# Here we have "called a function".

# The function `len` takes one input, and has one output. The output is the length of whatever the input was.

# Programmers also call function inputs "parameters" or, confusingly, "arguments".

# Here's another example:

# In[2]:


sorted("Python")


# Which gives us back a *list* of the letters in Python, sorted alphabetically (more specifically, according to their [Unicode order](https://www.ssec.wisc.edu/~tomw/java/unicode.html#x0000)).

# The input goes in brackets after the function name, and the output emerges wherever the function is used.

# So we can put a function call anywhere we could put a "literal" object or a variable. 

# In[3]:


len("Jim") * 8


# In[4]:


x = len("Mike")
y = len("Bob")
z = x + y


# In[5]:


print(z)


# ## 1.3.2 Using methods

# Objects come associated with a bunch of functions designed for working on objects of that type. We access these with a dot, just as we do for data attributes:

# In[6]:


"shout".upper()


# These are called methods. If you try to use a method defined for a different type, you get an error:

# In[7]:


x = 5


# In[8]:


type(x)


# In[9]:


x.upper()


# If you try to use a method that doesn't exist, you get an error:

# In[10]:


x.wrong


# Methods and properties are both kinds of **attribute**, so both are accessed with the dot operator.

# Objects can have both properties and methods:

# In[11]:


z = 1 + 5j


# In[12]:


z.real


# In[13]:


z.conjugate()


# In[14]:


z.conjugate


# ## 1.3.3 Functions are just a type of object!

# Now for something that will take a while to understand: don't worry if you don't get this yet, we'll
# look again at this in much more depth later in the course.
# 
# If we forget the (), we realise that a *method is just a property which is a function*!

# In[15]:


z.conjugate


# In[16]:


type(z.conjugate)


# In[17]:


somefunc = z.conjugate


# In[18]:


somefunc()


# Functions are just a kind of variable, and we can assign new labels to them:

# In[19]:


sorted([1, 5, 3, 4])


# In[20]:


magic = sorted


# In[21]:


type(magic)


# In[22]:


magic(["Technology", "Advanced"])


# ## 1.3.4 Getting help on functions and methods

# The 'help' function, when applied to a function, gives help on it!

# In[23]:


help(sorted)


# The 'dir' function, when applied to an object, lists all its attributes (properties and methods):

# In[24]:


dir("Hexxo")


# Most of these are confusing methods beginning and ending with __, part of the internals of python.

# Again, just as with error messages, we have to learn to read past the bits that are confusing, to the bit we want:

# In[25]:


"Hexxo".replace("x", "l")


# In[26]:


help("FIsh".replace)


# ## 1.3.5 Operators

# Now that we know that functions are a way of taking a number of inputs and producing an output, we should look again at
# what happens when we write:

# In[27]:


x = 2 + 3


# In[28]:


print(x)


# This is just a pretty way of calling an "add" function. Things would be more symmetrical if add were actually written
# 
#     x = +(2, 3)
#     
# Where '+' is just the name of the name of the adding function.

# In python, these functions **do** exist, but they're actually **methods** of the first input: they're the mysterious `__` functions we saw earlier (Two underscores.)

# In[29]:


x.__add__(7)


# We call these symbols, `+`, `-` etc, "operators".

# The meaning of an operator varies for different types:

# In[30]:


"Hello" + "Goodbye"


# In[31]:


[2, 3, 4] + [5, 6]


# Sometimes we get an error when a type doesn't have an operator:

# In[32]:


7 - 2


# In[33]:


[2, 3, 4] - [5, 6]


# The word "operand" means "thing that an operator operates on"!

# Or when two types can't work together with an operator:

# In[34]:


[2, 3, 4] + 5


# To do this, put:

# In[35]:


[2, 3, 4] + [5]


# Just as in Mathematics, operators have a built-in precedence, with brackets used to force an order of operations:

# In[36]:


print(2 + 3 * 4)


# In[37]:


print((2 + 3) * 4)


# *Supplementary material*: http://www.mathcs.emory.edu/~valerie/courses/fall10/155/resources/op_precedence.html
