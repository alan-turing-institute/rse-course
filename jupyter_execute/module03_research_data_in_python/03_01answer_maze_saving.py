#!/usr/bin/env python
# coding: utf-8

# # Solution: Saving and loading data

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


# Save the maze with json:

# In[2]:


import json


# In[3]:


with open("maze.json", "w") as json_maze_out:
    json_maze_out.write(json.dumps(house))


# Consider the file on the disk:

# In[4]:


get_ipython().run_cell_magic('bash', '', "#%%cmd (windows)\ncat 'maze.json'\n")


# and now load it into a different variable:

# In[5]:


with open("maze.json") as json_maze_in:
    maze_again = json.load(json_maze_in)


# In[6]:


maze_again


# Or with YAML:

# In[7]:


import yaml


# In[8]:


with open("maze.yaml", "w") as yaml_maze_out:
    yaml_maze_out.write(yaml.dump(house))


# In[9]:


get_ipython().run_cell_magic('bash', '', "#%%cmd (windows)\ncat 'maze.yaml'\n")


# In[10]:


with open("maze.yaml") as yaml_maze_in:
    maze_again = yaml.safe_load(yaml_maze_in)


# In[11]:


maze_again

