from .FloorNode import *


class HomeNode(Node):
    floor_max = 100
    def __init__(self):
        super().__init__(self)
        self.floor_count = 0
        self.outrooms = []#виселені жителі
        self.maxID = 0
        self.id = self.get_maxID()
        self.apartmens_count = 0

    def get_maxID(self):
        self.maxID += 1
        return self.maxID

    def new_rand(self):  # random floor creating
        for i in range(randint(1, 10)):
            self.add_floor(True)

    def add_floor(self, rand=False):
        if self.floor_count >= HomeNode.floor_max:
            return False
        tfn = FloorNode(self)
        tfn.parent = self
        # додає поверх із випадковою кількістю квартир та кімнат в них
        if rand:
            for i in range(randint(1, FloorNode.apartmens_max)):
                tfn.add_apartmet()
        # додає поверх із одною квартирою з випадковою кількістю кімнат
        else:
            tfn.add_apartmet(0)
        self.__dict__[hex(tfn.id)[1:]] = tfn
        self.floor_count += 1
        return True

    # видалити поверхи (якщо на поверсі є жителі вони не видаляються)
    def del_floors(self, ids: list):
        out = True  # все гаразд
        ndel = []  # поверхи що не видалились
        tdel = []  # поверхи що видалились
        for k in ids:  # floors walker
            if self.__dict__[hex(k.id)[1:]].inhabs_count == 0:
                tdel.append(hex(k.id)[1:])
                del self.__dict__[hex(k.id)[1:]]
            else:
                ndel.append(hex(k.id)[1:])
                out = False  # якийсь із поверхів не видалився
        return out, ndel, tdel


    def get_floors(self):
        out = []
        for k in self.__dict__:
            if k[0] == 'x':
                out.append(self.__dict__[k])
        return out










