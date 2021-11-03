from .room import Room
from .person import Person


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
        house.describe()
        print()
        house.wander()
        print()

    def simulate(self, steps):
        for _ in range(steps):
            self.step()
