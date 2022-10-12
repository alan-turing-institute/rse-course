#!/usr/bin/env python
# coding: utf-8

# # 7.4 Refactoring

# *Estimated time for this notebook: 20 minutes*

# Let's put ourselves in an scenario - that you've probably been in before. Imagine you are changing a large piece of legacy code that's not well structured, introducing many changes at once, trying to keep in your head all the bits and pieces that need to be modified to make it all work again. And suddenly, your officemate comes and ask you to go for coffee... and you've lost all track of what you had in your head and need to start again.
# 
# Instead of doing so, we could use a more robust approach to go from nasty ugly code to clean code in a safer way.

# ## Refactoring

# 
# To refactor is to:
# 
# * Make a change to the design of some software
# * Which improves the structure or readability
# * But which leaves the actual behaviour of the program completely unchanged.
# 
# 

# ## A word from the Master

# 
# > Refactoring is a controlled technique for improving the design of an existing code base. 
# Its essence is applying a series of small behavior-preserving transformations, each of which "too small to be worth doing". 
# However the cumulative effect of each of these transformations is quite significant. 
# By doing them in small steps you reduce the risk of introducing errors. 
# You also avoid having the system broken while you are carrying out the restructuring - 
# which allows you to gradually refactor a system over an extended period of time.
# 
# -- Martin Fowler [Refactoring](https://martinfowler.com/books/refactoring.html).
# 

# ## List of known refactorings

# 
# The next few sections will present some known refactorings.
# 
# We'll show before and after code, present any new coding techniques needed to do the refactoring, and describe [*code smells*](https://en.wikipedia.org/wiki/Code_smell): how you know you need to refactor.
# 

# ### Replace magic numbers with constants

# 💩**Smell**: Raw numbers appear in your code
# 
# **before:**
# 
# ```python
# data = [math.sin(x) for x in np.arange(0, 3.141, 3.141 / 100)]
# result = [0] * 100
# for i in range(100):
#     for j in range(i + 1, 100):
#         result[j] += data[i] * data[i - j] / 100
# ```
# 
# **after:**
# 
# ```python
# resolution = 100
# pi = 3.141
# data = [math.sin(x) for x in np.arange(0, pi, pi / resolution)]
# result = [0] * resolution
# for i in range(resolution):
#     for j in range(i + 1, resolution):
#         result[j] += data[i] * data[i - j] / resolution
# ```

# ### Replace repeated code with a function

# 💩**Smell**: Fragments of repeated code appear.
# 
# Fragment of model where some birds are chasing each other: if the angle of view of one can see the prey, then start hunting, and if the other see the predator, then start running away.
# 
# **before:**
# 
# ```python
# if abs(hawk.facing - starling.facing) < hawk.viewport:
#     hawk.hunting()
# 
# if abs(starling.facing - hawk.facing) < starling.viewport:
#     starling.flee()
# ```
# 
# **after:**
# 
# ```python
# def can_see(source, target):
#     return (source.facing - target.facing) < source.viewport
# 
# 
# if can_see(hawk, starling):
#     hawk.hunting()
# 
# if can_see(starling, hawk):
#     starling.flee()
# ```

# ### Change of variable name

# 💩**Smell**: Code needs a comment to explain what it is for.
# 
# **before:**
# 
# ```python
# z = find(x, y)
# if z:
#     ribe(x)
# ```
# 
# **after:**
# 
# ```python
# gene = subsequence(chromosome, start_codon)
# if gene:
#     transcribe(gene)
# ```

# ### Separate a complex expression into a local variable

# 💩**Smell**: An expression becomes long.
# 
# **before:**
# 
# ```python
# if color == "red" and fast or big and economy > 40 or price < 5000:
#     print("Vrroom!")
# ```
# 
# **after:**
# 
# ```python
# exciting = color == "red" and fast
# practical = big and economy > 40
# in_budget = price < 5000
# 
# if exciting or practical or in_budget:
#     print("Vrroom!")
# ```

# ### Replace loop with iterator

# 💩**Smell**: Loop variable is an integer from 1 to something.
# 
# **before:**
# 
# ```python
# total = 0
# for i in range(resolution):
#     total += data[i]
# ```
# 
# **after:**
# 
# ```python
# total = 0
# for value in data:
#     total += value
# ```

# ### Replace hand-written code with library code

# 💩**Smell**: It feels like surely someone else must have done this at some point.
# 
# **before:**
# 
# ```python
# xcoords = [start + i * step for i in range(int((end - start) / step))]
# ```
# 
# **after:**
# 
# ```python
# import numpy as np
# 
# xcoords = np.arange(start, end, step)
# ```
# 
# See [Numpy](http://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html),
#     [Pandas](http://pandas.pydata.org/).
# 

# ### Replace set of arrays with array of structures

# 💩**Smell**: A function needs to work corresponding indices of several arrays:
# 
# **before:**
# 
# ```python
# def can_see(i, source_angles, target_angles, source_viewports):
#     return abs(source_angles[i] - target_angles[i]) < source_viewports[i]
# ```
# 
# **after:**
# 
# ```python
# def can_see(source, target):
#     return (source["facing"] - target["facing"]) < source["viewport"]
# ```
# 
# Warning: this refactoring greatly improves readability but can make code slower,
# depending on memory layout. Be careful.

# ### Replace constants with a configuration file

# 💩**Smell**: You need to change your code file to explore different research scenarios.
# 
# **before:**

# In[1]:


flight_speed = 2.0  # mph
bounds = [0, 0, 100, 100]
turning_circle = 3.0  # m
bird_counts = {"hawk": 5, "starling": 500}


# **after:**

# In[2]:


get_ipython().run_cell_magic('writefile', 'config.yaml', 'bounds: [0, 0, 100, 100]\ncounts:\n    hawk: 5\n    starling: 500\nspeed: 2.0\nturning_circle: 3.0\n')


# In[3]:


import yaml

config = yaml.safe_load(open("config.yaml"))
print(config)


# 
# See [YAML](http://www.yaml.org/) and [PyYaml](http://pyyaml.org/),
# and [Python's os module](https://docs.python.org/3/library/os.html).
# 

# ### Replace global variables with function arguments

# 💩**Smell**: A global variable is assigned and then used inside a called function:
# 
# **before:**
# 
# ```python
# viewport = pi / 4
# 
# if hawk.can_see(starling):
#     hawk.hunt(starling)
# 
# 
# class Hawk:
#     def can_see(self, target):
#         return (self.facing - target.facing) < viewport
# ```
# 
# **after:**
# 
# ```python
# viewport = pi / 4
# if hawk.can_see(starling, viewport):
#     hawk.hunt(starling)
# 
# 
# class Hawk:
#     def can_see(self, target, viewport):
#         return (self.facing - target.facing) < viewport
# ```

# ### Merge neighbouring loops

# 💩**Smell**: Two neighbouring loops have the same for statement
# 
# **before:**
# 
# ```python
# for bird in birds:
#     bird.build_nest()
# 
# for bird in birds:
#     bird.lay_eggs()
# ```
# 
# **after:**
# 
# ```python
# for bird in birds:
#     bird.build_nest()
#     bird.lay_eggs()
# ```
# 
# Though there may be a case where all the nests need to be built before the birds can start laying eggs.

# ### Break a large function into smaller units

# 
# * 💩**Smell**: A function or subroutine no longer fits on a page in your editor.
# * 💩**Smell**: A line of code is indented more than three levels.
# * 💩**Smell**: A piece of code interacts with the surrounding code through just a few variables.
# 
# **before:**
# 
# ```python
# def do_calculation():
#     for predator in predators:
#         for prey in preys:
#             if predator.can_see(prey):
#                 predator.hunt(prey)
#             if predator.can_reach(prey):
#                 predator.eat(prey)
# ```
# 
# **after:**
# 
# ```python
# def do_calculation():
#     for predator in predators:
#         for prey in preys:
#             predate(predator, prey)
# 
# 
# def predate(predator, prey):
#     if predator.can_see(prey):
#         predator.hunt(prey)
#     if predator.can_reach(prey):
#         predator.eat(prey)
# ```

# ### Separate code concepts into files or modules

# - 💩**Smell**: You find it hard to locate a piece of code.
# - 💩**Smell**: You get a lot of version control conflicts.
# 
# **before:**

# In[4]:


class One:
    pass


class Two:
    def __init__():
        self.child = One()


# **after:**

# In[5]:


get_ipython().run_cell_magic('writefile', 'anotherfile.py', 'class One:\n    pass\n')


# In[6]:


from anotherfile import One


class Two:
    def __init__():
        self.child = One()


# ### Refactoring is a safe way to improve code

# 
# You may think you can see how to rewrite a whole codebase to be better.
# 
# However, you may well get lost halfway through the exercise.
# 
# By making the changes as small, reversible, incremental steps,
# you can reach your target design more reliably.
# 

# ### Tests and Refactoring

# 
# Badly structured code cannot be unit tested. There are no "units".
# 
# Before refactoring, ensure you have a robust regression test.
# 
# This will allow you to *Refactor with confidence*.
# 
# As you refactor, if you create any new units (functions, modules, classes),
# add new tests for them.
# 

# ### Refactoring Summary

# 
# * Replace magic numbers with constants
# * Replace repeated code with a function
# * Change of variable/function/class name
# * Replace loop with iterator
# * Replace hand-written code with library code
# * Replace set of arrays with array of structures
# * Replace constants with a configuration file
# * Replace global variables with function arguments
# * Break a large function into smaller units
# * Separate code concepts into files or modules
# 
# And many more...
# 
# Read [The Refactoring Book](https://martinfowler.com/books/refactoring.html).
# 
# 
# 
