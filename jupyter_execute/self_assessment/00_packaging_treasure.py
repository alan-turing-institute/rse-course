#!/usr/bin/env python
# coding: utf-8

# # An Adventure In Packaging: An exercise in research software engineering.

# In this exercise, you will convert the already provided solution to the programming challenge defined in this Jupyter notebook, into a proper Python package.

# The code to actually solve the problem is already given, but as roughly sketched out code in a notebook.

# Your job will be to convert the code into a formally structured package, with unit tests, a command line interface, and demonstrating your ability to use `git` version control.

# First, we set out the problem we are solving, and it's informal solution. Next, we specify in detail the target for your tidy solution. Finally, to assist you in creating a good solution, we state the marks scheme we will use.

# # Treasure Hunting for Beginners: an AI testbed

# We are going to look at a simple game, a modified version of one with a [long history](https://en.wikipedia.org/wiki/Hunt_the_Wumpus). Games of this kind have been used as test-beds for development of artificial intelligence.
# 
# A *dungeon* is a network of connected *rooms*. One or more rooms contain *treasure*. Your character, the *adventurer*, moves between rooms, looking for the treasure.
# A *troll* is also in the dungeon. The troll moves between rooms at random. If the troll catches the adventurer, you lose. If you find treasure before being eaten, you win. (In this simple version, we do not consider the need to leave the dungeon.)
# 
# The starting rooms for the adventurer and troll are given in the definition of the dungeon.
# 
# The way the adventurer moves is called a *strategy*. Different strategies are more or less likely to succeed.
# 
# We will consider only one strategy this time - the adventurer will also move at random.
# 
# We want to calculate the probability that this strategy will be successful for a given dungeon.
# 
# We will use a "monte carlo" approach - simply executing the random strategy many times, and counting the proportion of times the adventurer wins.

# Our data structure for a dungeon will be somewhat familiar from the Maze example:

# In[1]:


dungeon1 = {
    "treasure": [1],  # Room 1 contains treasure
    "adventurer": 0,  # The adventurer starts in room 0
    "troll": 2,  # The troll starts in room 2
    "network": [
        [1],  # Room zero connects to room 1
        [0, 2],  # Room one connects to rooms 0 and 2
        [1],
    ],  # Room 2 connects to room 1
}


# So this example shows a 3-room linear corridor: with the adventurer at one end, the troll at the other, and the treasure in the middle.

# With the adventurer following a random walk strategy, we can define a function to update a dungeon:

# In[2]:


import random


def random_move(network, current_loc):
    targets = network[current_loc]
    return random.choice(targets)


# In[3]:


def update_dungeon(dungeon):
    dungeon["adventurer"] = random_move(dungeon["network"], dungeon["adventurer"])
    dungeon["troll"] = random_move(dungeon["network"], dungeon["troll"])


# In[4]:


update_dungeon(dungeon1)

dungeon1


# We can also define a function to test if the adventurer has won, died, or if the game continues:

# In[5]:


def outcome(dungeon):
    if dungeon["adventurer"] == dungeon["troll"]:
        return -1
    if dungeon["adventurer"] in dungeon["treasure"]:
        return 1
    return 0


# In[6]:


outcome(dungeon1)


# So we can loop, to determine the outcome of an adventurer in a dungeon:

# In[7]:


import copy


def run_to_result(dungeon):
    dungeon = copy.deepcopy(dungeon)
    max_steps = 1000
    for _ in range(max_steps):
        result = outcome(dungeon)
        if result != 0:
            return result
        update_dungeon(dungeon)
    # don't run forever, return 0 (e.g. if there is no treasure and the troll can't reach the adventurer)
    return result


# In[8]:


dungeon2 = {
    "treasure": [1],  # Room 1 contains treasure
    "adventurer": 0,  # The adventurer starts in room 0
    "troll": 2,  # The troll starts in room 2
    "network": [
        [1],  # Room zero connects to room 1
        [0, 2],  # Room one connects to rooms 0 and 2
        [1, 3],  # Room 2 connects to room 1 and 3
        [2],
    ],  # Room 3 connects to room 2
}


# In[9]:


run_to_result(dungeon2)


# Note that we might get a different result sometimes, depending on how the adventurer moves, so we need to run multiple times to get our probability:

# In[10]:


def success_chance(dungeon):
    trials = 10000
    successes = 0
    for _ in range(trials):
        outcome = run_to_result(dungeon)
        if outcome == 1:
            successes += 1
    success_fraction = successes / trials
    return success_fraction


# In[11]:


success_chance(dungeon2)


# Make sure you understand why this number should be a half, given a large value for `trials`.

# In[12]:


dungeon3 = {
    "treasure": [2],  # Room 2 contains treasure
    "adventurer": 0,  # The adventurer starts in room 0
    "troll": 4,  # The troll starts in room 4
    "network": [
        [1],  # Room zero connects to room 1
        [0, 2],  # Room one connects to rooms 0 and 2
        [1, 3],  # Room 2 connects to room 1 and 3
        [2, 4],  # Room 3 connects to room 2 and 4
        [3],
    ],  # Room 4 connects to room 3
}


# In[13]:


success_chance(dungeon3)


# [Not for credit] Do you understand why this number should be 0.4? Hint: The first move is always the same. In the next state, a quarter of the time, you win. 3/8 of the time, you end up back where you were before. The rest of the time, you lose (eventually). You can sum the series: $\frac{1}{4}(1+\frac{3}{8}+(\frac{3}{8})^2+...)=\frac{2}{5}$.

# # Packaging the Treasure: your exercise

# If you are following the guidelines from earlier lectures, you will use a single top-level folder with a sensible name. This top level folder should contain all the parts of your solution.

# Inside your top level folder, you should create a `setup.py` file to make the code installable. You should also create some other files, per the lectures, that should be present in all research software packages. (Hint, there are three of these.)

# Your tidied-up version of the solution code should be in a sub-folder called `adventure` which will be the python package itself. It will contain an `__init__.py` file, and the code itself should be in a file called `dungeon.py`. This should define a class `Dungeon`: instead of a data structure and associated functions, you must refactor this into a class and methods.
# 
# Thus, if you run python in your top-level folder, you should be able to `from adventure.dungeon import Dungeon`.

# You must create a command-line entry point, called `hunt`. This should use the entry_points facility in `setup.py`, to point toward a module designed for use as the entry point, in `adventure/command.py`. This should use the `Argparse` library. When invoked with `hunt mydungeon.yml --samples 500` the command must print on standard output the probability of finding the treasure in the specified dungeon, using the random walk strategy, after the specified number of test runs.

# The `dungeon.yml` file should be a yml file containing a structure representing the dungeon state. Use the same structure as the sample code above, even though you'll be building a `Dungeon` object from this structure rather than using it directly.

# You must create unit tests which cover a number of examples. These should be defined in `adventure/tests/test_dungeon.py`. Don't forget to add an __init.py__ file to that folder too, so that at the top of the test file you can " `from ..dungeon import Dungeon`." If your unit tests use a fixture file to DRY up tests, this must be called `adventure/tests/fixtures.yml`. For example, this could contain a yaml array of many dungeon structures.

# You should `git init` as soon as you create the top-level folder, and `git commit` your work regularly as the exercise progresses.

# # Suggested Marking Scheme

# If you want to self-assess your solution you can consider using the marking scheme below.

# * Code in dungeon.py, implementing the random walk strategy: (**5 marks**)
#   * Which works. (**1 mark**)
#   * Cleanly laid out and formatted - PEP8. (**1 mark**)
#   * Defining the class `Dungeon` with a valid object oriented structure. (**1 mark**)
#   * Breaking down the solution sensibly into subunits. (**1 mark**)
#   * Structured so that it could be used as a base for other strategies. (**1 mark**)
# * Command line entry point: (**4 marks**)
#   * Accepting a dungeon definition text file as input. (**1 mark**)
#   * With an optional parameter to control sample size. (**1 mark**)
#   * Which prints the result to standard out. (**1 mark**)
#   * Which correctly uses the `Argparse` library. (**1 mark**)
#   * Which is itself cleanly laid out and formatted. (**1 mark**)
# * setup.py file: (**5 marks**)
#   * Which could be used to `pip install` the project. (**1 mark**)
#   * With appropriate metadata, including version number and author. (**1 mark**)
#   * Which packages code (but not tests), correctly. (**1 mark**)
#   * Which specifies library dependencies. (**1 mark**)
#   * Which points to the entry point function. (**1 mark**)
# * Three other metadata files: (**3 marks**)
#   * Hint: Who did it, how to reference it, who can copy it.
# * Unit tests: (**5 marks**)
#   * Which test some obvious cases. (**1 mark**)
#   * Which correctly handle approximate results within an appropriate tolerance. (**1 mark**)
#   * Which test how the code fails when invoked incorrectly. (**1 mark**)
#   * Which use a fixture file or other approach to avoid overly repetitive test code. (**1 mark**)
#   * Which are themselves cleanly laid out code. (**1 mark**)
# * Version control: (**2 marks**)
#   * Sensible commit sizes. (**1 mark**)
#   * Appropriate commit comments. (**1 mark**)

# Total: **25 marks**
