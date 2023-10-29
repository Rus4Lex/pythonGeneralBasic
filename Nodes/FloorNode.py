from ApartmentNode import *
from random import randint as rint
#поверх
class FloorNode(Node):

    apartmens_max = 10
    def __init__(self, id, root):
        super().__init__(root)
        self.id = self.root.get_maxID()
        self.apartmens_count = 0


    # виселити поверх
    def sub_inhabitants(self):
        pass

    # додати квартиру
    def add_apartmet(self, rooms=rint(1, ApartmentNode.room_max)):
        if self.apartmens_count >= FloorNode.apartmens_max:
            return False # maximum 1 inhab 1 room
        tfn = ApartmentNode(self.root)
        tfn.parent = self
        tfn.add_rooms(rooms)
        self.__dict__[hex(self.apartmens_count)[:1]] = tfn
        return True
