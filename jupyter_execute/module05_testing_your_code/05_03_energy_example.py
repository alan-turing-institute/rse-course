#!/usr/bin/env python
# coding: utf-8

# # 5.3 Classroom exercise: energy calculation
# 

# *Estimated time for this notebook: 30 minutes*

# 
# ## Diffusion model in 1D
# 
# Description: A one-dimensional diffusion model. (Could be a gas of particles, or a bunch of crowded people in a corridor, or animals in a valley habitat...)
# 
# - Agents are on a 1d axis
# - Agents do not want to be where there are other agents
# - This is represented as an 'energy': the higher the energy, the more unhappy the agents.
# 
# Implementation:
# 
# - Given a vector $n$ of positive integers, and of arbitrary length
# - Compute the energy, $E(n) = \sum_i n_i(n_i - 1)$
# - Later, we will have the likelyhood of an agent moving depend on the change in energy.

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
from matplotlib import pyplot as plt

density = np.array([0, 0, 3, 5, 8, 4, 2, 1])
fig, ax = plt.subplots()
ax.bar(np.arange(len(density)) - 0.5, density)
ax.xrange = [-0.5, len(density) - 0.5]
ax.set_ylabel("Particle count $n_i$")
ax.set_xlabel("Position $i$")


# Here, the total energy due to position 2 is $3 (3-1)=6$, and due to column 7 is $1 (1-1)=0$. We need to sum these to get the
# total energy.

# ## Starting point
# 
# Create a Python module:

# In[2]:


get_ipython().run_cell_magic('bash', '', 'rm -rf diffusion\nmkdir diffusion\ntouch diffusion/__init__.py\n')


# **Windows:** You will need to run the following instead
#     
# ```cmd
# %%cmd
# rmdir /s diffusion
# mkdir diffusion
# type nul > diffusion/__init__.py
# ```
# 
# **NB.** If you are using the Windows command prompt, you will also have to replace all subsequent `%%bash` directives with `%%cmd` 

# * Implementation file: diffusion_model.py

# In[3]:


get_ipython().run_cell_magic('writefile', 'diffusion/model.py', 'def energy(density, coeff=1.0):\n    """Energy associated with the diffusion model\n\n    Parameters\n    ----------\n\n    density: array of positive integers\n        Number of particles at each position i in the array\n    coeff: float\n        Diffusion coefficient.\n    """\n    # implementation goes here\n')


# * Testing file: test_diffusion_model.py

# In[4]:


get_ipython().run_cell_magic('writefile', 'diffusion/test_model.py', 'from .model import energy\n\n\ndef test_energy():\n    pass\n    # Test something\n')


# Invoke the tests:

# In[5]:


get_ipython().run_cell_magic('bash', '', 'cd diffusion\npytest\n')


# Now, write your code (in `model.py`), and tests (in `test_model.py`), testing as you do.

# ## Solution
# 
# Don't look until after you've tried!
# 
# In the spirit of test-driven development let's first consider our tests.

# In[6]:


get_ipython().run_cell_magic('writefile', 'diffusion/test_model.py', '"""Unit tests for a diffusion model."""\n\nfrom pytest import raises\nfrom .model import energy\n\n\ndef test_energy_fails_on_non_integer_density():\n    with raises(TypeError) as exception:\n        energy([1.0, 2, 3])\n\n\ndef test_energy_fails_on_negative_density():\n    with raises(ValueError) as exception:\n        energy([-1, 2, 3])\n\n\ndef test_energy_fails_ndimensional_density():\n    with raises(ValueError) as exception:\n        energy([[1, 2, 3], [3, 4, 5]])\n\n\ndef test_zero_energy_cases():\n    # Zero energy at zero density\n    densities = [[], [0], [0, 0, 0]]\n    for density in densities:\n        assert energy(density) == 0\n\n\ndef test_derivative():\n    from numpy.random import randint\n\n    # Loop over vectors of different sizes (but not empty)\n    for vector_size in randint(1, 1000, size=30):\n\n        # Create random density of size N\n        density = randint(50, size=vector_size)\n\n        # will do derivative at this index\n        element_index = randint(vector_size)\n\n        # modified densities\n        density_plus_one = density.copy()\n        density_plus_one[element_index] += 1\n\n        # Compute and check result\n        # d(n^2-1)/dn = 2n\n        expected = 2.0 * density[element_index] if density[element_index] > 0 else 0\n        actual = energy(density_plus_one) - energy(density)\n        assert expected == actual\n\n\ndef test_derivative_no_self_energy():\n    """If particle is alone, then its participation to energy is zero."""\n    from numpy import array\n\n    density = array([1, 0, 1, 10, 15, 0])\n    density_plus_one = density.copy()\n    density[1] += 1\n\n    expected = 0\n    actual = energy(density_plus_one) - energy(density)\n    assert expected == actual\n')


# Now let's write an implementation that passes the tests.
# 

# In[7]:


get_ipython().run_cell_magic('writefile', 'diffusion/model.py', '"""Simplistic 1-dimensional diffusion model."""\nfrom numpy import array, any, sum\n\n\ndef energy(density):\n    """Energy associated with the diffusion model\n    :Parameters:\n      density: array of positive integers\n         Number of particles at each position i in the array/geometry\n    """\n\n    # Make sure input is an numpy array\n    density = array(density)\n\n    # ...of the right kind (integer). Unless it is zero length,\n    #    in which case type does not matter.\n\n    if density.dtype.kind != "i" and len(density) > 0:\n        raise TypeError("Density should be a array of *integers*.")\n    # and the right values (positive or null)\n    if any(density < 0):\n        raise ValueError("Density should be an array of *positive* integers.")\n    if density.ndim != 1:\n        raise ValueError(\n            "Density should be an a *1-dimensional*" + "array of positive integers."\n        )\n\n    return sum(density * (density - 1))\n')


# In[8]:


get_ipython().run_cell_magic('bash', '', 'cd diffusion\npytest\n')


# ## Coverage
# 
# With pytest, you can use the ["pytest-cov" plugin](https://github.com/pytest-dev/pytest-cov) to measure test coverage

# In[9]:


get_ipython().run_cell_magic('bash', '', 'cd diffusion\npytest --cov\n')


# Or an html report:

# In[10]:


get_ipython().run_cell_magic('bash', '', '#%%cmd (windows)\ncd diffusion\npytest --cov --cov-report html\n')


# The HTML [coverage results](./diffusion/htmlcov/index.html) will be in `diffusion/htmlcov/index.html`
