#!/usr/bin/env python
# coding: utf-8

# # Classroom Exercises

# **List of exercises and estimated completion times**
# 
# [1a - Python Libraries](#Exercise-1a-Python-Libraries) *5 minutes*
# 
# [1b - Using Functions](#Exercise-1b-Using-Functions) *10 minutes*
# 
# [1c - Operators](#Exercise-1c-Operators) *10 minutes*
# 
# [1d - Maze Model](#Exercise-1d-Maze-Model) *25 minutes*
# 
# [1e - The Maze Population](#Exercise-1e-The-Maze-Population) *10 minutes*
# 

# ### Exercise 1a Python Libraries
# *Relevant Sections: 1.0.2*
# 
# The directory that contains this workbook also contains a `Python` file titled `draw_infinity.py`. Import it to a notebook and make the figure in the same way as `eight` was drawn in section 1.0.2

# ### Exercise 1b Using Functions
# *Relevant Sections: 1.3.1 to 1.3.5*
# 
# Try to find the operator or function you need to calculate the following (the easiest way might be an internet search).
# 
# What is 2 to the power 15?
# 
# Convert `"It was the best of times"` to uppercase.
# 
# Sort the list `[10, 9, 0, 20, 8, 2, 30, 7, 3]`.
# 
# What is 100! ? (That is, what is the factorial of 100?) Hint: the `factorial` function is in the `math` library

# ### Exercise 1c Operators
# *Relevant Sections: 1.3.5, 1.4.3*
# 
# Which of the operators `+`, `-`, `*`, and `/` do something useful with the lists `[1, 10, 100]` and `[5, 4, 7]`?
# 
# What happens if you apply the operators `+`, `-`, `*`, `/` to a list and a number?
# 
# What about a string and a string?

# ### Exercise 1d Maze Model
# *Relevant Sections: 1.6.1, 1.7.1*
# 
# Work with a partner to design a data structure to represent a maze using dictionaries and lists.
# 
# * Each place in the maze has a name, which is a string.
# * Each place in the maze has one or more people currently standing at it, by name.
# * Each place in the maze has a maximum capacity of people that can fit in it.
# * From each place in the maze, you can go from that place to a few other places, using a direction like 'up', 'north', or 'sideways'
# 
# Create an example instance, in a notebook, of a simple structure for your maze:
# 
# * The front room can hold 2 people. James is currently there. You can go outside to the garden, or upstairs to the bedroom, or north to the kitchen.
# * From the kitchen, you can go south to the front room. It fits 1 person.
# * From the garden you can go inside to front room. It fits 3 people. Sue is currently there.
# * From the bedroom, you can go downstairs to the front room. You can also jump out of the window to the garden. It fits 2 people.
# 
# Make sure that your model:
# 
# * Allows empty rooms
# * Allows you to jump out of the upstairs window, but not to fly back up.
# * Allows rooms which people can't fit in.
# 
# 
# ```python
# house = [ "Your answer here" ]
# ```
# or
# ```python
# house = { "Your answer here" }
# ```

# ### Exercise 1e The Maze Population
# *Relevant Sections: 1.6.1, 1.7.1, 1.9.1, 1.9.2*
# 
# Take your maze data structure. Write a program to count the total number of people in the maze, and also determine the total possible occupants.
