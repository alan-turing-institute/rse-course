#!/usr/bin/env python
# coding: utf-8

# # Solution: counting people in the maze

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


# We can count the occupants and capacity like this:

# In[2]:


capacity = 0
occupancy = 0
for name, room in house.items():
    capacity += room["capacity"]
    occupancy += len(room["people"])
print("House can fit {} people, and currently has: {}.".format(capacity, occupancy))


# As a side note, note how we included the values of `capacity` and `occupancy` in the last line. This is a handy syntax for building strings that contain the values of variables. You can read more about it [here](https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat) or in the official documentation for the [string format method](https://docs.python.org/3/library/stdtypes.html#str.format).
