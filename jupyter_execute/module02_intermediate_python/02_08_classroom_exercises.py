#!/usr/bin/env python
# coding: utf-8

# # 2.7 Classroom Exercises

# **List of exercises and estimated completion times**
# 
# [2a - Occupancy Dictionary](#Exercise-2a-Occupancy-Dictionary) *5 minutes*
# 
# [2b - Occupancy Dictionary Extension](#Exercise-2b-Occupancy-Dictionary-Extension) *5 minutes*
# 
# [2c - Functions](#Exercise-2c-Functions) *15 minutes*
# 
# [2d - Using Libraries](#Exercise-2d-Using-Libraries) *15 minutes*
# 
# [2e - Longitude and Latitude](#Exercise-2f-Longitude-and-Latitude) *15 minutes*
# 
# [2f - Defining Classes](#Exercise-2e-Defining-Classes) *45 minutes*
# 
# [2g - Longitude and Latitude Extension](#Exercise-2e-Longitude-and-Latitude-Extension) *10 minutes*

# ## Exercise 2a Occupancy Dictionary
# 
# *Relevant Sections: 2.0.2*

# In one of the module 1 exercises you designed a data structure to represent a maze using dictionaries and lists.
# 
# The answer to your initial maze model output might have looked similar to this:

# In[1]:


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


# Take this maze data structure.
# 
# First write an expression to print out a new dictionary, which holds, for each room, that room's capacity.
# 
# The output should look like:
# 
# ```python
# {"bedroom": 1, "garden": 3, "kitchen": 1, "living": 2}
# ```

# ## Exercise 2b Occupancy Dictionary Extension
# *Relevant Sections: 2.0.2 and 2.0.4*
# 
# Now, write a program to print out a new dictionary, which gives,for each room's name, the number of people in it.
# Don't add in a zero value in the dictionary for empty rooms.
# 
# The output should look similar to:
# 
# ```python
# {"garden": 1, "living": 1}
# ```

# ## Exercise 2c Functions
# *Relevant Sections: 2.1.1, 2.1.8, (2.0.2)*

# Write a function that will take the following input and return a list containing only even integers
# ```python
# (1, 1.99999999999, "three", 20/5, 5, 6, "sju", "8", 9, 10., 11, 12)
# ```
# 
# The call to your function could look something like this:
# 
# ```python
# my_function(1, 1.99999999999, "three", 20/5, 5, 6, "sju", "8", 9, 10., 11, 12)
# ```
# or
# ```python
# my_function(*inputs)
# ```

# ## Exercise 2d Using Libraries
# *Relevant Sections: 2.2.1*

# Investigate the similarities and differences between the responses (if any) from the `numpy`, `scipy`, `statistics`, and `math` modules to the following calculations:
# 
# 
# $\pi$
# 
# $log_{10}(n)$ where n is positive
# 
# $log_{10}(n)$ where n is negative
# 
# The mean of the numbers 1 to 9 (inclusive)
# 

# For those interested, each of these libraries has their own documentation. [NumPy](https://numpy.org/doc/stable/user/whatisnumpy.html), [SciPy](https://docs.scipy.org/doc/scipy/tutorial/general.html), [statistics](https://docs.python.org/3/library/statistics.html), and [math](https://docs.python.org/3/library/math.html)

# ## Exercise 2e Longitude and Latitude
# *Relevant Sections: 2.4.2, 2.4.1*
# 
# In section 2.4.2 a map of an area collected from the internet was displayed.
# 
# Write a function that will accept user-specified latitude, and longitude and return the response. Then use `IPython` to display the image as in 2.5.2
# 
# The answer could look something like:
# 
#     function_response = my_function(lat, lon)
#     Image(function_response)
# 
# some interesting coordinates are:

# In[2]:


coordinates_as_lat_lon = [
    (36.2110, -115.2669),
    (53.0066, 7.1920),
    (41.3908, 2.1631),
    (40.7822, -73.9653),
    (25.8380, 50.6050),
]


# ## Exercise 2f Defining Classes
# *Relevant Sections: 2.6.1, 2.6.2, 2.6.3, 2.6.4, 2.6.5*
# 
# In section 2.6.4 and 2.6.5 two examples of the maze model were given. 
# 
# Compare the two solutions.
# Discuss with a partner which you like better, and why.
# 
# Then, starting from scratch, design your own.
# What choices did you make that are different?

# ### Exercise 2g Longitude and Latitude Extension
# *Relevant Sections: 2.3.7*
# 
# Use the function you wrote in 2e above as the basis for a new function that will receive the longitude, latitude, **zoom level** and a name to save the file as.
# Use this function to save a map image file somewhere on your local disk.
# 
# *Zoom between 14 and 16 work well for the example coordinates*
# 
# 
