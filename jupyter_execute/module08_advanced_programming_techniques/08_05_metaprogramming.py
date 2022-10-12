#!/usr/bin/env python
# coding: utf-8

# # 8.5 Metaprogramming
# ⚠️ **Warning: Advanced Topic!** ⚠️

# *Estimated time for this notebook: 15 minutes*

# ## Metaprogramming globals

# 
# Consider a bunch of variables, each of which need initialising and incrementing:
# 
# 
# 

# In[1]:


bananas = 0
apples = 0
oranges = 0
bananas += 1
apples += 1
oranges += 1


# 
# 
# The right hand side of these assignments doesn't respect the DRY principle. We
# could of course define a variable for our initial value:
# 
# 
# 

# In[2]:


initial_fruit_count = 0
bananas = initial_fruit_count
apples = initial_fruit_count
oranges = initial_fruit_count


# 
# 
# However, this is still not as DRY as it could be: what if we wanted to replace
# the assignment with, say, a class constructor and a buy operation:
# 
# 
# 

# In[3]:


class Basket:
    def __init__(self):
        self.count = 0

    def buy(self):
        self.count += 1


bananas = Basket()
apples = Basket()
oranges = Basket()
bananas.buy()
apples.buy()
oranges.buy()


# 
# 
# We had to make the change in three places. Whenever you see a situation where a
# refactoring or change of design might require you to change the code in
# multiple places, you have an opportunity to make the code DRYer.
# 
# In this case, metaprogramming for incrementing these variables would involve
# just a loop over all the variables we want to initialise:
# 
# 
# 

# In[4]:


baskets = [bananas, apples, oranges]
for basket in baskets:
    basket.buy()


# 
# 
# However, this trick **doesn't** work for initialising a new variable:
# 
# 
# 

# In[5]:


baskets = [bananas, apples, oranges, kiwis]


# 
# 
# So can we declare a new variable programmatically? Given a list of the
# **names** of fruit baskets we want, initialise a variable with that name?
# 
# 
# 

# 
# 
# 
# Every module or class in Python, is, under the hood, a special
# dictionary storing the values in its **namespace**. `globals()` gives a reference to the attribute dictionary for the current module:
# 
# 
# 

# In[6]:


print("globals() is a\n", type(globals()))
print("\nWith these keys:\n", globals().keys())


# We can access variables via this dictionary:

# In[7]:


globals()["apples"]


# In[8]:


apples


# And create new variables by assigning to this dictionary:

# In[9]:


basket_names = ["bananas", "apples", "oranges", "kiwis"]

for name in basket_names:
    globals()[name] = Basket()


kiwis.count


# 
# 
# This is **metaprogramming**.
# 
# I would NOT recommend using it for an example as trivial as the one above. 
# A better, more Pythonic choice here would be to use a data structure to manage your set of fruit baskets:
# 
# 
# 

# In[10]:


baskets = {}
for name in basket_names:
    baskets[name] = Basket()

baskets["kiwis"].count


# 
# 
# Or even, using a dictionary comprehension:
# 
# 
# 

# In[11]:


baskets = {name: Basket() for name in baskets}
baskets["kiwis"].count


# 
# 
# Which is the nicest way to do this, I think. Code which feels like
# metaprogramming is needed to make it less repetitive can often instead be DRYed
# up using a refactored data structure, in a way which is cleaner and more easy
# to understand. Nevertheless, metaprogramming is worth knowing. 
# 

# ## Metaprogramming class attributes

# We can metaprogram the attributes of a **module** using the globals() function.
# 
# We will also want to be able to metaprogram a class, by accessing its attribute dictionary.
# 
# This will allow us, for example, to programmatically add members to a class.

# In[12]:


class Boring:
    pass


# If we are adding our own attributes, we can just do so directly:

# In[13]:


x = Boring()

x.name = "Michael"


# In[14]:


x.name


# And these turn up, as expected, in an attribute dictionary for the class:

# In[15]:


x.__dict__


# We can use `getattr` to access this special dictionary:

# In[16]:


getattr(x, "name")


# If we want to add an attribute given it's name as a string, we can use setattr:

# In[17]:


setattr(x, "age", 75)

x.age


# And we could do this in a loop to programmatically add many attributes.

# The real power of accessing the attribute dictionary comes when we realise that
# there is *very little difference* between member data and member functions.

# Now that we know, from our functional programming, that **a function is just a
# variable that can be *called* with `()`**, we can set an attribute to a function,
# and
# it becomes a member function!

# In[18]:


setattr(Boring, "describe", lambda self: f"{self.name} is {self.age}")


# In[19]:


x.describe()


# In[20]:


x.describe


# In[21]:


Boring.describe


# Note that we set this method as an attribute of the class, not the instance, so it is available to other instances of `Boring`:

# In[22]:


y = Boring()
y.name = "Terry"
y.age = 78


# In[23]:


y.describe()


# We can define a standalone function, and then **bind** it to the class. Its first argument automagically becomes
# `self`.

# In[24]:


def broken_birth_year(b_instance):
    import datetime

    current = datetime.datetime.now().year
    return current - b_instance.age


# In[25]:


Boring.birth_year = broken_birth_year


# In[26]:


x.birth_year()


# In[27]:


x.birth_year


# In[28]:


x.birth_year.__name__


# ## Metaprogramming function locals

# We can access the attribute dictionary for the local namespace inside a
# function with `locals()` but this *cannot be written to*.
# 
# Lack of safe
# programmatic creation of function-local variables is a flaw in Python.

# In[29]:


class Person:
    def __init__(self, name, age, job, children_count):
        for name, value in locals().items():
            if name == "self":
                continue
            print(f"Setting self.{name} to {value}")
            setattr(self, name, value)


# In[30]:


terry = Person("Terry", 78, "Screenwriter", 0)


# In[31]:


terry.name


# ## Metaprogramming warning!

# 
# Use this stuff **sparingly**!
# 
# The above example worked, but it produced Python code which is not particularly understandable.
# Remember, your objective when programming is to produce code which is **descriptive of what it does**.
# 
# The above code is **definitely** less readable, less maintainable and more error prone than:
# 
# 
# 

# In[32]:


class Person:
    def __init__(self, name, age, job, children_count):
        self.name = name
        self.age = age
        self.job = job
        self.children_count = children_count


# 
# 
# 
# Sometimes, metaprogramming will be **really** helpful in making non-repetitive
# code, and you should have it in your toolbox, which is why I'm teaching you it.
# But doing it all the time overcomplicated matters. We've talked a lot about the
# DRY principle, but there is another equally important principle:
# 
# > **KISS**: *Keep it simple, Stupid!*
# 
# Whenever you write code and you think, "Gosh, I'm really clever",you're
# probably *doing it wrong*. Code should be about clarity, not showing off.
# 
