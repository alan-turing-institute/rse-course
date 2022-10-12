#!/usr/bin/env python
# coding: utf-8

# # 2.3 Defining your own classes

# *Estimated time for this notebook: 20 minutes*

# ## 2.3.1 User Defined Types

# A **class** is a user-programmed Python type.

# It is defined like:

# In[1]:


class Room:
    pass


# Just as with other python types, you use the name of the type as a function to make a variable of that type:

# In[2]:


zero = int()
type(zero)


# In[3]:


myroom = Room()
type(myroom)


# In the jargon, we say that an **object** is an **instance** of a particular **class**.
# 
# `__main__` is the name of the scope in which top-level code executes, where we've defined the class `Room`.

# Once we have an object with a type of our own devising, we can add properties at will:

# In[4]:


myroom.name = "Living"


# In[5]:


myroom.name


# The most common use of a class is to allow us to group data into an object in a way that is 
# easier to read and understand than organising data into lists and dictionaries.

# In[6]:


myroom.capacity = 3
myroom.occupants = ["James", "Sue"]


# ## 2.3.2 Methods

# So far, our class doesn't do much!

# We define functions **inside** the definition of a class, in order to give them capabilities, just like the methods on built-in
# types.

# In[7]:


class Room:
    def overfull(self):
        return len(self.occupants) > self.capacity


# In[8]:


myroom = Room()
myroom.capacity = 3
myroom.occupants = ["James", "Sue"]


# In[9]:


myroom.overfull()


# In[10]:


myroom.occupants.append(["Clare"])


# In[11]:


myroom.occupants.append(["Bob"])


# In[12]:


myroom.overfull()


# When we write methods, we always write the first function argument as `self`, to refer to the object instance itself,
# the argument that goes "before the dot".

# This is just a convention for this variable name, not a keyword. You could call it something else if you wanted.

# ## 2.3.3 Constructors

# Normally, though, we don't want to add data to the class attributes on the fly like that. 
# Instead, we define a **constructor** that converts input data into an object. 

# In[13]:


class Room:
    def __init__(self, name, exits, capacity, occupants=[]):
        self.name = name
        self.occupants = occupants  # Note the default argument, occupants start empty
        self.exits = exits
        self.capacity = capacity

    def overfull(self):
        return len(self.occupants) > self.capacity


# In[14]:


living = Room("Living Room", {"north": "garden"}, 3)


# In[15]:


living.capacity


# Methods which begin and end with **two underscores** in their names fulfil special capabilities in Python, such as
# constructors.

# ## 2.3.4 Object-oriented design

# In building a computer system to model a problem, therefore, we often want to make:
# 
# * classes for each *kind of thing* in our system
# * methods for each *capability* of that kind
# * properties (defined in a constructor) for each *piece of information describing* that kind
# 

# For example, the below program might describe our "Maze of Rooms" system:

# We define a "Maze" class which can hold rooms:

# In[16]:


class Maze:
    def __init__(self, name):
        self.name = name
        self.rooms = {}

    def add_room(self, room):
        room.maze = self  # The Room needs to know
        # which Maze it is a part of
        self.rooms[room.name] = room

    def occupants(self):
        return [
            occupant
            for room in self.rooms.values()
            for occupant in room.occupants.values()
        ]

    def wander(self):
        """Move all the people in a random direction"""
        for occupant in self.occupants():
            occupant.wander()

    def describe(self):
        for room in self.rooms.values():
            room.describe()

    def step(self):
        self.describe()
        print("")
        self.wander()
        print("")

    def simulate(self, steps):
        for _ in range(steps):
            self.step()


# And a "Room" class with exits, and people:

# In[17]:


class Room:
    def __init__(self, name, exits, capacity, maze=None):
        self.maze = maze
        self.name = name
        self.occupants = {}  # Note the default argument, occupants start empty
        self.exits = exits  # Should be a dictionary from directions to room names
        self.capacity = capacity

    def has_space(self):
        return len(self.occupants) < self.capacity

    def available_exits(self):
        return [
            exit
            for exit, target in self.exits.items()
            if self.maze.rooms[target].has_space()
        ]

    def random_valid_exit(self):
        import random

        if not self.available_exits():
            return None
        return random.choice(self.available_exits())

    def destination(self, exit):
        return self.maze.rooms[self.exits[exit]]

    def add_occupant(self, occupant):
        occupant.room = self  # The person needs to know which room it is in
        self.occupants[occupant.name] = occupant

    def delete_occupant(self, occupant):
        del self.occupants[occupant.name]

    def describe(self):
        if self.occupants:
            print(f"{self.name}: " + " ".join(self.occupants.keys()))


# We define a "Person" class for room occupants:

# In[18]:


class Person:
    def __init__(self, name, room=None):
        self.name = name

    def use(self, exit):
        self.room.delete_occupant(self)
        destination = self.room.destination(exit)
        destination.add_occupant(self)
        print(
            "{some} goes {action} to the {where}".format(
                some=self.name, action=exit, where=destination.name
            )
        )

    def wander(self):
        exit = self.room.random_valid_exit()
        if exit:
            self.use(exit)


# And we use these classes to define our people, rooms, and their relationships:

# In[19]:


james = Person("James")
sue = Person("Sue")
bob = Person("Bob")
clare = Person("Clare")


# In[20]:


living = Room(
    "livingroom", {"outside": "garden", "upstairs": "bedroom", "north": "kitchen"}, 2
)
kitchen = Room("kitchen", {"south": "livingroom"}, 1)
garden = Room("garden", {"inside": "livingroom"}, 3)
bedroom = Room("bedroom", {"jump": "garden", "downstairs": "livingroom"}, 1)


# In[21]:


house = Maze("My House")


# In[22]:


for room in [living, kitchen, garden, bedroom]:
    house.add_room(room)


# In[23]:


living.add_occupant(james)


# In[24]:


garden.add_occupant(sue)
garden.add_occupant(clare)


# In[25]:


bedroom.add_occupant(bob)


# And we can run a "simulation" of our model:

# In[26]:


house.simulate(3)


# ## 2.3.5 Alternative object models

# There are many choices for how to design programs to do this. Another choice would be to separately define exits as a different class from rooms. This way, 
# we can use arrays instead of dictionaries, but we have to first define all our rooms, then define all our exits.

# In[27]:


class Maze:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.occupants = []

    def add_room(self, name, capacity):
        result = Room(name, capacity)
        self.rooms.append(result)
        return result

    def add_exit(self, name, source, target, reverse=None):
        source.add_exit(name, target)
        if reverse:
            target.add_exit(reverse, source)

    def add_occupant(self, name, room):
        self.occupants.append(Person(name, room))
        room.occupancy += 1

    def wander(self):
        "Move all the people in a random direction"
        for occupant in self.occupants:
            occupant.wander()

    def describe(self):
        for occupant in self.occupants:
            occupant.describe()

    def step(self):
        self.describe()
        print("")
        self.wander()
        print("")

    def simulate(self, steps):
        for _ in range(steps):
            self.step()


# In[28]:


class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.occupancy = 0
        self.exits = []

    def has_space(self):
        return self.occupancy < self.capacity

    def available_exits(self):
        return [exit for exit in self.exits if exit.valid()]

    def random_valid_exit(self):
        import random

        if not self.available_exits():
            return None
        return random.choice(self.available_exits())

    def add_exit(self, name, target):
        self.exits.append(Exit(name, target))


# In[29]:


class Person:
    def __init__(self, name, room=None):
        self.name = name
        self.room = room

    def use(self, exit):
        self.room.occupancy -= 1
        destination = exit.target
        destination.occupancy += 1
        self.room = destination
        print(
            "{some} goes {action} to the {where}".format(
                some=self.name, action=exit.name, where=destination.name
            )
        )

    def wander(self):
        exit = self.room.random_valid_exit()
        if exit:
            self.use(exit)

    def describe(self):
        print("{who} is in the {where}".format(who=self.name, where=self.room.name))


# In[30]:


class Exit:
    def __init__(self, name, target):
        self.name = name
        self.target = target

    def valid(self):
        return self.target.has_space()


# In[31]:


house = Maze("My New House")


# In[32]:


living = house.add_room("livingroom", 2)
bed = house.add_room("bedroom", 1)
garden = house.add_room("garden", 3)
kitchen = house.add_room("kitchen", 1)


# In[33]:


house.add_exit("north", living, kitchen, "south")


# In[34]:


house.add_exit("upstairs", living, bed, "downstairs")


# In[35]:


house.add_exit("outside", living, garden, "inside")


# In[36]:


house.add_exit("jump", bed, garden)


# In[37]:


house.add_occupant("James", living)
house.add_occupant("Sue", garden)
house.add_occupant("Bob", bed)
house.add_occupant("Clare", garden)


# In[38]:


house.simulate(3)


# This is a huge topic, about which many books have been written. The differences between these two designs are important, and will have long-term consequences for the project. That is the how we start to think about **software engineering**, as opposed to learning to program, and is an important part of this course.
