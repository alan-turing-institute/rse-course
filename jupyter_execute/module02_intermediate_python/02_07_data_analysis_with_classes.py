#!/usr/bin/env python
# coding: utf-8

# # 2.7 Data analysis with classes

# *Estimated time to complete this notebook: 10 minutes*

# Earlier, we wrote some code to measure the amount of green content on satellite images.
# Now, we're going to convert this into a "Greengraph" class, and save it as a module.

# ⚠️ **It is generally a better idea to create files in an editor or integrated development environment (IDE) rather than through the notebook!** ⚠️

# ## 2.7.1 Classes for Greengraph

# In[1]:


get_ipython().run_cell_magic('bash', '', 'mkdir -p greengraph  # Create the folder for the module (on mac or linux)\n')


# In[2]:


get_ipython().run_cell_magic('writefile', 'greengraph/graph.py', 'import numpy as np\nimport geopy\nfrom .map import Map\n\n\nclass Greengraph:\n    def __init__(self, start, end):\n        self.start = start\n        self.end = end\n        self.geocoder = geopy.geocoders.Nominatim(user_agent="rsd-course")\n\n    def geolocate(self, place):\n        return self.geocoder.geocode(place, exactly_one=False)[0][1]\n\n    def location_sequence(self, start, end, steps):\n        lats = np.linspace(start[0], end[0], steps)\n        longs = np.linspace(start[1], end[1], steps)\n        return np.vstack([lats, longs]).transpose()\n\n    def green_between(self, steps):\n        return [\n            Map(*location).count_green()\n            for location in self.location_sequence(\n                self.geolocate(self.start), self.geolocate(self.end), steps\n            )\n        ]\n')


# In[3]:


get_ipython().run_cell_magic('writefile', 'greengraph/map.py', '\nimport numpy as np\nfrom io import BytesIO\nimport imageio as img\nimport requests\n\n\nclass Map:\n    def __init__(\n        self, lat, long, satellite=True, zoom=10, size=(400, 400), sensor=False\n    ):\n        base = "https://static-maps.yandex.ru/1.x/?"\n\n        params = dict(\n            z=zoom,\n            size=str(size[0]) + "," + str(size[1]),\n            ll=str(long) + "," + str(lat),\n            l="sat" if satellite else "map",\n            lang="en_US",\n        )\n\n        self.image = requests.get(\n            base, params=params\n        ).content  # Fetch our PNG image data\n        content = BytesIO(self.image)\n        self.pixels = img.imread(content)  # Parse our PNG image as a numpy array\n\n    def green(self, threshold):\n        # Use NumPy to build an element-by-element logical array\n        greener_than_red = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 0]\n        greener_than_blue = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 2]\n        green = np.logical_and(greener_than_red, greener_than_blue)\n        return green\n\n    def count_green(self, threshold=1.1):\n        return np.sum(self.green(threshold))\n\n    def show_green(data, threshold=1.1):\n        green = self.green(threshold)\n        out = green[:, :, np.newaxis] * array([0, 1, 0])[np.newaxis, np.newaxis, :]\n        buffer = BytesIO()\n        result = img.imwrite(buffer, out, format="png")\n        return buffer.getvalue()\n')


# In[4]:


get_ipython().run_cell_magic('writefile', 'greengraph/__init__.py', 'from .graph import Greengraph\n')


# ## 2.7.2 Invoking our code and making a plot

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
from greengraph import Greengraph
from matplotlib import pyplot as plt

mygraph = Greengraph("New York", "Chicago")
data = mygraph.green_between(20)


# In[6]:


plt.plot(data)

