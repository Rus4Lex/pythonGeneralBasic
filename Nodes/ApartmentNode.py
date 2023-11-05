from .InhabitantNode import *
from typing import List
#квартира
class ApartmentNode(Node):

    room_max = 4
    def __init__(self, root):
        super().__init__(root)
        self.id = self.root.get_maxID()
        self.rooms_count: int = 1

    # додати кімнати
    def set_rooms(self, cnt):
        self.rooms_count = (cnt % ApartmentNode.room_max) + 1
        if self.rooms_count < self.inhabs_count:
            self.rooms_count = self.inhabs_count
            return False # maximum 1 inhab 1 room
        return True

    # поселити мешканця
    def add_inhabitant(self, inhab):
        if self.rooms_count <= self.inhabs_count:
            return False # maximum 1 inhab 1 room
        else:
            tit = inhab
            tit.parent = self
            self.__dict__[hex(tit.id)[1:]] = tit
            self.inhabs_count += 1
            self.parent.inhabs_count += 1
            self.root.inhabs_count += 1
        return True


    # виселити мешканців
    def sub_inhabitants(self, ids=None, over=False):
        if self.inhabs_count == 0:
            return False #room is empty
        if ids is None:# if ids is None delete all inhabitants
            ids = [self.__dict__[x].id for x in self.__dict__ if x[0] == 'x']
        for k in ids:
            if not over:
                tit = self.__dict__[hex(k.id)[1:]]
                tit.parent = self.root
                self.root.outrooms.append(tit)
            del self.__dict__[hex(k.id)[1:]]
            self.inhabs_count -= 1
            self.parent.inhabs_count -= 1
            self.root.inhabs_count -= 1
        return True

    # список жителів цієї квартири
    def get_habitants(self) -> List[InhabitantNode]:
        out = []
        for k in self.__dict__:
            if k[0] == 'x':
                out.append(self.__dict__[k])
        return out

    def sizeof(self) -> int:
        # elem count(1 bytes) = 3
        # [0x12(1 bytes), address(4 bytes)]
        # [0x13(1 bytes), address(4 bytes)]
        # [0x1(1 bytes), address(4 bytes)]
        # [roomsCount(4 bytes)]
        # [inhabsCount(4 bytes)]
        # [elem count(4 bytes)[id(4 bytes), address(4 bytes)]...]
        inhbs = self.get_habitants()
        sze = 28+(len(inhbs)*8)
        for i in inhbs:
            sze += i.sizeof()

        return sze  # bytes


