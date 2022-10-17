#!/usr/bin/env python
# coding: utf-8

# # 3.3 NumPy

# *Estimated time to complete this notebook: 20 minutes*

# ## 3.3.1 The Scientific Python Trilogy

# Why is Python so popular for research work?

# MATLAB has typically been the most popular "language of technical computing", with strong built-in support for efficient numerical analysis with matrices (the *mat* in MATLAB is for Matrix, not Maths), and plotting.

# Other dynamic languages have cleaner, more logical syntax (Ruby, Haskell)

# But Python users developed three critical libraries, matching the power of MATLAB for scientific work:

# * Matplotlib, the plotting library created by [John D. Hunter](https://en.wikipedia.org/wiki/John_D._Hunter)
# * NumPy, a fast matrix maths library created by [Travis Oliphant](https://www.anaconda.com/people/travis-oliphant)
# * IPython, the precursor of the notebook, created by [Fernando Perez](http://fperez.org)

# By combining a plotting library, a matrix maths library, and an easy-to-use interface allowing live plotting commands
# in a persistent environment, the powerful capabilities of MATLAB were matched by a free and open toolchain.

# Furthermore, tools such as Pandas and SciPy are built on, extend, or utilise these libraries

# We've learned about Matplotlib and IPython in this course already. NumPy is the last part of the trilogy.

# ## 3.3.2 Limitations of Python Lists

# The normal Python List is just one dimensional. To make a matrix, we have to nest Python lists:

# In[1]:


x = [list(range(5)) for N in range(5)]


# In[2]:


x


# In[3]:


x[2][2]


# Applying an operation to every element is a pain:

# In[4]:


x + 5


# In[5]:


[[elem + 5 for elem in row] for row in x]


# Common useful operations like transposing a matrix or reshaping a 10 by 10 matrix into a 20 by 5 matrix are not easy to code in raw Python lists.

# ## 3.3.3 The NumPy array

# NumPy's array type represents a multidimensional matrix $M_{i,j,k...n}$

# The NumPy array seems at first to be just like a list:

# In[6]:


import numpy as np

my_array = np.array(range(5))


# In[7]:


my_array


# In[8]:


my_array[2]


# In[9]:


for element in my_array:
    print("Hello" * element)


# We can also see our first weakness of NumPy arrays versus Python lists:

# In[10]:


my_array.append(4)


# For NumPy arrays, you typically don't change the data size once you've defined your array,
# whereas for Python lists, you can do this efficiently. However, you get back lots of goodies in return...

# ## 3.3.4 Elementwise Operations

# But most operations can be applied element-wise automatically!

# In[11]:


my_array + 2


# These "vectorized" operations are very fast: (see [here](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) for more information on the `%%timeit` magic)

# In[12]:


import numpy as np

big_list = range(10000)
big_array = np.arange(10000)


# In[13]:


get_ipython().run_cell_magic('timeit', '', '[x**2 for x in big_list]\n')


# In[14]:


get_ipython().run_cell_magic('timeit', '', 'big_array**2\n')


# ## 3.3.5 Arange and linspace

# NumPy has two easy methods for defining floating-point evenly spaced arrays:

# In[15]:


x = np.arange(0, 10, 0.1)  # Start, stop, step size


# Note that using non-integer step size does not work with Python lists:

# In[16]:


y = list(range(0, 10, 0.1))


# Similarly, we can quickly an evenly spaced range of a known size (eg. for graph plotting):

# In[17]:


import math

values = np.linspace(0, math.pi, 100)  # Start, stop, number of steps


# In[18]:


values


# NumPy comes with 'vectorised' versions of common functions which work element-by-element when applied to arrays:

# In[19]:


from matplotlib import pyplot as plt

plt.plot(values, np.sin(values))


# So we don't have to use awkward list comprehensions when using these.

# ## 3.3.6 Multi-Dimensional Arrays

# NumPy's true power comes from multi-dimensional arrays:

# In[20]:


np.zeros([3, 4, 2])  # 3 arrays with 4 rows and 2 columns each


# Unlike a list-of-lists in Python, we can reshape arrays:

# In[21]:


x = np.array(range(40))
x


# In[22]:


y = x.reshape([4, 5, 2])  # 4 Arrays - 5 Rows - 2 Columns
y


# And index multiple columns at once:

# In[23]:


y[3, 2, 1]


# Including selecting on inner axes while taking all from the outermost:

# In[24]:


y[:, 2, 1]


# And subselecting ranges:

# In[25]:


y[2:, :1, :]  # Last 2 axes, 1st row, all columns


# And [transpose](https://en.wikipedia.org/wiki/Transpose) arrays:

# In[26]:


y.transpose()


# You can get the dimensions of an array with `shape`

# In[27]:


y.shape  # 4 Arrays - 5 Rows - 2 Columns


# In[28]:


y.transpose().shape  # 2 Arrays - 5 Rows - 4 Columns


# Some numpy functions apply by default to the whole array, but can be chosen to act only on certain axes:

# In[29]:


x = np.arange(12).reshape(4, 3)
x


# In[30]:


x.mean(1)  # Mean along the second axis, leaving the first.


# In[31]:


x.mean(0)  # Mean along the first axis, leaving the second.


# In[32]:


x.mean()  # mean of all axes


# ## 3.3.7 Array Datatypes

# A Python `list` can contain data of mixed type:

# In[33]:


x = ["hello", 2, 3.4]


# In[34]:


type(x[2])


# In[35]:


type(x[1])


# A NumPy array always contains just one datatype:

# In[36]:


np.array(x)


# NumPy will choose the least-generic-possible datatype that can contain the data:

# In[37]:


y = np.array([2, 3.4])


# In[38]:


y


# You can access the array's `dtype`, or check the type of individual elements:

# In[39]:


y.dtype


# In[40]:


type(y[0])


# In[41]:


z = np.array([3, 4, 5])
z


# In[42]:


type(z[0])


# The results are, when you get to know them, fairly obvious string codes for datatypes: 
#     NumPy supports all kinds of datatypes beyond the python basics.

# NumPy will convert python type names to dtypes:

# In[43]:


x = [2, 3.6, 7.2, 0]


# In[44]:


int_array = np.array(x, dtype=int)


# In[45]:


int_array


# In[46]:


int_array.dtype


# In[47]:


float_array = np.array(x, dtype=float)


# In[48]:


float_array


# In[49]:


float_array.dtype

