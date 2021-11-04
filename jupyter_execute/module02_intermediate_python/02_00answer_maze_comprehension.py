#!/usr/bin/env python
# coding: utf-8

# # Solution

# With this maze structure:

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


# We can get a simpler dictionary with just capacities like this:

# In[2]:


{name: room["capacity"] for name, room in house.items()}


# To get the current number of occupants, we can use a similar dictionary comprehension. Remember that we can *filter* (only keep certain rooms) by adding an `if` clause:

# In[3]:


{name: len(room["people"]) for name, room in house.items() if len(room["people"]) > 0}

