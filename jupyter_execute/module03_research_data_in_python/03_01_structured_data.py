#!/usr/bin/env python
# coding: utf-8

# # Structured Data

# ## Structured data

# CSV files can only model data where each record has several fields, and each field is a simple datatype,
# a string or number.

# We often want to store data which is more complicated than this, with nested structures of lists and dictionaries.
# Structured data formats like JSON, YAML, and XML are designed for this.

# ## JSON

# [JSON](https://en.wikipedia.org/wiki/JSON) is a very common open-standard data format that is used to store structured data in a human-readable way.

# This allows us to represent data which is combinations of lists and dictionaries as a text file which
# looks a bit like a Javascript (or Python) data literal.

# In[1]:


import json


# Any nested group of dictionaries and lists can be saved:

# In[2]:


mydata = {"key": ["value1", "value2"], "key2": {"key4": "value3"}}


# In[3]:


json.dumps(mydata)


# If you would like a more readable output, you can use the `indent` argument.

# In[4]:


print(json.dumps(mydata, indent=4))


# Loading data is also really easy:

# In[5]:


get_ipython().run_cell_magic('writefile', 'myfile.json', '{"somekey": ["a list", "with values"]}')


# In[6]:


with open("myfile.json", "r") as f:
    mydataasstring = f.read()


# In[7]:


mydataasstring


# In[8]:


mydata = json.loads(mydataasstring)


# In[9]:


mydata["somekey"]


# This is a very nice solution for loading and saving Python data structures.

# It's a very common way of transferring data on the internet, and of saving datasets to disk.

# There's good support in most languages, so it's a nice inter-language file interchange format.

# ## YAML

# [YAML](https://en.wikipedia.org/wiki/YAML) is a very similar data format to JSON, with some nice additions:

# * You don't need to quote strings if they don't have funny characters in
# * You can have comment lines, beginning with a #
# * You can write dictionaries without the curly brackets: it just notices the colons.
# * You can write lists like this:

# In[10]:


get_ipython().run_cell_magic('writefile', 'myfile.yaml', 'somekey:\n    - a list # Look, this is a list\n    - with values')


# In[11]:


import yaml  # This may need installed as pyyaml


# In[12]:


with open("myfile.yaml") as myfile:
    mydata = yaml.safe_load(myfile)
print(mydata)


# **Supplementary Materials:** `yaml.safe_load` is preferred over `yaml.load` to avoid executing arbitrary code in untrusted files. See [here](https://github.com/yaml/pyyaml/wiki/PyYAML-yaml.load(input)-Deprecation) for details.

# YAML is a popular format for ad-hoc data files, but the library doesn't ship with default Python (though it is part
# of Anaconda and Canopy), so some people still prefer JSON for its universality.

# Because YAML gives the **option** of serialising a list either as newlines with dashes, *or* with square brackets,
# you can control this choice:

# In[13]:


print(yaml.safe_dump(mydata, default_flow_style=True))


# In[14]:


print(yaml.safe_dump(mydata, default_flow_style=False))


# `default_flow_style=False` uses a "block style" (rather than an "inline" or "flow style") to delineate data structures. [See the YAML docs for more details](http://yaml.org/spec/1.2/spec.html).

# ## XML

# **Supplementary material**: [XML](http://www.w3schools.com/xml/) is another popular choice when saving nested data structures. 
# It's very careful, but verbose. If your field uses XML data, you'll need to learn a [python XML parser](https://docs.python.org/3/library/xml.etree.elementtree.html)
# (there are a few), and about how XML works.

# ### Exercise: Saving and loading data

# Use YAML or JSON to save your maze data structure to disk and load it again.
