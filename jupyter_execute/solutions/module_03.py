#!/usr/bin/env python
# coding: utf-8

# # Module 03

# ### Exercise 3a  Saving and loading data
# *Relevant sections: 3.1.2, 3.1.3*
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


# ### Exercise 3a Answer

# **Save as JSON or YAML**

# In[2]:


import json
import yaml


# In[3]:


# Write with json.dump
with open("myfile.json", "w") as f:
    json.dump(house, f)


# In[4]:


# Look at the file on disk
get_ipython().system('cat myfile.json')


# In[5]:


# Or with file.write, using json.dumps to convert to a string
with open("myotherfile.json", "w") as json_maze_out:
    json_maze_out.write(json.dumps(house))


# In[6]:


# Look at the file on disk
get_ipython().system('cat myotherfile.json')


# In[7]:


# Write with yaml.safe_dump
with open("myfile.yml", "w") as f:
    yaml.safe_dump(house, f, default_flow_style=False)


# In[8]:


# Look at the file on disk
get_ipython().system('cat myfile.yml')


# In[9]:


# Or with file.write, using yaml.dump to convert to a string
with open("myotherfile.yaml", "w") as yaml_maze_out:
    yaml_maze_out.write(yaml.dump(house, default_flow_style=True))


# In[10]:


# Look at the file on disk
get_ipython().system('cat myotherfile.yaml')


# **Loading with JSON or YAML**

# In[11]:


# Read into a string then load with json.loads
with open("myfile.json", "r") as f:
    mydataasstring = f.read()
my_json_data = json.loads(mydataasstring)
print(my_json_data["living"])


# In[12]:


# Read directly with json.load
with open("myotherfile.json") as f_json_maze:
    maze_again = json.load(f_json_maze)
print(maze_again["living"])


# In[13]:


# Read into a string then load with yaml.safe_load
with open("myfile.yaml", "r") as f:
    mydataasstring = f.read()
my_yaml_data = yaml.safe_load(mydataasstring)
print(my_yaml_data["living"])


# In[14]:


# Read directly with yaml.safe_load
with open("myotherfile.yaml") as f_yaml_maze:
    maze_again = yaml.safe_load(f_yaml_maze)
print(maze_again["living"])


# ### Exercise 3b Plotting with matplotlib

# Generate two plots, next to each other (on the same row).
# 
# The first plot should show sin(x) and cos(x) for the range of x between -1 pi and +1 pi. 
# 
# The second plot should show sin(x), cos(x) and the sum of sin(x) and cos(x) over the same -pi to +pi range. Set suitable limits on the axes and pick colours, markers, or line-styles that will make it easy to differentiate between the curves. Add legends to both axes.

# ### Exercise 3b Answer

# In[15]:


import matplotlib.pyplot as plt
import numpy as np

# Use numpy to get the range of x values (math should work too)
x = np.arange(-np.pi, np.pi, 0.1)

# Define figure dimensions
fig = plt.figure(figsize=(15,5))


ax1 = fig.add_subplot(1,2,1)
ax1.plot(x, np.sin(x),label="sin(x)",color='black', linestyle='dashed')
ax1.plot(x, np.cos(x),label="cos(x)", color='#56B4E9')
ax1.legend()
ax1.set_ylim(-1.5, 1.5)

ax2 = fig.add_subplot(1,2,2)
ax2.plot(x, np.sin(x),label="sin(x)",color='black', linestyle='dashed')
ax2.plot(x, np.cos(x),label="cos(x)", color='#56B4E9')
ax2.plot(x, np.cos(x)+np.sin(x), label='cos(x) + sin(x)', color='#E69F00', marker=".")
ax2.legend()
ax2.set_ylim(-1.5, 1.5)


# ### Exercise 3c The biggest earthquake in the UK this century

# ### The Problem
# `GeoJSON` is a json-based file format for sharing geographic data. One example dataset is the USGS earthquake data:

# In[16]:


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


# In[17]:


quakes.text[0:100]


# ### Exercise 3c Answer
# *Relevant sections: 3.1, 2.5.2, 2.5.1*
# 
# ### Load the data
# * Get the text of the web result
# * Parse the data as JSON

# In[18]:


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
        "endtime": "2022-11-02", # Change the date to yesterday
        "orderby": "time-asc",
    },
)


# In[19]:


import json
# Can get the data indirectly via the text and then load json text....
my_quake_data = json.loads(quakes.text) # Section 3.1 - structured data

# Requests also has a built in json parser (note this gives exactly the same result as 'my_quake_data')
requests_json = quakes.json()


# ### Investigate the data
# * Understand how the data is structured into dictionaries and lists
#    * Where is the magnitude?
#    * Where is the place description or coordinates?

# There is no foolproof way of doing this. A good first step is to see the type of our data!

# In[20]:


type(requests_json)


# Now we can navigate through this dictionary to see how the information is stored in the nested dictionaries and lists. The `keys` method can indicate what kind of information each dictionary holds, and the `len` function tells us how many entries are contained in a list. How you explore is up to you!

# In[21]:


requests_json.keys()


# In[22]:


type(requests_json["features"])


# In[23]:


len(requests_json["features"])


# In[24]:


requests_json["features"][0]


# In[25]:


requests_json["features"][0].keys()


# It looks like the coordinates are in the `geometry` section and the magnitude is in the `properties` section.

# In[26]:


requests_json["features"][0]["geometry"]


# In[27]:


requests_json["features"][0]["properties"].keys()


# In[28]:


requests_json["features"][0]["properties"]["mag"]


# ### Search through the data
# * Program a search through all the quakes to find the biggest quake
# * Find the place of the biggest quake

# In[29]:


quakes = requests_json["features"]


# In[30]:


largest_so_far = quakes[0]
for quake in quakes:
    if quake["properties"]["mag"] > largest_so_far["properties"]["mag"]:
        largest_so_far = quake
largest_so_far["properties"]["mag"]


# In[31]:


lon = largest_so_far["geometry"]["coordinates"][0]
lat = largest_so_far["geometry"]["coordinates"][1]

print(f"Latitude: {lat} Longitude: {lon}")


# ### Visualise your answer
# * Form a URL for an online map service at that latitude and longitude: look back at the introductory example
# * Display that image

# In[32]:


import IPython
import requests


# In[33]:


# This is a solution to one of the questions in module 2
# The only difference here is that the map type is set to map rather than satellite view and the zoom is 10 not 12
def op_response(lat, lon):
    response = requests.get(
    "https://static-maps.yandex.ru:443/1.x",
        params={
            "size": "400,400",  # size of map
            "ll": str(lon) + "," + str(lat),  # longitude & latitude of centre
            "z": 10,  # zoom level
            "l": "map",  # map layer (map image)
            "lang": "en_US",  # language
            },
        )
    return response.content

    
op = op_response(lat, lon)

IPython.core.display.Image(op)


# ## [Optional] Equivalent solution using pandas

# In this instance Pandas probably isn't the first thing that you would use as we have nested dictionaries and JSON works very well in such cases.
# If we really want to use Pandas we'll need to flatten the nested values before constructing a DataFrame.

# In[35]:


features = requests_json["features"]
features[0]


# In[36]:


# We can use ** to convert a dictionary into pairs of (key, value)
# We can then run `{(k1, v1), (k2, v2)}` to convert a list of keys and values back into a dictionary
combined_features = [{**f["geometry"], **f["properties"]} for f in features]
combined_features[0]


# In[37]:


import pandas as pd

df = pd.DataFrame.from_records(combined_features)
df.head()


# In[38]:


df.sort_values("mag", ascending=False, inplace=True)
df.head()


# You can see that we haven't really gained much over the JSON solution.
# We still needed to look at the data to see its structure and we had to manually flatten the structure.
