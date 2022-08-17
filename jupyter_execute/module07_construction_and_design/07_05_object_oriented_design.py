#!/usr/bin/env python
# coding: utf-8

# # Design

# 
# ## Object-Oriented Design
# 
# In this session, we will finally discuss the thing most people think of when they refer to "Software Engineering": the deliberate *design* of software.
# We will discuss processes and methodologies for planned development of large-scale software projects: *Software Architecture*.
# 
# The software engineering community has, in large part, focused on an object-oriented approach to the design and development of large scale software systems.
# The basic concepts of object orientation are necessary to follow much of the software engineering conversation.
# 
# 
# ### Design processes
# 
# 
# In addition to object-oriented architecture, software engineers have focused on the development of processes for robust, reliable software development. 
# These codified ways of working hope to enable organisations to repeatably and reliably complete complex software projects in a way that minimises both development 
# and maintainance costs, and meets user requirements.
# 
# 
# ### Design and research
# 
# 
# Software engineering theory has largely been developed in the context of commercial software companies.
# 
# The extent to which the practices and processes developed for commercial software are applicable in a research context is itself an active area of research.
# 
# 
# 

# ## Recap of Object-Orientation

# ### Classes: User defined types
# 
# ```python
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# 
#     def grow_up(self):
#         self.age += 1
# 
# 
# terry = Person("Terry", 76)
# terry.home = "Colwyn Bay"
# ```
# 
# ⚠️ Notice, that in Python, you can add properties to an object once it's been defined. **Just because you can doesn't mean you should!**
# 

# ### Declaring a class 

# **Class:** A user-defined type
# 
# ```python
# class MyClass:
#     pass
# ```

# ### Object instances

# **Instance:** A particular object *instantiated* from a class.
# 
# ```python
# my_object = MyClass()
# ```

# ### Method

# **Method:** A function which is "built in" to a class
# 
# ```python
# class MyClass:
#     def someMethod(self, argument):
#         pass
# 
# 
# my_object = MyClass()
# my_object.someMethod(value)
# ```

# ### Constructor

# **Constructor:** A special method called when instantiating a new object
# 
# ```python
# class MyClass:
#     def __init__(self, argument):
#         pass
# 
# 
# my_object = MyClass(value)
# ```

# ### Member Variable

# **Member variable:** a value stored inside an instance of a class.

# In[1]:


class MyClass:
    def __init__(self):
        self.member = "Value"


my_object = MyClass()
print(my_object.member)


# ## Object refactorings

# ### Replace add-hoc structure with user defined classes

# 💩**Smell**: A data structure made of nested arrays and dictionaries becomes unwieldy.
# 
# **before:**
# 
# ```python
# from random import random
# 
# birds = [
#     {"position": random(), "velocity": random(), "type": kind} for kind in bird_types
# ]
# 
# average_position = average([bird["position"] for bird in birds])
# ```
# 
# **after:**
# 
# ```python
# class Bird:
#     def __init__(self, kind):
#         from random import random
# 
#         self.type = kind
#         self.position = random()
#         self.velocity = random()
# 
# 
# birds = [Bird(kind) for kind in bird_types]
# average_position = average([bird.position for bird in birds])
# ```

# ### Replace function with a method

# 💩**Smell**: A function is always called with the same kind of thing
# 
# **before:**
# 
# ```python
# def can_see(source, target):
#     return (source.facing - target.facing) < source.viewport
# 
# 
# if can_see(hawk, starling):
#     hawk.hunt()
# ```
# 
# **after:**
# 
# ```python
# class Bird:
#     def can_see(self, target):
#         return (self.facing - target.facing) < self.viewport
# 
# 
# if hawk.can_see(starling):
#     hawk.hunt()
# ```

# ### Replace method arguments with class members

# 💩**Smell**: A variable is nearly always used in arguments to 
# a class.
# 
# 
# **before:**
# 
# ```python
# class Person:
#     def __init__(self, genes):
#         self.genes = genes
# 
#     def reproduce_probability(self, age):
#         pass
# 
#     def death_probability(self, age):
#         pass
# 
#     def emigrate_probability(self, age):
#         pass
# ```
# 
# **after:**
# 
# ```python
# class Person:
#     def __init__(self, genes, age):
#         self.age = age
#         self.genes = genes
# 
#     def reproduce_probability(self):
#         pass
# 
#     def death_probability(self):
#         pass
# 
#     def emigrate_probability(self):
#         pass
# ```

# ### Replace global variable with class and member

# 💩**Smell**: A global variable is referenced by a few functions
# 
# **before:**
# 
# ```python
# name = "Terry Jones"
# birthday = [1, 2, 1942]
# today = [22, 11]
# 
# if today == birthday[0:2]:
#     print(f"Happy Birthday, {name}")
# else:
#     print("No birthday for you today.")
# ```
# 
# **after:**
# 
# ```python
# class Person:
#     def __init__(self, birthday, name):
#         self.birth_day = birthday[0]
#         self.birth_month = birthday[1]
#         self.birth_year = birthday[2]
#         self.name = name
# 
#     def check_birthday(self, today_day, today_month):
#         if not self.birth_day == today_day:
#             return False
#         if not self.birth_month == today_month:
#             return False
#         return True
# 
#     def greet_appropriately(self, today):
#         if self.check_birthday(*today):
#             print(f"Happy Birthday, {self.name}")
#         else:
#             print("No birthday for you.")
# 
# 
# john = Person([5, 5, 1943], "Michael Palin")
# john.greet_appropriately(today)
# ```

# ### Object Oriented Refactoring Summary

# 
# * Replace ad-hoc structure with a class
# * Replace function with a method
# * Replace method argument with class member
# * Replace global variable with class data
# 
# 
# 
