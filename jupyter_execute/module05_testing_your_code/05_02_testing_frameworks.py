#!/usr/bin/env python
# coding: utf-8

# # Testing frameworks

# ## Why use testing frameworks?
# 
# Frameworks should simplify our lives:
# 
# * Should be easy to add simple test
# * Should be possible to create complex test:
#     * Fixtures
#     * Setup/Tear down
#     * Parameterized tests (same test, mostly same input)
# * Find all our tests in a complicated code-base 
# * Run all our tests with a quick command
# * Run only some tests, e.g. ``test --only "tests about fields"``
# * **Report failing tests**
# * Additional goodies, such as code coverage

# ## Common testing frameworks

# * Language agnostic: [CTest](https://cmake.org/cmake/help/latest/manual/ctest.1.html)
#   * Test runner for executables, bash scripts, etc...
#   * Great for legacy code hardening
#     
# * C unit-tests:
#     * all c++ frameworks,
#     * [Check](https://libcheck.github.io/check/),
#     * [CUnit](http://cunit.sourceforge.net)
# 
# * C++ unit-tests:
#     * [CppTest](http://cpptest.sourceforge.net/),
#     * [Boost::Test](https://www.boost.org/doc/libs/1_79_0/libs/test/doc/html/index.html),
#     * [google-test](https://google.github.io/googletest/),
#     * [Catch](https://github.com/catchorg/Catch2)
# 
# * Python unit-tests:
#     * [unittest](https://docs.python.org/3/library/unittest.html) comes with standard python library
#     * [pytest](http://pytest.org/latest/), includes test discovery, coverage, etc
# 
# * R unit-tests:
#     * [RUnit](https://cran.r-project.org/web/packages/RUnit/index.html),
#     * [testthat](https://testthat.r-lib.org/)
# 
# * Fortran unit-tests:
#     * [pfunit](https://github.com/Goddard-Fortran-Ecosystem/pFUnit)(works with MPI)

# ## pytest framework: usage
# 
# [pytest](https://docs.pytest.org/en/latest/) is a recommended python testing framework.

# We can use its tools in the notebook for on-the-fly tests in the notebook. This, happily, includes the negative-tests example we were looking for a moment ago.

# In[1]:


def I_only_accept_positive_numbers(number):
    # Check input
    if number < 0:
        raise ValueError("Input " + str(number) + " is negative")

    # Do something


# In[2]:


from pytest import raises


# In[3]:


with raises(ValueError):
    I_only_accept_positive_numbers(-5)


# but the real power comes when we write a test file alongside our code files in our homemade packages:

# In[4]:


get_ipython().run_cell_magic('bash', '', "#on windows replace '%%bash' with %%cmd\nrm -rf saskatchewan\nmkdir -p saskatchewan\ntouch saskatchewan/__init__.py #on windows replace with 'type nul > saskatchewan/__init__.py'\n")


# In[5]:


get_ipython().run_cell_magic('writefile', 'saskatchewan/overlap.py', "def overlap(field1, field2):\n    left1, bottom1, top1, right1 = field1\n    left2, bottom2, top2, right2 = field2\n\n    overlap_left = max(left1, left2)\n    overlap_bottom = max(bottom1, bottom2)\n    overlap_right = min(right1, right2)\n    overlap_top = min(top1, top2)\n    # Here's our wrong code again\n    overlap_height = overlap_top - overlap_bottom\n    overlap_width = overlap_right - overlap_left\n\n    return overlap_height * overlap_width\n")


# In[6]:


get_ipython().run_cell_magic('writefile', 'saskatchewan/test_overlap.py', 'from .overlap import overlap\n\n\ndef test_full_overlap():\n    assert overlap((1.0, 1.0, 4.0, 4.0), (2.0, 2.0, 3.0, 3.0)) == 1.0\n\n\ndef test_partial_overlap():\n    assert overlap((1, 1, 4, 4), (2, 2, 3, 4.5)) == 2.0\n\n\ndef test_no_overlap():\n    assert overlap((1, 1, 4, 4), (4.5, 4.5, 5, 5)) == 0.0\n')


# In[7]:


get_ipython().run_cell_magic('bash', '', '#%%cmd #(windows)\ncd saskatchewan\npytest || echo "Tests failed"\n')


# Note that it reported **which** test had failed, how many tests ran, and how many failed.

# The symbol `..F` means there were three tests, of which the third one failed.

# Pytest will:
# 
# * automagically finds files ``test_*.py``
# * collects all subroutines called ``test_*``
# * runs tests and reports results

# Some options:
# 
# * help: `pytest --help`
# * run only tests for a given feature: `pytest -k foo` # tests with 'foo' in the test name

# # Testing with floating points
# 
# ## Floating points are not reals
# 
# 
# Floating points are inaccurate representations of real numbers:
# 
# `1.0 == 0.99999999999999999` is true to the last bit.

# This can lead to numerical errors during calculations: $1000 (a - b) \neq 1000a - 1000b$

# In[8]:


1000.0 * 1.0 - 1000.0 * 0.9999999999999998


# In[9]:


1000.0 * (1.0 - 0.9999999999999998)


# *Both* results are wrong: `2e-13` is the correct answer.
# 
# The size of the error will depend on the magnitude of the floating points:

# In[10]:


1000.0 * 1e5 - 1000.0 * 0.9999999999999998e5


# The result should be `2e-8`.

# ## Comparing floating points
# 
# Use the "approx", for a default of a relative tolerance of $10^{-6}$

# In[11]:


from pytest import approx

assert 0.7 == approx(0.7 + 1e-7)


# Or be more explicit:

# In[12]:


magnitude = 0.7
assert 0.7 == approx(0.701, rel=0.1, abs=0.1)


# Choosing tolerances is a big area of debate: https://software-carpentry.org/blog/2014/10/why-we-dont-teach-testing.html

# ## Comparing vectors of floating points
# 
# Numerical vectors are best represented using [numpy](http://www.numpy.org/).

# In[13]:


from numpy import array, pi

vector_of_reals = array([0.1, 0.2, 0.3, 0.4]) * pi


# Numpy ships with a number of assertions (in `numpy.testing`) to make
# comparison easy:

# In[14]:


from numpy import array, pi
from numpy.testing import assert_allclose

expected = array([0.1, 0.2, 0.3, 0.4, 1e-12]) * pi
actual = array([0.1, 0.2, 0.3, 0.4, 2e-12]) * pi
actual[:-1] += 1e-6
assert_allclose(actual, expected, rtol=1e-5, atol=1e-8)


# It compares the difference between `actual` and `expected` to ``atol + rtol * abs(expected)``.
