#!/usr/bin/env python
# coding: utf-8

# # Module 08

# ### Solution to Exercise 1: Iterators and generators

# In[1]:


# Using __iter__ and __next__
class range2:
    def __init__(self, max_counter):
        self.max_counter = max_counter
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.max_counter:
            counter = self.counter
            self.counter += 1
            return counter
        else:
            raise StopIteration


# In[2]:


# Testing it
print(range2(10))
print(tuple(range2(10)))
for i in range2(10):
    print(i)


# In[3]:


# Using yield
def range3(max_counter):
    counter = 0
    while counter < max_counter:
        yield counter
        counter += 1


# In[4]:


# Testing it
print(range3(10))
print(tuple(range3(10)))
for i in range3(10):
    print(i)


# ### Solution to Exercise 2: Operator Overloading

# In[5]:


class DataLoader:
    def __init__(self):
        pass

    def process(self):
        print("I am loading some data")


class DataCleaner:
    def __init__(self):
        pass

    def process(self):
        print("I am cleaning some data")


# In[6]:


class Pipeline:
    def __init__(self):
        self.modules = []

    # Add __iadd__ function to overload '+='
    def __iadd__(self, module):
        self.modules.append(module)
        return self

    def process(self):
        print("I'm a pipeline, don't do anything much by myself")
        for module in self.modules:
            module.process()


# In[7]:


p = Pipeline()
p += DataLoader()
p += DataCleaner()
p.process()


# In[ ]:




