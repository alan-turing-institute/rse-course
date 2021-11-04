#!/usr/bin/env python
# coding: utf-8

# # Exercise/Example: the biggest Earthquake in the UK this Century

# ## The Problem

# `GeoJSON` is a json-based file format for sharing geographic data. One example dataset is the USGS earthquake data:

# In[1]:


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
)


# In[2]:


quakes.text[0:100]


# ## Your exercise
# 
# Determine the **location** of the **largest magnitude** earthquake in the UK this century.

# You can break this exercise down into several subtasks. You'll need to:
# ### Load the data
# * Get the text of the web result
# * Parse the data as JSON
# 
# ### Investigate the data
# * Understand how the data is structured into dictionaries and lists
#    * Where is the magnitude?
#    * Where is the place description or coordinates?
#    
# ### Search through the data
# * Program a search through all the quakes to find the biggest quake
# * Find the place of the biggest quake
# 
# ### Visualise your answer
# * Form a URL for an online map service at that latitude and longitude: look back at the introductory example
# * Display that image
