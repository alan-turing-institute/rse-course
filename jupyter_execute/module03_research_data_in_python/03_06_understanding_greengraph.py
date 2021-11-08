#!/usr/bin/env python
# coding: utf-8

# # Recap: Understanding the "Greengraph" Example

# We now know enough to understand everything we did in [the initial example chapter on the "Greengraph"](https://alan-turing-institute.github.io/rsd-engineeringcourse/html/module01_introduction_to_python/01_01_data_analysis_example.html) ([notebook](../module01_introduction_to_python/01_01_data_analysis_example.ipynb)). Go back to that part of the notes, and re-read the code. 

# Now, we can even write it up into a class, and save it as a module. Remember that it is generally a better idea to create files in an editor or integrated development environment (IDE) rather than through the notebook!

# ## Classes for Greengraph

# In[1]:


get_ipython().run_cell_magic('bash', '', '#%%cmd (windows)\nmkdir -p greengraph  # Create the folder for the module (on mac or linux)')


# In[2]:


get_ipython().run_cell_magic('writefile', 'greengraph/graph.py', 'import numpy as np\nimport geopy\nfrom .map import Map\n\n\nclass Greengraph:\n    def __init__(self, start, end):\n        self.start = start\n        self.end = end\n        self.geocoder = geopy.geocoders.Nominatim(user_agent="rsd-course")\n\n    def geolocate(self, place):\n        return self.geocoder.geocode(place, exactly_one=False)[0][1]\n\n    def location_sequence(self, start, end, steps):\n        lats = np.linspace(start[0], end[0], steps)\n        longs = np.linspace(start[1], end[1], steps)\n        return np.vstack([lats, longs]).transpose()\n\n    def green_between(self, steps):\n        return [\n            Map(*location).count_green()\n            for location in self.location_sequence(\n                self.geolocate(self.start), self.geolocate(self.end), steps\n            )\n        ]')


# In[3]:


get_ipython().run_cell_magic('writefile', 'greengraph/map.py', '\nimport numpy as np\nfrom io import BytesIO\nimport imageio as img\nimport requests\n\n\nclass Map:\n    def __init__(\n        self, lat, long, satellite=True, zoom=10, size=(400, 400), sensor=False\n    ):\n        base = "https://static-maps.yandex.ru/1.x/?"\n\n        params = dict(\n            z=zoom,\n            size=str(size[0]) + "," + str(size[1]),\n            ll=str(long) + "," + str(lat),\n            l="sat" if satellite else "map",\n            lang="en_US",\n        )\n\n        self.image = requests.get(\n            base, params=params\n        ).content  # Fetch our PNG image data\n        content = BytesIO(self.image)\n        self.pixels = img.imread(content)  # Parse our PNG image as a numpy array\n\n    def green(self, threshold):\n        # Use NumPy to build an element-by-element logical array\n        greener_than_red = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 0]\n        greener_than_blue = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 2]\n        green = np.logical_and(greener_than_red, greener_than_blue)\n        return green\n\n    def count_green(self, threshold=1.1):\n        return np.sum(self.green(threshold))\n\n    def show_green(data, threshold=1.1):\n        green = self.green(threshold)\n        out = green[:, :, np.newaxis] * array([0, 1, 0])[np.newaxis, np.newaxis, :]\n        buffer = BytesIO()\n        result = img.imwrite(buffer, out, format="png")\n        return buffer.getvalue()')


# In[4]:


get_ipython().run_cell_magic('writefile', 'greengraph/__init__.py', 'from .graph import Greengraph')


# ## Invoking our code and making a plot

# In[5]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
from greengraph import Greengraph

mygraph = Greengraph("New York", "Chicago")
data = mygraph.green_between(20)


# In[6]:


plt.plot(data)

