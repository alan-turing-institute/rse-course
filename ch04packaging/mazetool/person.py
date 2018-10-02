
class Person(object):
    def __init__(self, name, room = None):
        self.name=name
        self.room=room
    
    def use(self, exit):
        self.room.occupancy -= 1
        destination=exit.target
        destination.occupancy +=1
        self.room=destination
        print(self.name, "goes", exit.name, "to the", destination.name)
    
    def wander(self):
        exit = self.room.random_valid_exit()
        if exit:
            self.use(exit)
            
    def describe(self):
        print(self.name, "is in the", self.room.name)
