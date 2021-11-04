#!/usr/bin/env python
# coding: utf-8

# # Optimising Mandelbrot

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


xmin = -1.5
ymin = -1.0
xmax = 0.5
ymax = 1.0
resolution = 300
xstep = (xmax - xmin) / resolution
ystep = (ymax - ymin) / resolution
xs = [(xmin + (xmax - xmin) * i / resolution) for i in range(resolution)]
ys = [(ymin + (ymax - ymin) * i / resolution) for i in range(resolution)]


# In[3]:


def mandel1(position, limit=50):
    value = position
    while abs(value) < 2:
        limit -= 1
        value = value ** 2 + position
        if limit < 0:
            return 0
    return limit


# In[4]:


data1 = [[mandel1(complex(x, y)) for x in xs] for y in ys]


# ## Many Mandelbrots

# Let's compare our naive python implementation which used a list comprehension, taking 662ms, with the following:

# In[5]:


get_ipython().run_cell_magic('timeit', '', 'data2 = []\nfor y in ys:\n    row = []\n    for x in xs:\n        row.append(mandel1(complex(x, y)))\n    data2.append(row)')


# In[6]:


data2 = []
for y in ys:
    row = []
    for x in xs:
        row.append(mandel1(complex(x, y)))
    data2.append(row)


# Interestingly, not much difference. I would have expected this to be slower, due to the normally high cost of **appending** to data.

# In[7]:


from matplotlib import pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')
plt.imshow(data2, interpolation="none")


# We ought to be checking if these results are the same by comparing the values in a test, rather than re-plotting. This is cumbersome in pure Python, but easy with NumPy, so we'll do this later.

# Let's try a pre-allocated data structure:

# In[8]:


data3 = [[0 for i in range(resolution)] for j in range(resolution)]


# In[9]:


get_ipython().run_cell_magic('timeit', '', 'for j, y in enumerate(ys):\n    for i, x in enumerate(xs):\n        data3[j][i] = mandel1(complex(x, y))')


# In[10]:


for j, y in enumerate(ys):
    for i, x in enumerate(xs):
        data3[j][i] = mandel1(complex(x, y))


# In[11]:


plt.imshow(data3, interpolation="none")


# Nope, no gain there. 

# Let's try using functional programming approaches:

# In[12]:


get_ipython().run_cell_magic('timeit', '', 'data4 = []\nfor y in ys:\n    bind_mandel = lambda x: mandel1(complex(x, y))\n    data4.append(list(map(bind_mandel, xs)))')


# In[13]:


data4 = []
for y in ys:
    bind_mandel = lambda x: mandel1(complex(x, y))
    data4.append(list(map(bind_mandel, xs)))


# In[14]:


plt.imshow(data4, interpolation="none")


# That was a tiny bit slower.

# So, what do we learn from this? Our mental image of what code should be faster or slower is often wrong, or doesn't make much difference. The only way to really improve code performance is empirically, through measurements.
