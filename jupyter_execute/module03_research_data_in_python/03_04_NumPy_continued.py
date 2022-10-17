#!/usr/bin/env python
# coding: utf-8

# # 3.4 Advanced NumPy

# *Estimated time to complete this notebook: 20 minutes*

# ## 3.4.1 Recap

# In the previous section we introduced numpy array that represents a multidimensional matrix $M_{i,j,k...n}$. Which, among other things, allows for vectorised versions of common functions

# In[1]:


import numpy as np


# ## 3.4.2 Broadcasting

# This is another really powerful feature of NumPy.

# By default, array operations are element-by-element:

# In[2]:


np.arange(5) * np.arange(5)


# If we multiply arrays with non-matching shapes we get an error:

# In[3]:


np.arange(5) * np.arange(6)


# In[4]:


np.zeros([2, 3]) * np.zeros([2, 4])


# In[5]:


m1 = np.arange(100).reshape([10, 10])


# In[6]:


m2 = np.arange(100).reshape([10, 5, 2])


# In[7]:


m1 + m2


# Arrays must match in **all** dimensions in order to be compatible:

# In[8]:


np.ones([3, 3]) * np.ones([3, 3])  # Note elementwise multiply, *not* matrix multiply.


# In[9]:


m3 = np.arange(9).reshape([3, 3])
m3


# In[10]:


m4 = np.arange(9, 18).reshape([3, 3])
m4


# In[11]:


m3 * m4  # Note elementwise multiply, *not* matrix multiply.


# **Except**, that if one array has any Dimension 1, then the data is **REPEATED** to match the other.

# In[12]:


col = np.arange(10).reshape([10, 1])
col


# In[13]:


row = col.transpose()
row


# In[14]:


col.shape  # "Column Vector"


# In[15]:


row.shape  # "Row Vector"


# In[16]:


row + col


# In[17]:


10 * row + col


# This works for arrays with more than one unit dimension. 

# ## 3.4.3 Another example

# In[18]:


x = np.array([1, 2]).reshape(1, 2)
x


# In[19]:


y = np.array([3, 4, 5]).reshape(3, 1)
y


# In[20]:


result = x + y
result.shape


# In[21]:


result


# What numpy is doing:
# 
# <img src="broadcasting.png" alt="Numpy broadcasting example" style="width: 250px;"/>

# ## 3.4.4 Newaxis

# Broadcasting is very powerful, and numpy allows indexing with `np.newaxis` to temporarily create new one-long dimensions on the fly.

# In[22]:


import numpy as np

x = np.arange(10).reshape(2, 5)
y = np.arange(8).reshape(2, 2, 2)


# In[23]:


x


# In[24]:


y


# In[25]:


x_dash = x[:, :, np.newaxis, np.newaxis]
x_dash.shape


# In[26]:


y_dash = y[:, np.newaxis, :, :]
y_dash.shape


# In[27]:


y_dash


# In[28]:


res = x_dash * y_dash


# In[29]:


res.shape


# In[30]:


np.sum(res)


# Note that `newaxis` works because a $3 \times 1 \times 3$ array and a $3 \times 3$ array contain the same data,
# differently shaped:

# In[31]:


threebythree = np.arange(9).reshape(3, 3)
threebythree


# In[32]:


threebythree[:, np.newaxis, :]


# ## 3.4.5 Dot Products using broadcasting

# NumPy multiply is element-by-element, not a dot-product:

# In[33]:


a = np.arange(9).reshape(3, 3)
a


# In[34]:


b = np.arange(3, 12).reshape(3, 3)
b


# In[35]:


a * b


# We can use what we've learned about the algebra of broadcasting and newaxis to get a dot-product, (matrix inner product).
# 
# First we add new axes to $A$ and $B$:

# In[36]:


a[:, :, np.newaxis].shape


# In[37]:


b[np.newaxis, :, :].shape


# Now we use broadcasting to generate $A_{ij}B_{jk}$ as a 3-d matrix:

# In[38]:


a[:, :, np.newaxis] * b[np.newaxis, :, :]


# Then we sum over the middle, $j$ axis, [which is the 1-axis of three axes numbered (0,1,2)] of this 3-d matrix. Thus we generate $\Sigma_j A_{ij}B_{jk}$.

# In[39]:


(a[:, :, np.newaxis] * b[np.newaxis, :, :]).sum(1)


# Or if you prefer:

# In[40]:


(a.reshape(3, 3, 1) * b.reshape(1, 3, 3)).sum(1)


# We can see that the broadcasting concept gives us a powerful and efficient way to express many linear algebra operations computationally.

# ## 3.4.6 Dot Products using numpy functions

# However, as the dot-product is a common operation, `numpy` has a built in function:

# In[41]:


np.dot(a, b)


# This can also be written as:

# In[42]:


a.dot(b)


# If you are using `Python 3.5` or later, a dedicated matrix multiplication operator has been added, allowing you to do the following:

# In[43]:


a @ b


# ## 3.4.7 Record Arrays

# These are a special array structure designed to match the CSV "Record and Field" model. It's a very different structure
# from the normal NumPy array, and different fields *can* contain different datatypes. We saw this when we looked at CSV files:

# In[44]:


x = np.arange(50).reshape([10, 5])


# In[45]:


record_x = x.view(
    dtype={"names": ["col1", "col2", "another", "more", "last"], "formats": [int] * 5}
)


# In[46]:


record_x


# Record arrays can be addressed with field names like they were a dictionary:

# In[47]:


record_x["col1"]


# Indeed we can use these methods when parsing CSV files instead of using Pandas.

# ## 3.4.8 Logical arrays, masking, and selection

# Numpy defines operators like == and < to apply to arrays *element by element*:

# In[48]:


x = np.zeros([3, 4])
x


# In[49]:


y = np.arange(-1, 2)[:, np.newaxis] * np.arange(-2, 2)[np.newaxis, :]
y


# In[50]:


iszero = x == y
iszero


# A logical array can be used to select elements from an array:

# In[51]:


y[np.logical_not(iszero)]


# Although when printed, this comes out as a flat list, if assigned to, the *selected elements of the array are changed!*

# In[52]:


y[iszero] = 5


# In[53]:


y


# ## 3.4.9 Numpy memory

# Numpy memory management can be tricksy:

# In[54]:


x = np.arange(5)
y = x[:]


# In[55]:


y[2] = 0
x


# It does **not** behave like lists!

# In[56]:


x = list(range(5))
y = x[:]


# In[57]:


y[2] = 0
x


# We must use `np.copy` to force separate memory. Otherwise NumPy tries its hardest to make slices be *views* on data.

# Now, this has all been very theoretical, but let's go through a practical example, and see how powerful NumPy can be.
