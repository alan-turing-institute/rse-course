#!/usr/bin/env python
# coding: utf-8

# *Estimated time for this notebook: 20 minutes*

# Cython can be viewed as an extension of Python where variables and functions are annotated with extra information, in particular types. The resulting Cython source code will be compiled into optimized C or C++ code, which can potentially speed up slow Python code. In other words, Cython provides a way of writing Python with comparable performance to that of C/C++.

# ## 9.3.0 How to Build Cython Code

# Cython code must, unlike Python, be compiled. This happens in the following stages:
# 
# * The cython code in `.pyx` file will be translated to a `C` file.
# * The `C` file will be compiled by a C compiler into a shared library, which will be directly loaded into Python. 
# 
# If you're writing `.py` files, you use the `cythonize` command in your terminal.
# In a Jupyter notebook, everything is a lot easier. One needs only to load the Cython extension (`%load_ext Cython`) at the beginning and use `%%cython` cell magic. Cells starting with `%%cython` will be treated as a `.pyx` code and, consequently, compiled.
# 
# For details, please see [Building Cython Code](http://docs.cython.org/src/quickstart/build.html).

# ## 9.3.1 Compiling a Pure Python Function

# We'll copy our pure Python `mandel()` function from the earlier notebook and redefine our real and imaginary inputs.

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


def mandel(constant, max_iterations=50):
    """Computes the values of the series for up to a maximum number of iterations.

    The function stops when the absolute value of the series surpasses 2 or when it reaches the maximum
    number of iterations.

    Returns the number of iterations.
    """

    value = 0

    counter = 0
    while counter < max_iterations:
        if abs(value) > 2:
            break

        value = (value * value) + constant

        counter = counter + 1

    return counter


assert mandel(0) == 50
assert mandel(3) == 1
assert mandel(0.5) == 5


# We will cythonise our function without adding any type hints.

# In[3]:


get_ipython().run_line_magic('load_ext', 'Cython')


# In[4]:


get_ipython().run_cell_magic('cython', '', '\ndef mandel_cython():\n    value = 0\n')


# In[5]:


mandel_cython()


# In[6]:


get_ipython().run_cell_magic('cython', '', '\ndef mandel_cython(constant, max_iterations=50):\n    """Computes the values of the series for up to a maximum number of iterations. \n    \n    The function stops when the absolute value of the series surpasses 2 or when it reaches the maximum \n    number of iterations.\n    \n    Returns the number of iterations.\n    """\n    \n    value = 0\n\n    counter = 0\n    while counter < max_iterations:\n        if abs(value) > 2:\n            break\n\n        value = (value * value) + constant\n\n        counter = counter + 1\n\n    return counter\n\n\nassert mandel_cython(0) == 50\nassert mandel_cython(3) == 1\nassert mandel_cython(0.5) == 5\n')


# Let's verify the result

# In[7]:


data_python = [[mandel(x + 1j * y) for x in xs] for y in ys]
data_cython = [[mandel_cython(x + 1j * y) for x in xs] for y in ys]


# In[8]:


from matplotlib import pyplot as plt

plt.set_cmap("cividis")  # use a CVD-friendly palette

f, axarr = plt.subplots(1, 2)
axarr[0].imshow(data_python, interpolation="none", extent=[xmin, xmax, ymin, ymax])
axarr[0].set_title("Pure Python")
axarr[0].set_ylabel("Imaginary")
axarr[0].set_xlabel("Real")
axarr[1].imshow(data_cython, interpolation="none", extent=[xmin, xmax, ymin, ymax])
axarr[1].set_title("Cython")
axarr[1].set_ylabel("Imaginary")
axarr[1].set_xlabel("Real")
f.tight_layout()


# In[9]:


get_ipython().run_cell_magic('timeit', '', '[[mandel(x + 1j * y) for x in xs] for y in ys]  # pure python\n')


# In[10]:


get_ipython().run_cell_magic('timeit', '', '[[mandel_cython(x + 1j * y) for x in xs] for y in ys]  # cython\n')


# We have improved the performance of a factor of 1.5 by just using the Cython compiler, **without changing the code**!

# ## 9.3.2 Cython with C Types
# 
# But we can do better by telling Cython what C data types we would use in the code. Note we're not actually writing C, we're writing Python with C types.

# ### The --annotate Option
# 
# If we pass the `--annotate`/`-a` option to `%%cython` then it will output information about the line-by-line cost of running your function. You can use this to target the most costly operations first or to estimate how much more optimising there is to do.

# In[11]:


get_ipython().run_cell_magic('cython', '--annotate', '\ndef mandel_cython(constant, max_iterations=50):\n    """Computes the values of the series for up to a maximum number of iterations. \n    \n    The function stops when the absolute value of the series surpasses 2 or when it reaches the maximum \n    number of iterations.\n    \n    Returns the number of iterations.\n    """\n    \n    value = 0\n\n    counter = 0\n    while counter < max_iterations:\n        if abs(value) > 2:\n            break\n\n        value = (value * value) + constant\n\n        counter = counter + 1\n\n    return counter\n')


# ### Typing Variables

# In[12]:


get_ipython().run_cell_magic('cython', '', '\ndef mandel_cython_var_typed(constant, max_iterations=50):\n    """Computes the values of the series for up to a maximum number of iterations. \n    \n    The function stops when the absolute value of the series surpasses 2 or when it reaches the maximum \n    number of iterations.\n    \n    Returns the number of iterations.\n    """\n    cdef double complex value # typed variable\n    value = 0\n\n    counter = 0\n    while counter < max_iterations:\n        if abs(value) > 2:\n            break\n\n        value = (value * value) + constant\n\n        counter = counter + 1\n\n    return counter\n\n\nassert mandel_cython_var_typed(0) == 50\nassert mandel_cython_var_typed(3) == 1\nassert mandel_cython_var_typed(0.5) == 5\n')


# In[13]:


get_ipython().run_cell_magic('timeit', '', '[[mandel_cython_var_typed(x + 1j * y) for x in xs] for y in ys]\n')


# ### Typing Function Parameters and Return Values

# In[14]:


get_ipython().run_cell_magic('cython', '', '\ncpdef int mandel_cython_func_typed(double complex constant, int max_iterations=50):\n    """Computes the values of the series for up to a maximum number of iterations. \n    \n    The function stops when the absolute value of the series surpasses 2 or when it reaches the maximum \n    number of iterations.\n    \n    Returns the number of iterations.\n    """\n    cdef double complex value # typed variable\n    value = 0\n\n    cdef int counter = 0\n    while counter < max_iterations:\n        if abs(value) > 2:\n            break\n\n        value = (value * value) + constant\n\n        counter = counter + 1\n\n    return counter\n\n\nassert mandel_cython_func_typed(0) == 50\nassert mandel_cython_func_typed(3) == 1\nassert mandel_cython_func_typed(0.5) == 5\n')


# In[15]:


get_ipython().run_cell_magic('timeit', '', '[[mandel_cython_func_typed(x + 1j * y) for x in xs] for y in ys]\n')


# ### Cython with numpy ndarray
# 
# You can use NumPy from Cython exactly the same as in regular Python, but by doing so you are losing potentially high speedups because Cython has support for fast access to NumPy arrays. 

# In[16]:


import numpy as np

cs_listcomp = [[(x + 1j * y) for x in xs] for y in ys]
cs = np.asarray(cs_listcomp)


# In[17]:


get_ipython().run_cell_magic('cython', '', "\nimport numpy as np\ncimport numpy as np \n\ncpdef int mandel_cython_numpy(np.ndarray[double complex, ndim=2] constants, int max_iterations=50): \n    cdef np.ndarray[long,ndim=2] diverged_at_count\n    cdef np.ndarray[double complex, ndim=2] value\n    cdef int counter\n\n    diverged_at_count = np.ones((constants.shape[0], constants.shape[1]), dtype=int)*max_iterations\n    value = np.zeros((constants.shape[0], constants.shape[1]), dtype=complex)\n    counter = 0\n    while counter < max_iterations:\n        value = value*value + constants\n        diverging = abs(value) > 2\n        \n        # Any positions which are:\n        # - diverging\n        # - haven't diverged before\n        # are diverging for the first time\n        first_diverged_this_time = np.logical_and(\n            diverging,\n            diverged_at_count == max_iterations\n        )\n        \n        # Update diverged_at_count for all positions which first diverged at this step\n        diverged_at_count[first_diverged_this_time] = counter\n        # Reset any divergent values to exactly 2\n        value[diverging] = 2\n        counter = counter + 1\n\n    return diverged_at_count\n\nassert mandel_cython_numpy(np.asarray([[0 + 1j*0]])) == np.asarray([[50]])\nassert mandel_cython_numpy(np.asarray([[4 + 1j*0]])) == np.asarray([[0]])\n")


# Note the double import of numpy:
# 
# - the standard numpy module
# - the Cython-enabled version of numpy that ensures fast indexing of and other operations on arrays.
# 
# **Both import statements are necessary** in code that uses numpy arrays. The new thing in the code above is declaration of arrays by np.ndarray.

# In[18]:


get_ipython().run_cell_magic('timeit', '', 'mandel_cython_numpy(cs)\n')

