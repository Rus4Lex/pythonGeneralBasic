from Node import *

class HomeNode(Node):
    def __init__(self):
        super().__init__(self)
        self.floor_count = 0
        self.outrooms = []
        self.maxID = 0

    def get_maxID(self):
        self.maxID += 1
        return self.maxID
    def add_floor(self):
        self.floor_count += 1
        self.__dict__[str(hex(self.floor_count))[2:]] = None