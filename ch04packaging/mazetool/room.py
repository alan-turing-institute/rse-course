from .exit import Exit


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
