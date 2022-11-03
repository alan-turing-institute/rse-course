#!/usr/bin/env python
# coding: utf-8

# # 5.0 Testing

# *Estimated time for this notebook: 5 minutes*

# ## Introduction
# 
# As we write code, we want to be sure that it does behaves the way we'd like it to - so we test it. Testing (and re-testing) our code is something that needs to be done regularly (ideally after every change to the code), comprehensively, quickly and reliably. In short testing is an task that is ideally suited to automation. 
# 
# We write additional code to test the behaviour for our main code. We use these terms to distinguish between the two types of code:
# 
# * "Production code" - the code that fulfills the purpose of the software, and is run by the end user.
# * "Test code" - additional code only used by software development team
# 
# **For this module we are focusing on _automated testing_.**

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
# > "Trying to improve the quality of software by doing more testing is like trying to lose weight by
# > weighting yourself more often." - Steve McConnell
# 
# * Testing won't correct a buggy code
# * Testing will tell you were the bugs are...
# * ... if (and only if) the test cases *cover* the scenarios that cause the bugs or occur.
# 
# Also, automated tests only test a narrow interpretation of quality software development. They do *not* help test that your software is _useful_ and help solves a users' problem. We will touch on this again in Module 06.
# 

# ### Tests at different scales
# 
# Level of test           | Area covered by test                                      | Notes
# ----------------------- | --------------------------------------------------------- | ---------------------
# **Unit testing**        | smallest logical block of work (often < 10 lines of code) | Unit tests should run fast (eg ~1/100th sec) so that they can be re-run regularly (eg every git commit). To achieve this they should not invoke network access or substantial disk access. 
# **Component testing**   | several logical blocks of work together                   | These can be useful where you need to tease out the expected/useful behaviour of 3rd party libraries.
# **Integration testing** | all components together / whole program                   | These can take longer to run, and can be run less often.
# 
# 
# * When writing new code (see below) always start by creating tests at the smallest scale (unit tests). 
# * If a unit test is too complicated to write, then consider adjusting your production code (possibly by breaking it down into smaller, individually testable functions). Ensuring that your production code is easy to test is a healthy habit.

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
