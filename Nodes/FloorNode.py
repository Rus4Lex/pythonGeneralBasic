from ApartmentNode import *
from random import randint as rint
#поверх
class FloorNode(Node):

    apartmens_max = 10
    def __init__(self, root):
        super().__init__(root)
        self.id = self.root.get_maxID()
        self.apartmens_count = 0


    # виселити поверх
    def sub_inhabitants(self):
        pass

    # додати квартиру
    def add_apartmet(self, rooms=rint(1, ApartmentNode.room_max)):
        if self.apartmens_count >= FloorNode.apartmens_max:
            return False
        tfn = ApartmentNode(self.root)
        tfn.parent = self
        tfn.add_rooms(rooms)
        self.__dict__[hex(self.apartmens_count)[1:]] = tfn
        self.apartmens_count += 1
        return True

    def sub_apartment(self, ids: list):
        out = True
        for apartment in ids:
            tfn = self.__dict__[hex(apartment)[1:]]
            if tfn.inhabs_count == 0:
                del self.__dict__[hex(apartment)[1:]]
            else:
                out = False
        return out
