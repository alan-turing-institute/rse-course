#!/usr/bin/env python
# coding: utf-8

# # 3.1 Structured Data

# *Estimated time to complete this notebook: 15 minutes*

# ## 3.1.1 Structured data

# CSV files can only model data where each record has several fields, and each field is a simple datatype,
# a string or number.

# We often want to store data which is more complicated than this, with nested structures of lists and dictionaries.
# Structured data formats like JSON, YAML, and XML are designed for this.

# ## 3.1.2 JSON

# [JSON](https://en.wikipedia.org/wiki/JSON) is a very common open-standard data format that is used to store structured data in a human-readable way.

# This allows us to represent data which is combinations of lists and dictionaries as a text file which
# looks a bit like a Javascript (or Python) data literal.

# In[1]:


import json


# **Any nested group of dictionaries and lists can be saved:**

# Saving and loading data is really easy.
# 
# To save a dictionary as a json file:

# In[2]:


example_dictionary = {"somekey": ["a list", "with values", "for json"]}

with open("myfile.json", "w") as f:
    json.dump(example_dictionary, f)


# And read in the data back in from the file

# In[3]:


with open("myfile.json", "r") as f:
    my_json_data = json.load(f)


# In[4]:


my_json_data


# In[5]:


my_json_data["somekey"]


# This is a very nice solution for loading and saving Python data structures.
# 
# It's a very common way of transferring data on the internet, and of saving datasets to disk.
# 
# There's good support in most languages, so it's a nice inter-language file interchange format.

# ## 3.1.3 YAML

# [YAML](https://en.wikipedia.org/wiki/YAML) is a very similar data format to JSON, with some nice additions:

# * You don't need to quote strings if they don't have funny characters in
# * You can have comment lines, beginning with a #
# * You can write dictionaries without the curly brackets: it just notices the colons.
# * You can write lists like this:

# In[6]:


get_ipython().run_cell_magic('writefile', 'myfile.yaml', 'somekey:\n    - a list # Look, this is a list\n    - with values\n    - for yaml\n')


# In[7]:


import yaml  # This may need installed as pyyaml


# In[8]:


with open("myfile.yaml") as myfile:
    my_yaml_data = yaml.safe_load(myfile)
print(my_yaml_data)


# **Supplementary Materials:** `yaml.safe_load` is preferred over `yaml.load` to avoid executing arbitrary code in untrusted files. See [here](https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation) for details.

# YAML is a popular format for ad-hoc data files, but the library doesn't ship with default Python (though it is part
# of Anaconda and Canopy), so some people still prefer JSON for its universality.

# Because YAML gives the **option** of serialising a list either as newlines with dashes, *or* with square brackets,
# you can control this choice:

# In[9]:


print(yaml.safe_dump(my_yaml_data, default_flow_style=True))


# In[10]:


print(yaml.safe_dump(my_yaml_data, default_flow_style=False))


# `default_flow_style=False` uses a "block style" (rather than an "inline" or "flow style") to delineate data structures. [See the YAML docs for more details](http://yaml.org/spec/1.2/spec.html).

# In addition to saving a yaml file via cell magics, they can also be written:

# In[11]:


with open("myotherfile.yml", "w") as f:
    yaml.safe_dump(my_yaml_data, f, default_flow_style=False)


# ## 3.1.4 JSON to YAML

# And of course the json formatted data can be written as a yaml file, and vice versa. Here we are taking the data we read in for the json example and saving it as a yaml file. 

# In[12]:


with open("json_to_yaml.yaml", "w") as f:
    yaml.safe_dump(my_json_data, f, default_flow_style=False)


# You can compare the original json file to the json-data-saved-as-yaml either when loaded....

# In[13]:


# The original json file
with open("myfile.json", "r") as f:
    mydataasstring = f.read()
print(json.loads(mydataasstring))


# In[14]:


# The data from the json file saved as a yaml then read in
with open("json_to_yaml.yaml") as f:
    my_json_yaml_data = yaml.safe_load(f)
print(my_json_yaml_data)


# To how they appear in their respective file formats

# In[15]:


get_ipython().run_cell_magic('bash', '', "#%%cmd (windows)\ncat 'myfile.json' # The original json file\n")


# In[16]:


get_ipython().run_cell_magic('bash', '', "#%%cmd (windows)\ncat 'json_to_yaml.yaml' # The data from the json file saved as a yaml\n")


# ## 3.1.5 XML

# **Supplementary material**: [XML](http://www.w3schools.com/xml/) is another popular choice when saving nested data structures. 
# It's very careful, but verbose. If your field uses XML data, you'll need to learn a [python XML parser](https://docs.python.org/3/library/xml.etree.elementtree.html)
# (there are a few), and about how XML works.
