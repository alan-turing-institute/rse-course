#!/usr/bin/env python
# coding: utf-8

# # NumPy

# ## The Scientific Python Trilogy

# Why is Python so popular for research work?

# MATLAB has typically been the most popular "language of technical computing", with strong built-in support for efficient numerical analysis with matrices (the *mat* in MATLAB is for Matrix, not Maths), and plotting.

# Other dynamic languages have cleaner, more logical syntax (Ruby, Haskell)

# But Python users developed three critical libraries, matching the power of MATLAB for scientific work:

# * Matplotlib, the plotting library created by [John D. Hunter](https://en.wikipedia.org/wiki/John_D._Hunter)
# * NumPy, a fast matrix maths library created by [Travis Oliphant](https://www.anaconda.com/people/travis-oliphant)
# * IPython, the precursor of the notebook, created by [Fernando Perez](http://fperez.org)

# By combining a plotting library, a matrix maths library, and an easy-to-use interface allowing live plotting commands
# in a persistent environment, the powerful capabilities of MATLAB were matched by a free and open toolchain.

# We've learned about Matplotlib and IPython in this course already. NumPy is the last part of the trilogy.

# ## Limitations of Python Lists

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

# ## The NumPy array

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

# ## Elementwise Operations

# But most operations can be applied element-wise automatically!

# In[11]:


my_array + 2


# These "vectorized" operations are very fast: (see [here](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-timeit) for more information on the `%%timeit` magic)

# In[12]:


import numpy as np

big_list = range(10000)
big_array = np.arange(10000)


# In[13]:


get_ipython().run_cell_magic('timeit', '', '[x ** 2 for x in big_list]')


# In[14]:


get_ipython().run_cell_magic('timeit', '', 'big_array ** 2')


# ## Arange and linspace

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


get_ipython().run_line_magic('matplotlib', 'inline')

from matplotlib import pyplot as plt

plt.plot(values, np.sin(values))


# So we don't have to use awkward list comprehensions when using these.

# ## Multi-Dimensional Arrays

# NumPy's true power comes from multi-dimensional arrays:

# In[20]:


np.zeros([3, 4, 2])  # 3 arrays with 4 rows and 2 columns each


# Unlike a list-of-lists in Python, we can reshape arrays:

# In[21]:


x = np.array(range(40))
x


# In[22]:


y = x.reshape([4, 5, 2])
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


y.shape


# In[28]:


y.transpose().shape


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


# ## Array Datatypes

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


# ## Broadcasting

# This is another really powerful feature of NumPy.

# By default, array operations are element-by-element:

# In[50]:


np.arange(5) * np.arange(5)


# If we multiply arrays with non-matching shapes we get an error:

# In[51]:


np.arange(5) * np.arange(6)


# In[52]:


np.zeros([2, 3]) * np.zeros([2, 4])


# In[53]:


m1 = np.arange(100).reshape([10, 10])


# In[54]:


m2 = np.arange(100).reshape([10, 5, 2])


# In[55]:


m1 + m2


# Arrays must match in all dimensions in order to be compatible:

# In[56]:


np.ones([3, 3]) * np.ones([3, 3])  # Note elementwise multiply, *not* matrix multiply.


# **Except**, that if one array has any Dimension 1, then the data is **REPEATED** to match the other.

# In[57]:


col = np.arange(10).reshape([10, 1])
col


# In[58]:


row = col.transpose()
row


# In[59]:


col.shape  # "Column Vector"


# In[60]:


row.shape  # "Row Vector"


# In[61]:


row + col


# In[62]:


10 * row + col


# This works for arrays with more than one unit dimension. 

# ## Another example

# In[63]:


x = np.array([1, 2]).reshape(1, 2)
x


# In[64]:


y = np.array([3, 4, 5]).reshape(3, 1)
y


# In[65]:


result = x + y
result.shape


# In[66]:


result


# What numpy is doing:
# 
# <img src="broadcasting.png" alt="Numpy broadcasting example" style="width: 250px;"/>

# ## Newaxis

# Broadcasting is very powerful, and numpy allows indexing with `np.newaxis` to temporarily create new one-long dimensions on the fly.

# In[67]:


import numpy as np

x = np.arange(10).reshape(2, 5)
y = np.arange(8).reshape(2, 2, 2)


# In[68]:


x


# In[69]:


y


# In[70]:


x_dash = x[:, :, np.newaxis, np.newaxis]
x_dash.shape


# In[71]:


y_dash = y[:, np.newaxis, :, :]
y_dash.shape


# In[72]:


res = x_dash * y_dash


# In[73]:


res.shape


# In[74]:


np.sum(res)


# Note that `newaxis` works because a $3 \times 1 \times 3$ array and a $3 \times 3$ array contain the same data,
# differently shaped:

# In[75]:


threebythree = np.arange(9).reshape(3, 3)
threebythree


# In[76]:


threebythree[:, np.newaxis, :]


# ## Dot Products using broadcasting

# NumPy multiply is element-by-element, not a dot-product:

# In[77]:


a = np.arange(9).reshape(3, 3)
a


# In[78]:


b = np.arange(3, 12).reshape(3, 3)
b


# In[79]:


a * b


# We can what we've learned about the algebra of broadcasting and newaxis to get a dot-product, (matrix inner product).
# 
# First we add new axes to $A$ and $B$:

# In[80]:


a[:, :, np.newaxis].shape


# In[81]:


b[np.newaxis, :, :].shape


# Now we use broadcasting to generate $A_{ij}B_{jk}$ as a 3-d matrix:

# In[82]:


a[:, :, np.newaxis] * b[np.newaxis, :, :]


# Then we sum over the middle, $j$ axis, [which is the 1-axis of three axes numbered (0,1,2)] of this 3-d matrix. Thus we generate $\Sigma_j A_{ij}B_{jk}$.

# In[83]:


(a[:, :, np.newaxis] * b[np.newaxis, :, :]).sum(1)


# Or if you prefer:

# In[84]:


(a.reshape(3, 3, 1) * b.reshape(1, 3, 3)).sum(1)


# We can see that the broadcasting concept gives us a powerful and efficient way to express many linear algebra operations computationally.

# ## Dot Products using numpy functions

# However, as the dot-product is a common operation, `numpy` has a built in function:

# In[85]:


np.dot(a, b)


# This can also be written as:

# In[86]:


a.dot(b)


# If you are using `Python 3.5` or later, a dedicated matrix multiplication operator has been added, allowing you to do the following:

# In[87]:


a @ b


# ## Record Arrays

# These are a special array structure designed to match the CSV "Record and Field" model. It's a very different structure
# from the normal NumPy array, and different fields *can* contain different datatypes. We saw this when we looked at CSV files:

# In[88]:


x = np.arange(50).reshape([10, 5])


# In[89]:


record_x = x.view(
    dtype={"names": ["col1", "col2", "another", "more", "last"], "formats": [int] * 5}
)


# In[90]:


record_x


# Record arrays can be addressed with field names like they were a dictionary:

# In[91]:


record_x["col1"]


# We've seen these already when we used NumPy's CSV parser.

# ## Logical arrays, masking, and selection

# Numpy defines operators like == and < to apply to arrays *element by element*:

# In[92]:


x = np.zeros([3, 4])
x


# In[93]:


y = np.arange(-1, 2)[:, np.newaxis] * np.arange(-2, 2)[np.newaxis, :]
y


# In[94]:


iszero = x == y
iszero


# A logical array can be used to select elements from an array:

# In[95]:


y[np.logical_not(iszero)]


# Although when printed, this comes out as a flat list, if assigned to, the *selected elements of the array are changed!*

# In[96]:


y[iszero] = 5


# In[97]:


y


# ## Numpy memory

# Numpy memory management can be tricksy:

# In[98]:


x = np.arange(5)
y = x[:]


# In[99]:


y[2] = 0
x


# It does **not** behave like lists!

# In[100]:


x = list(range(5))
y = x[:]


# In[101]:


y[2] = 0
x


# We must use `np.copy` to force separate memory. Otherwise NumPy tries its hardest to make slices be *views* on data.

# Now, this has all been very theoretical, but let's go through a practical example, and see how powerful NumPy can be.
