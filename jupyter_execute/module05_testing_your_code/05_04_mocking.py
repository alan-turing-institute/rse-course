#!/usr/bin/env python
# coding: utf-8

# # 5.4 Mocking

# *Estimated time for this notebook: 15 minutes*

# ## Definition
# 
# **Mock**: *verb*,
# 
# 1. to tease or laugh at in a scornful or contemptuous manner
# 2. to make a replica or imitation of something

# **Mocking**
# 
# - Replace a real object with a pretend object, which records how it is called, and can assert if it is called wrong

# ## Mocking frameworks
# 
# * C: [CMocka](http://www.cmocka.org/)
# * C++: [googlemock](https://google.github.io/googletest/reference/mocking.html)
# * Python: [unittest.mock](http://docs.python.org/dev/library/unittest.mock)

# ## Recording calls with mock
# 
# Mock objects record the calls made to them:

# In[1]:


from unittest.mock import Mock


function = Mock(name="myroutine", return_value=2)


# In[2]:


function(1)


# In[3]:


function(5, "hello", a=True)


# In[4]:


function.mock_calls


# The arguments of each call can be recovered

# In[5]:


name, args, kwargs = function.mock_calls[1]
args, kwargs


# Mock objects can return different values for each call

# In[6]:


function = Mock(name="myroutine", side_effect=[2, "xyz"])


# In[7]:


function(1)


# In[8]:


function(1, "hello", {"a": True})


# We expect an error if there are no return values left in the list:

# In[9]:


function()


# ## Using mocks to model test resources

# Often we want to write tests for code which interacts with remote resources. (E.g. databases, the internet, or data files.)

# We don't want to have our tests *actually* interact with the remote resource, as this would mean our tests failed
# due to lost internet connections, for example.

# Instead, we can use mocks to assert that our code does the right thing in terms of the *messages it sends*: the parameters of the
# function calls it makes to the remote resource.

# For example, consider the following code that downloads a map from the internet:

# In[10]:


import requests


def map_at(lat, long, satellite=False, zoom=12, size=(400, 400)):
    base = "https://static-maps.yandex.ru/1.x/?"
    params = dict(
        z=zoom,
        size=str(size[0]) + "," + str(size[1]),
        ll=str(long) + "," + str(lat),
        l="sat" if satellite else "map",
        lang="en_US",
    )
    return requests.get(base, params=params)


# In[11]:


london_map = map_at(51.5073509, -0.1277583)


# In[12]:


get_ipython().run_line_magic('matplotlib', 'inline')
import IPython

IPython.core.display.Image(london_map.content)


# We would like to test that it is building the parameters correctly. We can do this by **mocking** the requests object. We need to temporarily replace a method in the library with a mock. We can use "patch" to do this:

# In[13]:


from unittest.mock import patch

with patch.object(requests, "get") as mock_get:
    london_map = map_at(51.5073509, -0.1277583)
    print(mock_get.mock_calls)


# Our tests then look like:

# In[14]:


def test_build_default_params():
    with patch.object(requests, "get") as mock_get:
        default_map = map_at(51.0, 0.0)
        mock_get.assert_called_with(
            "https://static-maps.yandex.ru/1.x/?",
            params={
                "z": 12,
                "size": "400,400",
                "ll": "0.0,51.0",
                "l": "map",
                "lang": "en_US",
            },
        )


test_build_default_params()


# That was quiet, so it passed. When I'm writing tests, I usually modify one of the expectations, to something 'wrong', just to check it's not
# passing "by accident", run the tests, then change it back!

# ## Testing functions that call other functions

# In[15]:


def partial_derivative(function, at, direction, delta=1.0):
    f_x = function(at)
    x_plus_delta = at[:]
    x_plus_delta[direction] += delta
    f_x_plus_delta = function(x_plus_delta)
    return (f_x_plus_delta - f_x) / delta


# We want to test that the above function does the right thing. It is supposed to compute the derivative of a function
# of a vector in a particular direction.

# E.g.:

# In[16]:


partial_derivative(sum, [0, 0, 0], 1)


# How do we assert that it is doing the right thing? With tests like this:

# In[17]:


from unittest.mock import MagicMock


def test_derivative_2d_y_direction():
    func = MagicMock()
    partial_derivative(func, [0, 0], 1)
    func.assert_any_call([0, 1.0])
    func.assert_any_call([0, 0])


test_derivative_2d_y_direction()


# We made our mock a "Magic Mock" because otherwise, the mock results `f_x_plus_delta` and `f_x` can't be subtracted:

# In[18]:


MagicMock() - MagicMock()


# In[19]:


Mock() - Mock()

