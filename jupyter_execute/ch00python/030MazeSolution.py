#!/usr/bin/env python
# coding: utf-8

# # Solution: my Maze Model

# Here's one possible solution to the Maze model. Yours will probably be different, and might be just as good.
# That's the artistry of software engineering: some solutions will be faster, others use less memory, while others will
# be easier for other people to understand. Optimising and balancing these factors is fun!

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


# Some important points:

# * The whole solution is a complete nested structure.
# * I used indenting to make the structure easier to read.
# * Python allows code to continue over multiple lines, so long as sets of brackets are not finished.
# * There is an **empty** person list in empty rooms, so the type structure is robust to potential movements of people.
# * We are nesting dictionaries and lists, with string and integer data.
