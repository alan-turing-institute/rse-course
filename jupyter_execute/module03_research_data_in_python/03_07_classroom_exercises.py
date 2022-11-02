#!/usr/bin/env python
# coding: utf-8

# # 3.7 Classroom Exercises

# **List of exercises and estimated completion times**
# 
# 
# [3a - Saving and Loading Data](#Exercise-3a-Saving-and-Loading-Data) *5 minutes*
# 
# [3b - Plotting with matplotlib](#Exercise-3b-Plotting-with-matplotlib) *10 minutes*
# 
# [3c The Biggest Earthquake in the UK This Century](#Exercise-3c-The-Biggest-Earthquake-in-the-UK-This-Century) *30 minutes*

# ## Exercise 3a  Saving and Loading Data
# *Relevant sections: 3.2.2, 3.2.3*
# 
# Use YAML or JSON to save your maze data structure to disk and load it again.
# 
# The maze would have looked something like this:

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


# ## Exercise 3b Plotting with matplotlib

# Generate two plots, next to each other (on the same row).
# 
# The first plot should show sin(x) and cos(x) for the range of x between -1 pi and +1 pi.
# 
# **Hint:** The `range(start, stop, step)` function only works with integers. Use the `arange` function from `numpy` instead: `np.arange(start, stop, step)`.
# 
# The second plot should show sin(x), cos(x) and the sum of sin(x) and cos(x) over the same -pi to +pi range.
# Set suitable limits on the axes and pick colours, markers, or line-styles that will make it easy to differentiate between the curves.
# Add legends to both axes.

# ## Exercise 3c The Biggest Earthquake in the UK This Century
# 
# `GeoJSON` is a json-based file format for sharing geographic data.
# One example dataset is the USGS earthquake data:

# In[2]:


import requests

quakes = requests.get(
    "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
    params={
        "starttime": "2000-01-01",
        "maxlatitude": "58.723",
        "minlatitude": "50.008",
        "maxlongitude": "1.67",
        "minlongitude": "-9.756",
        "minmagnitude": "1",
        "endtime": "2021-01-19",
        "orderby": "time-asc",
    },
    timeout=60,
)


# In[3]:


quakes.text[0:100]


# ### The Problem
# 
# Determine the **location** of the **largest magnitude** earthquake in the UK this century.

# You can break this exercise down into several subtasks.
# You'll need to:
# #### Load the data
# * Get the text of the web result
# * Parse the data as JSON
# 
# #### Investigate the data
# * Understand how the data is structured into dictionaries and lists
#    * Where is the magnitude?
#    * Where is the place description or coordinates?
#    
# #### Search through the data
# * Program a search through all the quakes to find the biggest quake
# * Find the place of the biggest quake
# 
# #### Visualise your answer
# * Form a URL for an online map service at that latitude and longitude: look back at the introductory example
# * Display that image
