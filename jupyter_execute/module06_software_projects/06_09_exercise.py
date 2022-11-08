#!/usr/bin/env python
# coding: utf-8

# # 6.9 Exercise: Packaging Troll Treasure

# We are going to look at a simplified version of a game with a [long history](https://en.wikipedia.org/wiki/Hunt_the_Wumpus). Games of this kind have been used as test-beds for development of artificial intelligence.
# 
# A *dungeon* is a network of connected *rooms* on a square grid. One or more rooms contain *treasure*. Your character, the *adventurer*, moves between rooms, looking for the treasure.
# A *troll* is also in the dungeon and moves between rooms. If the troll catches the adventurer, you lose. If you find treasure before being eaten, you win. (In this simple version, we do not consider the need to leave the dungeon.)
# 
# The starting rooms for the adventurer and troll are given in the definition of the dungeon.
# 
# The way the adventurer and troll move is called a *strategy*. Different strategies are more or less likely to succeed. There are two strategies in the provided code - random movement, and movement controlled by human input.
# 
# The code provides a function to play a single game, or to simulate many games and estimate the probability the adventurer or troll wins.
# 
# In this exercise, you will convert the code provided in this Jupyter notebook into a proper Python package.

# ## What to do
# 
# Using the course material from this module to help:
# 
# **1.** Briefly familiarise yourself with the code below and how it works/runs, focusing on the different classes and functions that are defined rather than the implementation details. And try running a game in the notebook (see the [Playing Games](#playing-games) section).
# 
# **2.** Make a directory for your project
# 
# 
# **3.** Create a directory to contain your package (in your project directory) and copy the code from this notebook to it using multiple `.py` files. Remember to add `__init__.py` file(s).
# 
# 
# **4.** Create a `pyproject.toml` file to specify the metadata and dependencies for the package. The dependencies are [PyYAML](https://pypi.org/project/PyYAML/) version 6.0 and [art](https://pypi.org/project/art/) version 5.7.
# 
# 
# **5.** Create a virtual environment and activate it
# 
# 
# **6.** Install the package in your virtual environment.
# 
# - ⚠️ You might get an error that says something like `error: Multiple top-level packages discovered in a flat-layout`. This is because `setuptools` has detected multiple directories that look like python packages and doesn't know which one to choose. You should be able to fix this by adding (only) one of these sections to your `pyproject.toml` file:
# 
#   ```yaml
#   [tool.setuptools]
#   packages = ["<my_package_directory>"]
#   ```
# 
#   _**or**_
# 
#   ```yaml
#   [tool.setuptools.packages]
#   include = ["<my_package_directory>*"]
#   ```
#   
#   replacing `<my_package_directory>` with the name of the directory that contains your package (`.py` files)
# 
# **7.** Check that you can import your package and run a script to play a game.
# 
# 
# **8.** Make a command-line interface:
#   - Use `argparse` to create a function that can be called from the command-line with the path to a dungeon YAML file, and the option to either run a single game or calculate probabilities.
#   - Add a script to call your function to the `[project.scripts]` section of `pyproject.toml`
#   - Reinstall your package and verify the executable you defined can now be run from a terminal.
# 
# ### Extensions
# 
# If you'd like to take this further here are some other things you could try, depending on your interests:
# 
# **9.** Create a GitHub repo for your project. Try installing the package from GitHub.
# 
# 
# **10.** Add `README`, `LICENSE`, and `CITATION` files to your project directory.
# 
# 
# **11.** Improve documentation
#   - Add docstrings to functions to explain what they do, their inputs, and outputs (e.g. in numpydoc format)
#   - Build a documentaion web-site with sphinx
#   - Host the documentation on GitHub pages
# 
# **12.** Add unit tests
#   - Write unit tests, such as to verify the outcomes of the provided `test_xxx.yml` dungeon files.
#   - Add `pytest` as a development dependency for your package (and install it)
#   - Run the tests and verify they pass
# 
# 
# **13.** Improve or extend the code (you may like to revisit this after the next module):
#   - Specify your own dungeons or create a function to auto-generate them
#   - Create new movement behaviour classes for adventurers and trolls
#   - Look for places the code could be refactored (to reduce repetition, for example)
# 

# ## Code

# ### Rooms
# 
# The `direction` function determines the direction from grid point `a` to grid point `b` (length two tuples, x and y coordinte) if they are neighbouring points in the grid, or `None` otherwise:

# In[1]:


def direction(point_a, point_b):
    """
    Returns the direction from point_a to point_b, or None if they
    are not neighhbouring grid points.
    """
    if point_b == point_a:
        return "nowhere"
    if point_b[1] == point_a[1]:
        if point_b[0] == point_a[0] - 1:
            return "left"
        if point_b[0] == point_a[0] + 1:
            return "right"
    if point_b[0] == point_a[0]:
        if point_b[1] == point_a[1] - 1:
            return "up"
        if point_b[1] == point_a[1] + 1:
            return "down"

    return None


# A `Room` has a location (point) and optionally can link to other `Room`s at neighbouring grid points. :

# In[2]:


class Room:
    def __init__(self, point, links=None):
        self.point = tuple(point)  # grid point of this room
        self.links = links  # other rooms this rooms connects to
        self._validate_links()

    def __contains__(self, point):
        """
        `(x, y) in room_instance` returns `True` if `room_instance` has a link to
        a room at point `(x, y)`
        """
        return point in [link.point for link in self.links]

    def _validate_links(self):
        """
        Verifies all linked rooms are at neighbouring grid points
        """
        if not self.links:
            return
        for link in self.links:
            if not direction(self.point, link.point):
                raise ValueError(
                    f"Invalid link: {link.point} is not connected to {self.point}"
                )


# `Rooms` is a collection of rooms (that must be on a square grid), with each room stored in a dictionary keyed by its `(x, y)` coordinate (point):

# In[3]:


class Rooms:
    """
    Collection of rooms
    """

    def __init__(self, rooms):
        # rooms dictionary keyed by (x, y) coordinate (grid cell indices)
        self.rooms = {r.point: r for r in rooms}

    def __iter__(self):
        """
        Allows Rooms objects to be iterated over (see Module 7)
        """
        return iter(self.rooms.values())

    def __getitem__(self, point):
        """
        rooms[(x, y)] will retrieve the room at coordinate (x, y) (where
        rooms is an instance of the Rooms class)
        """
        return self.rooms[point]

    def __contains__(self, point):
        """
        (x, y) in rooms will return True if a room at coordinates (x, y)
        is in rooms (where rooms is an instance of the Rooms class)
        """
        return point in self.rooms

    @classmethod
    def from_list(cls, room_list):
        rooms = [
            Room(room["point"], [Room(link) for link in room["links"]])
            for room in room_list
        ]
        return cls(rooms)


# ### Treasure

# Treausre has a location (point) and a single character symbol to represent it when printing dungeon maps:

# In[4]:


class Treasure:
    def __init__(self, point, symbol):
        self.point = tuple(point)  # (x, y) grid location of the treasure
        self.symbol = symbol  # single char symbol to show the treasure on dungeon maps

    @classmethod
    def from_dict(cls, treasure_dict):
        return cls(treasure_dict["point"], treasure_dict["symbol"])


# ### Agents

# The `Agent` class stores general properties used by all agents (trolls or adventurers):

# In[5]:


class Agent:
    """
    Base functionality to create and load (but not move) an Agent
    """

    def __init__(self, point, name, symbol, verbose=True, allow_wait=True, **kwargs):
        self.point = tuple(point)  # (x, y) grid location of the agent
        self.name = name  # e.g. adventurer or troll
        self.symbol = symbol  # single char symbol to show the agent on dungeon maps
        self.verbose = verbose  # print output on agent behaviour if True
        self.allow_wait = allow_wait  # allow the agent to move nowhere

    def move(self, rooms):
        raise NotImplementedError("Use an Agent base class")

    @classmethod
    def from_dict(cls, agent_dict):
        return cls(
            agent_dict["point"],
            agent_dict["name"],
            agent_dict["symbol"],
            allow_wait=agent_dict["allow_wait"],
        )


# `RandomAgent`s choose to move to a connecting room at random (or stay where they are):

# In[6]:


import random


class RandomAgent(Agent):
    """
    Agent that makes random moves
    """

    def move(self, rooms):
        if not rooms[self.point].links:
            # this room isn't linked to anything, can't move
            if self.verbose:
                print(f"{self.name} is trapped")
            return

        # pick a random room to move to
        options = rooms[self.point].links
        if self.allow_wait:
            options.append(self)
        new_room = random.choice(options)

        if self.verbose:
            move = direction(self.point, new_room.point)
            print(f"{self.name} moves {move}")
        self.point = new_room.point


# `HumanAgent`s ask the user where to move next:

# In[7]:


class HumanAgent(Agent):
    """
    Agent that prompts the user where to move next
    """

    def move(self, rooms):
        if not rooms:
            if self.verbose:
                print(f"{self.name} is trapped")
            return
        # populate movement options depending on available rooms
        if self.allow_wait:
            options = ["wait"]
        else:
            options = []
        if (self.point[0] - 1, self.point[1]) in rooms:
            options.append("left")
        if (self.point[0] + 1, self.point[1]) in rooms:
            options.append("right")
        if (self.point[0], self.point[1] - 1) in rooms:
            options.append("up")
        if (self.point[0], self.point[1] + 1) in rooms:
            options.append("down")

        # prompt user for movement input
        choice = None
        while choice not in options:
            choice = input(f"Where will {self.name} move \n{options}? ")

        # move the agent
        if choice == "left":
            self.point = (self.point[0] - 1, self.point[1])
        elif choice == "right":
            self.point = (self.point[0] + 1, self.point[1])
        elif choice == "up":
            self.point = (self.point[0], self.point[1] - 1)
        elif choice == "down":
            self.point = (self.point[0], self.point[1] + 1)


# ### Dungeons
# 
# `Dungeon` have rooms, a piece of treasure, an adventurer, and a troll, and provide the functionality to update the agents, check whether the treasure or adventurer have found, and to draw a map of the dungeon:

# In[8]:


import yaml


class Dungeon:
    """
    Dungeon with:
    - Connected set of rooms on a square grid
    - The location of some treasure
    - An adventurer agent with an initial position
    - A troll agent with an initial position
    """

    def __init__(self, rooms, treasure, adventurer, troll, verbose=True):
        self.rooms = rooms
        self.treasure = treasure
        self.adventurer = adventurer
        self.troll = troll
        self.verbose = True

        # the extent of the square grid
        self.xlim = (
            min(r.point[0] for r in self.rooms),
            max(r.point[0] for r in self.rooms),
        )
        self.ylim = (
            min(r.point[1] for r in self.rooms),
            max(r.point[1] for r in self.rooms),
        )

        self._validate()

    def _validate(self):
        if self.treasure.point not in self.rooms:
            raise ValueError(f"Treasure{self.treasure.point} is not in the dungeon")
        if self.adventurer.point not in self.rooms:
            raise ValueError(
                f"{self.adventure.name}{treasure.point} is not in the dungeon"
            )
        if self.troll.point not in self.rooms:
            raise ValueError(f"{self.troll.name}{treasure.point} is not in the dungeon")

    @classmethod
    def from_file(cls, path):
        with open(path) as f:
            spec = yaml.safe_load(f)

        rooms = Rooms.from_list(spec["rooms"])
        treasure = Treasure.from_dict(spec["treasure"])

        agent_keys = ["adventurer", "troll"]
        agents = {}
        for agent in agent_keys:
            if spec[agent]["type"] == "random":
                agent_class = RandomAgent
            elif spec[agent]["type"] == "human":
                agent_class = HumanAgent
            else:
                raise ValueError(f"Unknown agent type {spec[agent]['type']}")
            agents[agent] = agent_class(**spec[agent])

        return cls(rooms, treasure, agents["adventurer"], agents["troll"])

    def update(self):
        """
        Move the adventurer and the troll
        """
        self.adventurer.move(self.rooms)
        self.troll.move(self.rooms)
        if self.verbose:
            print()
            self.draw()

    def outcome(self):
        """
        Check whether the adventurer found the treasure or the troll
        found the adventurer
        """
        if self.adventurer.point == self.troll.point:
            return -1
        if self.adventurer.point == self.treasure.point:
            return 1
        return 0

    def set_verbose(self, verbose):
        """Set whether to print output"""
        self.verbose = verbose
        self.adventurer.verbose = verbose
        self.troll.verbose = verbose

    def draw(self):
        """Draw a map of the dungeon"""
        layout = ""

        for y in range(self.ylim[0], self.ylim[1] + 1):
            for x in range(self.xlim[0], self.xlim[1] + 1):
                # room and character symbols
                if (x, y) in self.rooms:
                    if self.troll.point == (x, y):
                        layout += self.troll.symbol
                    elif self.adventurer.point == (x, y):
                        layout += self.adventurer.symbol
                    elif self.treasure.point == (x, y):
                        layout += self.treasure.symbol
                    else:
                        layout += "o"
                else:
                    layout += " "

                # horizontal connections
                if ((x, y) in self.rooms) and (((x + 1), y) in self.rooms[(x, y)]):
                    layout += " - "
                else:
                    layout += "   "

            # vertical connections
            if y < self.ylim[1]:
                layout += "\n"
                for x in range(self.xlim[0], self.xlim[1] + 1):
                    if ((x, y) in self.rooms) and ((x, y + 1) in self.rooms[(x, y)]):
                        layout += "|"
                    else:
                        layout += " "
                    if x < self.xlim[1]:
                        layout += "   "
                layout += "\n"

        print(layout)


# ### Games
# 
# The `Game` class runs a dungeon until the adventurer or troll wins, or calls a draw if neither wins in a given number of steps, and can simulate many games to estimate outcome probabilities:

# In[9]:


import copy

from art import tprint


class Game:
    def __init__(self, dungeon):
        self.dungeon = dungeon

    def preamble(self):
        tprint("Troll Treasure\n", font="small")
        print(
            f"""
The {self.dungeon.adventurer.name} is looking for treasure in a mysterious dungeon.
Will they succeed or be dinner for the {self.dungeon.troll.name} that lurks there?

The map of the dungeon is below:
o : an empty room
o - o : connected rooms
{self.dungeon.troll.symbol} : {self.dungeon.troll.name}
{self.dungeon.adventurer.symbol} : {self.dungeon.adventurer.name}
{self.dungeon.treasure.symbol} : the treasure
            """
        )

    def run(self, max_steps=1000, verbose=True, start_prompt=False):
        dungeon = copy.deepcopy(self.dungeon)
        dungeon.set_verbose(verbose)
        if verbose:
            self.preamble()
            dungeon.draw()
            if start_prompt:
                input("\nPress enter to continue...")
            else:
                print("\nLet the hunt begin!")

        for turn in range(max_steps):
            result = dungeon.outcome()
            if result != 0:
                if verbose:
                    if result == 1:
                        print(
                            f"\n{self.dungeon.adventurer.name} gets the treasure and returns a hero!"
                        )
                        tprint("WINNER", font="small")
                    elif result == -1:
                        print(f"\n{self.dungeon.troll.name} will eat tonight!")
                        tprint("GAME OVER", font="small")
                return result
            if verbose:
                print(f"\nTurn {turn + 1}")
            dungeon.update()
        # no outcome in max steps (e.g. no treasure and troll can't reach adventurer)
        if verbose:
            print(
                f"\nNo one saw {self.dungeon.adventurer.name} or {self.dungeon.troll.name} again."
            )
            tprint("STALEMATE", font="small")

        return result

    def probability(self, trials=10000, max_steps=1000, verbose=False):
        outcomes = {-1: 0, 0: 0, 1: 0}
        for _ in range(trials):
            result = self.run(max_steps=max_steps, verbose=False)
            outcomes[result] += 1
        for result in outcomes:
            outcomes[result] = outcomes[result] / trials
        return outcomes


# ## Playing Games

# ### Dungeon YAML files
# 
# Dungeons can be specified with YAML files, and we have provided a few examples in the `dungeons/` directory:

# In[10]:


import os

os.listdir("dungeons")


# The files starting `test_` are simlper dungeons with known outcome proabilities (which could be used in unit testing, for example).

# ### Run a single game

# In[11]:


d = Dungeon.from_file("dungeons/dungeon.yml")
g = Game(d)
g.run(max_steps=10)


# ### Estimate outcome probabilities

# In[12]:


d = Dungeon.from_file("dungeons/dungeon.yml")
g = Game(d)
g.probability(max_steps=10)
# -1: troll wins, 0: stalemate, +1: adventurer wins

