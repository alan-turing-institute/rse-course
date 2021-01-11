
class Exit(object):
    def __init__(self, name, target):
        self.name = name
        self.target = target
    
    def valid(self):
        return self.target.has_space()
