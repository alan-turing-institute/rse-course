#!/usr/bin/env python
# coding: utf-8

# # Testing

# ## Introduction

# ### A few reasons not to do testing

# Sensibility                          | Sense
# ------------------------------------ | -------------------------------------
# **It's boring**                      |  *Maybe*
# **Code is just a one off throwaway** |  *As with most research codes*
# **No time for it**                   |  *A bit more code, a lot less debugging*
# **Tests can be buggy too**           |  *See above*
# **Not a professional programmer**    |  *See above*
# **Will do it later**                 | *See above*

# ### A few reasons to do testing
# 
# * **lazyness** *testing saves time*
# * **peace of mind** *tests (should) ensure code is correct*
# * **runnable specification** *best way to let others know what a function should do and
#     not do*
# * **reproducible debugging** *debugging that happened and is saved for later reuse*
# * code structure / **modularity** *since the code is designed for at least two situations*
# * easier to modify *since results can be tested*

# ### Not a panacea
# 
# > Trying to improve the quality of software by doing more testing is like trying to lose weight by
# > weighting yourself more often.
#     - Steve McConnell

#  * Testing won't corrrect a buggy code
#  * Testing will tell you were the bugs are...
#  * ... if the test cases *cover* the bugs

# ### Tests at different scales
# 
# Level of test           | Area covered by test
# ----------------------- | ---------------------------------------------------------
# **Unit testing**        | smallest logical block of work (often < 10 lines of code)
# **Component testing**   | several logical blocks of work together
# **Integration testing** | all components together / whole program
# 
# 
# * Always start at the smallest scale! 
# * If a unit test is too complicated, go smaller.

# ### Legacy code hardening
# 
# * Very difficult to create unit-tests for existing code
# * Instead we make a **regression test**
# * Run program as a black box:
# 
# ```
# setup input
# run program
# read output
# check output against expected result
# ```
# 
# * Does not test correctness of code
# * Checks code is as similarly wrong on day N as day 0

# ### Testing vocabulary
# 
# * **fixture**: input data
# * **action**: function that is being tested
# * **expected result**: the output that should be obtained
# * **actual result**: the output that is obtained
# * **coverage**: proportion of all possible paths in the code that the tests take

# ### Branch coverage:

# ```python
# if energy > 0:
#     ! Do this 
# else:
#     ! Do that
# ```

# Is there a test for both `energy > 0` and `energy <= 0`?
