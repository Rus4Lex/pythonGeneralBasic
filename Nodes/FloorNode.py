from ApartmentNode import *
from random import randint as rint
#поверх
class FloorNode(Node):

    apartmens_max = 10
    def __init__(self, id, root):
        super().__init__(root)
        self.id = id
        self.apartmens_count = 0

    def sub_inhabitants(self):
        pass

    def add_apartmet(self, rooms=rint(1, ApartmentNode.room_max)):
        pass
