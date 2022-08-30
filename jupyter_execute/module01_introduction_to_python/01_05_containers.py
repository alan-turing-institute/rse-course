#!/usr/bin/env python
# coding: utf-8

# # 1.5 Containers
# *Estimated time to complete this notebook: 10 minutes*

# ## 1.5.1 Checking for containment.

# The `list` we saw is a container type: its purpose is to hold other objects. We can ask python whether or not a
# container contains a particular item:

# In[1]:


"Dog" in ["Cat", "Dog", "Horse"]


# In[2]:


"Bird" in ["Cat", "Dog", "Horse"]


# In[3]:


2 in range(5)


# In[4]:


99 in range(5)


# ## 1.5.2 Mutability

# A list can be modified: (is mutable)

# In[5]:


name = "James Philip John Hetherington".split(" ")
print(name)


# In[6]:


name[0] = "Dr"
name[1:3] = ["Griffiths-"]
name.append("PhD")

print(" ".join(name))


# ## 1.5.3 Tuples

# A `tuple` is an immutable sequence. It is like a list, except it cannot be changed. It is defined with round brackets.

# In[7]:


x = (0,)
type(x)


# In[8]:


my_tuple = ("Hello", "World")
my_tuple[0] = "Goodbye"


# In[9]:


type(my_tuple)


# `str` is immutable too:

# In[10]:


fish = "Hake"
fish[0] = "R"


# But note that container reassignment is moving a label, **not** changing an element:

# In[11]:


fish = "Rake"  ## OK!


# *Supplementary material*: Try the [online memory visualiser](http://www.pythontutor.com/visualize.html#code=name+%3D++%22James+Philip+John+Hetherington%22.split%28%22+%22%29%0A%0Aname%5B0%5D+%3D+%22Dr%22%0Aname%5B1%3A3%5D+%3D+%5B%22Griffiths-%22%5D%0Aname.append%28%22PhD%22%29%0A%0Aname+%3D+%22Bilbo+Baggins%22&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0) for this one.

# ## 1.5.4 Memory and containers

# 
# The way memory works with containers can be important:
# 
# 
# 

# In[12]:


x = list(range(3))
x


# In[13]:


y = x
y


# In[14]:


z = x[0:3]
y[1] = "Gotcha!"


# In[15]:


x


# In[16]:


y


# In[17]:


z


# In[18]:


z[2] = "Really?"


# In[19]:


x


# In[20]:


y


# In[21]:


z


# *Supplementary material*: This one works well at the [memory visualiser](http://www.pythontutor.com/visualize.html#code=x+%3D+%5B%22What's%22,+%22Going%22,+%22On%3F%22%5D%0Ay+%3D+x%0Az+%3D+x%5B0%3A3%5D%0A%0Ay%5B1%5D+%3D+%22Gotcha!%22%0Az%5B2%5D+%3D+%22Really%3F%22&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0).

# The explanation: While `y` is a second label on the *same object*, `z` is a separate object with the same data. Writing `x[:]` creates a new list containing all the elements of `x` (remember: `[:]` is equivalent to `[0:<last>]`). This is the case whenever we take a slice from a list, not just when taking all the elements with `[:]`.
# 
# The difference between `y=x` and `z=x[:]` is important!

# Nested objects make it even more complicated:

# In[22]:


x = [["a", "b"], "c"]
y = x
z = x[0:2]


# In[23]:


x[0][1] = "d"
z[1] = "e"


# In[24]:


x


# In[25]:


y


# In[26]:


z


# Try the [visualiser](http://www.pythontutor.com/visualize.html#code=x%3D%5B%5B'a','b'%5D,'c'%5D%0Ay%3Dx%0Az%3Dx%5B0%3A2%5D%0A%0Ax%5B0%5D%5B1%5D%3D'd'%0Az%5B1%5D%3D'e'&mode=display&origin=opt-frontend.js&cumulative=false&heapPrimitives=true&textReferences=false&py=2&rawInputLstJSON=%5B%5D&curInstr=0) again.
# 
# *Supplementary material*: The copies that we make through slicing are called *shallow copies*: we don't copy all the objects they contain, only the references to them. This is why the nested list in `x[0]` is not copied, so `z[0]` still refers to it. It is possible to actually create copies of all the contents, however deeply nested they are - this is called a *deep copy*. Python provides methods for that in its standard library, in the `copy` module. You can read more about that, as well as about shallow and deep copies, in the [library reference](https://docs.python.org/3/library/copy.html).

# ## 1.5.5 Identity vs Equality
# 
# Having the same data is different from being the same actual object
# in memory:

# In[27]:


[1, 2] == [1, 2]


# In[28]:


[1, 2] is [1, 2]


# The == operator checks, element by element, that two containers have the same data. 
# The `is` operator checks that they are actually the same object.

# But, and this point is really subtle, for immutables, the python language might save memory by reusing a single instantiated copy. This will always be safe.

# In[29]:


"Hello" == "Hello"


# In[30]:


"Hello" is "Hello"


# This can be useful in understanding problems like the one above:

# In[31]:


x = range(3)
y = x
z = x[:]


# In[32]:


x == y


# In[33]:


x is y


# In[34]:


x == z


# In[35]:


x is z

