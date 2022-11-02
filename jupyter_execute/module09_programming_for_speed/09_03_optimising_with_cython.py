#!/usr/bin/env python
# coding: utf-8

# # 9.3 Optimising with Cython

# *Estimated time for this notebook: 20 minutes*

# Cython can be viewed as an extension of Python where variables and functions are annotated with extra information, in particular types. The resulting Cython source code will be compiled into optimized C or C++ code, and thereby yielding substantial speed-up of slow Python code. In other words, Cython provides a way of writing Python with comparable performance to that of C/C++.

# ## Start coding in Cython

# Cython code must, unlike Python, be compiled. This happens in the following stages:
# 
# * The cython code in `.pyx` file will be translated to a `C` file.
# * The `C` file will be compiled by a C compiler into a shared library, which will be directly loaded into Python. 
# 
# In a Jupyter notebook, everything is a lot easier. One needs only to load the Cython extension (`%load_ext Cython`) at the beginning and put `%%cython` mark in front of cells of Cython code. Cells with Cython mark will be treated as a `.pyx` code and consequently, compiled into C. 
# 
# For details, please see [Building Cython Code](http://docs.cython.org/src/quickstart/build.html).
# 

# ### Pure python Mandelbrot set:

# In[1]:


xmin = -1.5
ymin = -1.0
xmax = 0.5
ymax = 1.0
resolution = 300
xstep = (xmax - xmin) / resolution
ystep = (ymax - ymin) / resolution
xs = [(xmin + (xmax - xmin) * i / resolution) for i in range(resolution)]
ys = [(ymin + (ymax - ymin) * i / resolution) for i in range(resolution)]


# In[2]:


def mandel(position, limit=50):
    value = position
    while abs(value) < 2:
        limit -= 1
        value = value**2 + position
        if limit < 0:
            return 0
    return limit


# ### Compiled by Cython:

# In[3]:


get_ipython().run_line_magic('load_ext', 'Cython')


# In[4]:


get_ipython().run_cell_magic('cython', '', '\ndef mandel_cython(position, limit=50):\n    value = position\n    while abs(value) < 2:\n        limit -= 1\n        value = value ** 2 + position\n        if limit < 0:\n            return 0\n    return limit\n')


# Let's verify the result

# In[5]:


data_python = [[mandel(complex(x, y)) for x in xs] for y in ys]
data_cython = [[mandel_cython(complex(x, y)) for x in xs] for y in ys]


# In[6]:


from matplotlib import pyplot as plt

plt.set_cmap("cividis")  # use a CVD-friendly palette

f, axarr = plt.subplots(1, 2)
axarr[0].imshow(data_python, interpolation="none", extent=[xmin, xmax, ymin, ymax])
axarr[0].set_title("Pure Python")
axarr[1].imshow(data_cython, interpolation="none", extent=[xmin, xmax, ymin, ymax])
axarr[1].set_title("Cython")


# In[7]:


get_ipython().run_line_magic('timeit', '[[mandel(complex(x,y)) for x in xs] for y in ys] # pure python')
get_ipython().run_line_magic('timeit', '[[mandel_cython(complex(x,y)) for x in xs] for y in ys] # cython')


# We have improved the performance of a factor of 1.5 by just using the Cython compiler, **without changing the code**!

# ### Cython with C Types
# But we can do better by telling Cython what C data type we would use in the code. Note we're not actually writing C, we're writing Python with C types.

# _typed variable_

# In[8]:


get_ipython().run_cell_magic('cython', '', 'def var_typed_mandel_cython(position, limit=50):\n    cdef double complex value # typed variable\n    value = position\n    while abs(value) < 2:\n        limit -= 1\n        value = value**2 + position\n        if limit < 0:\n            return 0\n    return limit\n')


# _typed function + typed variable_

# In[9]:


get_ipython().run_cell_magic('cython', '', 'cpdef call_typed_mandel_cython(double complex position, int limit=50): # typed function\n    cdef double complex value # typed variable\n    value = position\n    while abs(value)<2:\n        limit -= 1\n        value = value**2 + position\n        if limit < 0:\n            return 0\n    return limit\n')


# performance of one number:

# In[10]:


# pure python
get_ipython().run_line_magic('timeit', 'a = mandel(complex(0, 0))')


# In[11]:


# primitive cython
get_ipython().run_line_magic('timeit', 'a = mandel_cython(complex(0, 0))')


# In[12]:


# cython with C type variable
get_ipython().run_line_magic('timeit', 'a = var_typed_mandel_cython(complex(0, 0))')


# In[13]:


# cython with typed variable + function
get_ipython().run_line_magic('timeit', 'a = call_typed_mandel_cython(complex(0, 0))')


# ### Cython with numpy ndarray
# You can use NumPy from Cython exactly the same as in regular Python, but by doing so you are losing potentially high speedups because Cython has support for fast access to NumPy arrays. 

# In[14]:


import numpy as np

ymatrix, xmatrix = np.mgrid[ymin:ymax:ystep, xmin:xmax:xstep]
values = xmatrix + 1j * ymatrix


# In[15]:


get_ipython().run_cell_magic('cython', '', 'import numpy as np\ncimport numpy as np \n\ncpdef numpy_cython_1(np.ndarray[double complex, ndim=2] position, int limit=50): \n    cdef np.ndarray[long,ndim=2] diverged_at\n    cdef double complex value\n    cdef int xlim\n    cdef int ylim\n    cdef double complex pos\n    cdef int steps\n    cdef int x, y\n\n    xlim = position.shape[1]\n    ylim = position.shape[0]\n    diverged_at = np.zeros([ylim, xlim], dtype=int)\n    for x in xrange(xlim):\n        for y in xrange(ylim):\n            steps = limit\n            value = position[y,x]\n            pos = position[y,x]\n            while abs(value) < 2 and steps >= 0:\n                steps -= 1\n                value = value**2 + pos\n            diverged_at[y,x] = steps\n  \n    return diverged_at\n')


# Note the double import of numpy: the standard numpy module and a Cython-enabled version of numpy that ensures fast indexing of and other operations on arrays. **Both import statements are necessary** in code that uses numpy arrays. The new thing in the code above is declaration of arrays by np.ndarray.

# In[16]:


get_ipython().run_line_magic('timeit', 'data_python = [mandel(value) for row in values for value in row] # pure python')


# In[17]:


get_ipython().run_line_magic('timeit', 'data_cython = [call_typed_mandel_cython(value) for row in values for value in row] # typed cython')


# In[18]:


get_ipython().run_line_magic('timeit', 'data_numpy_cython = numpy_cython_1(values) # ndarray')


# `numpy` has a built-in function called `np.vectorize` to take a function that runs on a single object and return a function that runs on arrays of that object.
# Note that this is no faster than explicitly writing the vectorised version of the function yourself, as we can see below.

# In[19]:


numpy_cython_2 = np.vectorize(call_typed_mandel_cython)


# In[20]:


get_ipython().run_line_magic('timeit', 'numpy_cython_2(values) #  vectorize')


# We got approximately a 40x total speed up from `mandel` to `numpy_cython_1`.

# ### Calling C functions from Cython
# 
# #### Example: compare `sin()` from Python and C library

# In[21]:


get_ipython().run_cell_magic('cython', '', 'import math\ncpdef py_sin():\n    cdef int x\n    cdef double y\n    for x in range(1e7):\n        y = math.sin(x)\n')


# In[22]:


get_ipython().run_cell_magic('cython', '', 'from libc.math cimport sin as csin # import from C library\ncpdef c_sin():\n    cdef int x\n    cdef double y\n    for x in range(1e7):\n        y = csin(x)\n')


# In[23]:


get_ipython().run_line_magic('timeit', '[math.sin(i) for i in range(int(1e7))] # python')


# In[24]:


get_ipython().run_line_magic('timeit', 'py_sin()                                # cython call python library')


# In[25]:


get_ipython().run_line_magic('timeit', 'c_sin()                                 # cython call C library')

