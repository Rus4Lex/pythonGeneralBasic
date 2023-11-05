from .ApartmentNode import *
from random import randint
from typing import List
#поверх
class FloorNode(Node):

    apartmens_max = 10

    def __init__(self, root):
        super().__init__(root)
        self.id = self.root.get_maxID()
        self.apartmens_count = 0


    # виселити поверх
    def sub_inhabitants(self):
        for k in self.__dict__:
            if k[0] == 'x':
                self.__dict__[k].sub_inhabitants()

    # додати квартиру
    def add_apartment(self, rooms=None):
        if rooms is None:
            rooms = randint(1, ApartmentNode.room_max)
        if self.apartmens_count >= FloorNode.apartmens_max:
            return False
        tan = ApartmentNode(self.root)
        tan.parent = self
        tan.set_rooms(rooms)
        self.__dict__[hex(tan.id)[1:]] = tan
        self.apartmens_count += 1
        self.root.apartmens_count += 1
        return True


    #видалити квартири (якщо у квартирах є жителі вони не видаляються)
    def sub_apartment(self, ids: list):
        out = True
        ndel = []  # квартири що не видалились
        tdel = []  # квартири що видалились
        for apartment in ids:
            tfn = self.__dict__[hex(apartment.id)[1:]]
            if tfn.inhabs_count == 0:
                tdel.append(hex(apartment.id)[1:])
                del self.__dict__[hex(apartment.id)[1:]]
                self.apartmens_count -= 1
                self.root.apartmens_count -= 1
            else:
                ndel.append(hex(apartment.id)[1:])
                out = False# якась із квартир не видалилась
            if self.apartmens_count == 0:  # якщо видалити всі квартири з поверху він автоматично видаляється
                iid = hex(self.parent.id)[1:]
                del self.root.__dict__[iid]
        return out, ndel, tdel


    # повернення списку квартир за заданими параметрами
    def get_apartments(self, inhabs=None, rooms=None) -> List[ApartmentNode]:
        out = []
        for k in self.__dict__:
            if k[0] == 'x':
                tas = self.__dict__[k]
                if isinstance(inhabs, bool) and tas.inhabs_count > 0:
                    out.append(tas)
                elif inhabs is None and rooms is None:# all
                    out.append(tas)
                elif inhabs is None and rooms is not None:# room count
                    if tas.rooms_count == rooms:
                        out.append(tas)
                elif inhabs is not None and rooms is None:# inhabs count
                    if tas.inhabs_count == inhabs:
                        out.append(tas)
                elif inhabs is not None and rooms is not None:# rooms and inhabs count
                    if (tas.inhabs_count == inhabs) and (tas.rooms_count == rooms):
                        out.append(tas)

        return out

    def sizeof(self) -> int:
        # elem count(4 bytes)
        # [0x4(1 bytes), address(4 bytes)]
        # [0x1(1 bytes), address(4 bytes)]
        # [inhabsCount(4 bytes)]
        # [elem count(4 bytes)[id(4 bytes), address(4 bytes)]...]
        aps = self.get_apartments()
        sze = 22+(len(aps)*8)
        for a in aps:
            sze += a.sizeof()

        return sze  # bytes
