#!/usr/bin/env python
# coding: utf-8

# # 9.5 Performance scaling for containers and algorithms

# *Estimated time for this notebook: 15 minutes*

# We've seen that NumPy arrays are really useful. Why wouldn't we always want to use them for data which is all the same type?

# In[1]:


from timeit import repeat

import numpy as np
from matplotlib import pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# Let's look at appending data into a NumPy array, compared to a plain Python list: 

# In[2]:


def time_append_to_ndarray(count):
    # the function repeat does the same that the `%timeit` magic
    # but as a function; so we can plot it.
    return repeat(
        "np.append(before, [0])",
        f"import numpy as np; before=np.ndarray({count})",
        number=10000,
    )


# In[3]:


def time_append_to_list(count):
    return repeat("before.append(0)", f"before = [0] * {count}", number=10000)


# In[4]:


counts = np.arange(1, 100000, 10000)


def plot_time(function, counts, title=None):
    plt.plot(counts, list(map(function, counts)))
    plt.ylim(bottom=0)
    plt.ylabel("seconds")
    plt.xlabel("array size")
    plt.title(title or function.__name__)


# In[5]:


plot_time(time_append_to_list, counts)


# In[6]:


plot_time(time_append_to_ndarray, counts)


# Adding an element to a Python list is way faster! Also, it seems that adding an element to a Python list is independent of the length of the list, but it's not so for a NumPy array.

# How do they perform when accessing an element in the middle?

# In[7]:


def time_lookup_middle_element_in_list(count):
    test_list = [0] * count
    middle_position = count // 2

    def totime():
        return test_list[middle_position]

    return repeat(totime, number=10000)


# In[8]:


def time_lookup_middle_element_in_ndarray(count):
    test_array = np.ndarray(count)
    middle_position = count // 2

    def totime():
        return test_array[middle_position]

    return repeat(totime, number=10000)


# In[9]:


plot_time(time_lookup_middle_element_in_list, counts)


# In[10]:


plot_time(time_lookup_middle_element_in_ndarray, counts)


# Both scale well for accessing the middle element.

# What about inserting at the beginning?
# 
# If we want to insert an element at the beginning of a Python list we can do:

# In[11]:


x = list(range(5))
x


# In[12]:


x[0:0] = [-1]
x


# In[13]:


def time_insert_to_list(count):
    return repeat("before[0:0] = [0]", f"before = [0] * {count}", number=10000)


# In[14]:


plot_time(time_insert_to_list, counts)


# `list` performs **badly** for insertions at the beginning!

# There are containers in Python that work well for insertion at the start:

# In[15]:


from collections import deque


# In[16]:


def time_insert_to_deque(count):
    return repeat(
        "before.appendleft(0)",
        f"from collections import deque; before = deque([0] * {count})",
        number=10000,
    )


# In[17]:


plot_time(time_insert_to_deque, counts)


# But looking up in the middle scales badly:

# In[18]:


def time_lookup_middle_element_in_deque(count):
    test_deque = deque([0] * count)
    middle_position = count // 2

    def totime():
        return test_deque[middle_position]

    return repeat(totime, number=10000)


# In[19]:


plot_time(time_lookup_middle_element_in_deque, counts)


# What is going on here?

# Arrays are stored as contiguous memory. Anything which changes the length of the array requires the whole array to be copied elsewhere in memory.

# This copy takes time proportional to the array size.

# ![Adding an element to an array - memory representation](./array_memory.svg)

# The Python `list` type is **also** an array, but it is allocated with **extra memory**. Only when that memory is exhausted is a copy needed.

# ![Adding an element to a list - memory representation](list_memory.svg)

# If the extra memory is typically the size of the current array, a copy is needed every 1/N appends, and costs N to make, so **on average** copies are cheap. We call this **amortized constant time**. 
# 
# This makes it fast to look up values in the middle. However, it may also use more space than is needed.

# The deque type works differently: each element contains a pointer to the next. Inserting elements is therefore very cheap, but looking up the Nth element requires traversing N such pointers.

# ![Adding an element to a deque - memory representation](deque_memory.svg)

# ## Dictionary performance

# For another example, let's consider the performance of a dictionary versus a couple of other ways in which we could implement an associative array.

# In[20]:


class evildict:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, akey):
        for key, value in self.data:
            if key == akey:
                return value
        raise KeyError()


# If we have an evil dictionary of N elements, how long would it take - on average - to find an element?

# In[21]:


eric = [["Name", "Eric Idle"], ["Job", "Comedian"], ["Home", "London"]]


# In[22]:


eric_evil = evildict(eric)


# In[23]:


eric_evil["Job"]


# In[24]:


eric_dict = dict(eric)


# In[25]:


eric_evil["Job"]


# In[26]:


x = ["Hello", "License", "Fish", "Eric", "Pet", "Halibut"]


# In[27]:


sorted(x, key=lambda el: el.lower())


# What if we created a dictionary where we bisect the search?

# In[28]:


from bisect import bisect_left


class sorteddict:
    def __init__(self, data):
        self.data = sorted(data, key=lambda x: x[0])
        self.keys = list(map(lambda x: x[0], self.data))

    def __getitem__(self, akey):
        loc = bisect_left(self.keys, akey)

        if loc != len(self.data):
            return self.data[loc][1]

        raise KeyError()


# In[29]:


eric_sorted = sorteddict(eric)


# In[30]:


eric_sorted["Job"]


# In[31]:


def time_dict_generic(ttype, count):
    keys = list(range(count))
    values = [0] * count
    data = ttype(list(zip(keys, values)))

    def totime():
        return data[keys[count // 2]]

    return repeat(totime, number=10000)


# In[32]:


def time_dict(count):
    return time_dict_generic(dict, count)


def time_sorted(count):
    return time_dict_generic(sorteddict, count)


def time_evil(count):
    return time_dict_generic(evildict, count)


# In[33]:


plot_time(time_sorted, counts, title="sorted")


# We can't really see what's going on here for the sorted example as there's too much noise, but theoretically we should get **logarithmic** asymptotic performance. We write this down as $O(\ln N)$. This doesn't mean there isn't also a constant term, or a term proportional to something that grows slower (such as $\ln(\ln N)$): we always write down just the term that is dominant for large $N$. We saw before that `list` is $O(1)$ for appends, $O(N)$ for inserts. Numpy's `array` is $O(N)$ for appends.

# In[34]:


counts = np.arange(1, 1000, 100)
plot_time(time_evil, counts, title="evil")


# The simple check-each-in-turn solution is $O(N)$ - linear time.

# In[35]:


counts = np.arange(1, 100000, 10000)
plot_time(time_dict, counts, title="dict")


# Python's built-in dictionary is, amazingly, O(1): the time is **independent** of the size of the dictionary.
# 
# This uses a miracle of programming called the _Hash Table_:
# you can learn more about [these issues at this video from Harvard University](https://www.youtube.com/watch?v=h2d9b_nEzoA). This material is pretty advanced, but, I think, really interesting!

# Optional exercise: determine what the asymptotic peformance for the Boids model in terms of the number of Boids. Make graphs to support this. Bonus: how would the performance scale with the number of dimensions?
