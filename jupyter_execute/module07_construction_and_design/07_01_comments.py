#!/usr/bin/env python
# coding: utf-8

# # 7.1 Comments

# *Estimated time for this notebook: 15 minutes*

# ## Why comment?

# 
# * You're writing code for people, as well as computers.
# * Comments can help you build code, by representing your design
# * Comments explain subtleties in the code which are not obvious from the syntax
# * Comments explain *why* you wrote the code the way you did

# ## The Pseudocode Programming Process

# Start by writing a program in all comments:

# In[1]:


# To find the largest element in an array
# Set up a variable to track the largest so far
# Loop over every element
# - For each element, is it bigger than the previous biggest?
# - If so, it's the new biggest
# At the end, the biggest so far, is the biggest overall


# One by one, replace these with the equivalent in code

# In[2]:


# To find the largest element in an array
def largest(data):
    # Set up a variable to track the largest so far
    biggest_so_far = 0
    # Loop over every element
    for datum in data:
        # For each element, is it bigger than the previous biggest?
        if datum > biggest_so_far:
            # If so, it's the new biggest
            biggest_so_far = datum
    # At the end, the biggest so far, is the biggest overall
    return biggest_so_far


# In[3]:


largest([0, 1, 3, 6, 2, 5, 3])


# Then, remove only those comments that are now extraneous (see below for examples of extraneous comments)

# In[4]:


# To find the largest element in an array
def largest(data):
    # Set up a variable to track the largest so far
    biggest_so_far = 0
    for datum in data:
        # For each element, is it bigger than the previous biggest?
        # If so, it's the new biggest
        if datum > biggest_so_far:
            biggest_so_far = datum
    return biggest_so_far


# ## Who are you writing for?
# 
# * By far the most likely person who will read your code/comments is yourself, maybe in a week's time, or maybe in six months time.
# * Second most likely person in most cases, is someone in your team, or someone else who will probably have a roughly similar level of expertise, and be trying to do a similar thing.
# * Write comments with this in mind - try to help the person reading the code to understand _what_ you did and _why_.

# ## Prefer "in language" comments to comments proper, if we can

# _More_ comments doesn't necessarily mean _better_ - here are some examples of comments that don't really help the reader understand the code any better. If we can, it's nice to find ways to put our description of what the code does *inside* the code, instead of as comments. Then, when the code changes, the 'comments' stay in sync, beause they're part of the code.
# 
# For example, we can use a variable name or a function name, to hold what would have been in a comment. Here, instead of a comment and a one-word function name, we've made a longer function name.
# 
# ```python
# def largest_element_in_array(data):
#     # Set up a variable to track the largest so far
#     biggest_so_far = 0
#     for datum in data:
#         # For each element, is it bigger than the previous biggest?
#         # If so, it's the new biggest
#         if datum > biggest_so_far:
#             biggest_so_far = datum
#     return biggest_so_far
# ```

# ## Comments which are obvious

# Try to use comments to explain why the code does, not just repeat the code in a comment.
# 
# ```python
# counter = counter + 1  # Increment the counter
# for element in array:  # Loop over elements
#     pass
# ```

# ## Comments which could be replaced by better style

# The following piece of code could be a part of a game to move a turtle in a certain direction, with a particular angular velocity and step size.
# 
# ```python
# for i in range(len(agt)):  # for each agent
#     agt[i].theta += ws[i]  # Increment the angle of each agent
#     # by its angular velocity
#     agt[i].x += r * sin(agt[i].theta)  # Move the agent by the step-size
#     agt[i].y += r * cos(agt[i].theta)  # r in the direction indicated
# ```
# 
# we have used comments to make the code readable.
# 
# 
# Why not make the code readable instead?
# 
# ```python
# for agent in agents:
#     agent.turn()
#     agent.move()
# 
# 
# class Agent:
#     def turn(self):
#         self.direction += self.angular_velocity
# 
#     def move(self):
#         self.x += Agent.step_length * sin(self.direction)
#         self.y += Agent.step_length * cos(self.direction)
# ```
# 
# This is probably better. We are using the name of the functions (_i.e._ `turn`, `move`) instead of comments. Therefore, we've got _self-documenting_ code.
# 

# ## Comments which belong in an issue tracker
# 
# ```python
# x.clear()  # Code crashes here sometimes
# 
# 
# class Agent:
#     pass
#     # TODO: Implement pretty-printer method
# ```
# 
# BUT comments that reference issues in the tracker can be good.
# 
# E.g.
# 
# ```python
# if x.safe_to_clear():  # Guard added as temporary workaround for #32
#     x.clear()
# ```
# 
# is OK. And platforms like GitHub will create a link to it when browsing the code.

# ## Comments which only make sense to the author today
# 
# ```python
# agent.turn()  # Turtle Power!
# agent.move()
# agents[:] = []  # Shredder!
# ```

# ## Comments which are unpublishable
# 
# ```python
# # Stupid supervisor made me write this code
# # So I did it while very very drunk.
# ```

# ## Good commenting: pedagogical comments

# 
# Code that *is* good style, but you're not familiar with, or 
# that colleagues might not be familiar with
# 
# 
# ```python
# # This is how you define a decorator in python
# # See https://wiki.python.org/moin/PythonDecorators
# def double(decorated_function):
#     # Here, the result function calls the decorated_function
#     # twice, first on the entry input and then again on the 
#     # output of that
#     # the decorated function
#     def result_function(entry):
#         return decorated_function(decorated_function(entry))
# 
#     # The returned result is a function
#     return result_function
# 
# 
# @double
# def try_me_twice():
#     pass
# ```

# ## Great commenting: reasons and definitions

# 
# Comments which explain coding definitions or reasons for programming choices.
# 
# ```python
# def __init__(self):
#     self.angle = 0  # clockwise from +ve y-axis
#     nonzero_indices = []  # Use sparse model as memory constrained
# ```

# ## Are comments always helpful?

# Some authors argue that comments can be dangerous, as they can disincentivise 
# us from trying harder to use variable names and function names to discribe the code:

# > The proper use of comments is to compensate for our failure to express yourself in code. Note that I used the word failure. I meant it. Comments are always failures.
# -- Robert Martin, Clean Code

# This is definitely taking things too far, but there's a little grain of truth in it: 
