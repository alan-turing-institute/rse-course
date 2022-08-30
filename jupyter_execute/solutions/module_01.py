#!/usr/bin/env python
# coding: utf-8

# # Module 1

# **Exercise 1a**

# In[1]:


import draw_infinity
image = draw_infinity.make_figure()


# **Exercise 1b**

# In[2]:


#What is 2 to the power 15?
import math as m

print(2**15)
print(m.pow(2,15))
print("-----------")


#Convert `"It was the best of times"` to uppercase.
target = "It was the best of times"
print(target.upper())
print("It was the best of times".upper())
print("-----------")


#Sort the list `[10, 9, 0, 20, 8, 2, 30, 7, 3]`.
target = [10, 9, 0, 20, 8, 2, 30, 7, 3]
print(sorted(target)) # Returns a new list that is sorted
target.sort()  # N/B .sort() modifes the original list
print(target) 
print("-----------")


#What is 100! ? (That is, what is the factorial of 100?) Hint: the `factorial` function is in the `math` library m
print(m.factorial(100))

# Could do it my hand too but there are functions to do it in the math (and other) libraries
answer = 1
for i in range(1, 100):
    answer *= i
    
print(answer)


# A note about `sorted` and `sort`. 
# 
# ```python
# sorted(target)
# ```
# returns a **new list** that is sorted
# 
# ```python
# target.sort()
# ```
# 
# modifies the original list.
# If we look at their positions in memory we can verify this:

# In[3]:


example_list = [3, 8, 1, 0, 5, 8, 9, 1, 1, 5]
print(f"Example list = {example_list}")
print(hex(id(example_list))) # Where the example list is stored
print("")
new_list = sorted(example_list)
print(f"New list     = {new_list}")
print(hex(id(new_list))) # Where the new list is stored
print(f"Example list = {example_list}")
print(hex(id(example_list))) # Where the example list is stored
print("")
example_list.sort()
print(f"Example list = {example_list}")
print(hex(id(example_list))) # Where the (sorted) example list is stored


# We can see that the example list is in the same place as it was before, but now it is sorted

# **Exercise 1c**

# In[4]:


# Which of the operators `+`, `-`, `*`, and `/` do something useful with the lists `[1, 10, 100]` and `[5, 4, 7]`?
a = [1, 10, 100]
b = [5, 4, 7]
print(a+b)
# all others not allowed
print("")

# What happens if you apply the operators `+`, `-`, `*`, `/` to a list and a number?
c = [1, 2, 3, 4, 'five']
d = 2
print(c*d)
# all others not allowed
print("")


# What about a string and a string?
e = "string-1"
f = "string-2"
print(e + f)
# all others not allowed


# **Exercise 1d**

# Something with a similar structure to this:

# In[5]:


house = {
    "living": {
        "exits": {"north": "kitchen", "outside": "garden", "upstairs": "bedroom"},
        "people": ["James"],
        "capacity": 2,
    },
    "kitchen": {"exits": {"south": "living"}, "people": [], "capacity": 1},
    "garden": {"exits": {"inside": "living"}, "people": ["Sue"], "capacity": 3},
    "bedroom": {
        "exits": {"downstairs": "living", "jump": "garden"},
        "people": [],
        "capacity": 1,
    },
}


# **Exercise 1e**

# We can count the occupants and capacity like this:

# In[6]:


capacity = 0
occupancy = 0
for name, room in house.items():
    capacity += room["capacity"]
    occupancy += len(room["people"])
print(f"House can fit {capacity} people, and currently has: {occupancy}.")


# As a side note, note how we included the values of `capacity` and `occupancy` in the last line. This is a handy syntax for building strings that contain the values of variables. You can read more about it [here](https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36) or in the official documentation for formatted string literals; [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#tut-f-strings).
