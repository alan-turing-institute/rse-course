#!/usr/bin/env python
# coding: utf-8

# # 7.8 Exercise: Refactoring The Bad Boids
# 
# We have written some _very bad_ code implementing our Boids flocking example. We first looked at the Boids [in Module 3](../module03/module03_research_data_in_python/03_05_boids.html) (but you don't need to have seen the previous example to do this exercise). The task is to refactor and improve this initial implementation.
# 

# ## 7.8.1 Get the bad boids code
# 
# Here's the Github link: https://github.com/alan-turing-institute/bad-boids
# 
# 
# Please [fork it](https://docs.github.com/en/get-started/quickstart/fork-a-repo) on GitHub, and clone your fork:
# 
# ``` bash
# git clone git@github.com:yourname/bad-boids.git 
# # OR git clone https://github.com/yourname/bad-boids.git
# ```

# ## 7.8.2 Familiarise yourself with the code
# 
# Have a look at the `boids.py` file in the `bad-boids` directory and quickly review how it's implemented.
# 
# Then run the code:
# 
# ``` bash
# cd bad_boids
# python boids.py
# ```
# 
# You should be able to see some birds flying around, and then disappearing as they leave the window, like this:
# 
# <img src="bad_boids_animation.gif" width="600"/>
# 

# ## 7.8.3 Regression Test

# 
# First, have a look at the regression test we made in the `record_fixture.py` file. This saves the before and after state for one iteration of some boids, to the file `fixture.yml`.
# 
# Then, we used this saved state to define a regression test in `test_boids.py`.
# 
# Check the tests pass by running pytest from the `bad-boids` directory:
# 
# ```bash
# pytest
# ```
# 

# ## 7.8.4 Start refactoring

# Transform bad boids **gradually** into better code, while making sure it still works, using a refactoring approach.
# 
# Each time you make a change:
# 
# - Ensure the regression test still passes (you may need to update it to reflect any changed functions/classes in your code, but you _**shouldn't**_ change the `fixture.yml` file - the new implementation must reproduce the same results)
# - Do a git commit on your fork, and write a commit message explaining the refactoring you did.
# 
# Try to keep the changes as small as possible.
# 
# If your refactoring creates any units (functions, modules, or classes), **write a unit test** for the unit (it's a good idea to not rely only on regression testing).
# 
# Don't worry about the performance of the code for this exercise. That's a topic for the "Programming for Speed" module later.

# ### Refactoring Ideas
# 
# You probably won't have time to do all these in the session, but here are some refactorings we've seen in the module that you can try to apply here. We've loosely ordered them by where we'd suggest starting, but feel free to focus on the ones you're most interested in:
# 
# - Use linters to check and enforce a consistent style
# - Ensure the code follows PEP8 conventions (e.g. for naming and whitespace)
# - Consider whether any of the code "smells" and refactorings from [07_04_refactoring](07_04_refactoring.html) apply here
# - Consider whether there is structure in the code that could be refactored into classes (see [07_05_object_oriented_design](07_05_object_oriented_design.html) for ideas)
# - Add type annotations

# ## 7.8.5 Extensions
# 
# You may also like to apply some of what we've learned in previous modules, for example:
# 
# - Ensure dependencies are specified correctly
# - Run tests and checks automatically, for example with a GitHub actions workflow
# - Improve documentation
# - Make the code into a Python package (e.g. see [module06_software_projects/06_04_packaging](../module06_software_projects/06_04_packaging.html#using-setuptools))
