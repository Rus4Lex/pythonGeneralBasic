from InhabitantNode import *

class ApartmentNode(Node):
    def __init__(self, id, root):
        super().__init__(root)
        self.id = id
        self.rooms_count: int = 1
        self.inhabs_count: int = 0


    def add_rooms(self, cnt):
        if self.rooms_count + cnt > 4:
            return False
        else:
            self.rooms_count += cnt
            return True

    def sub_rooms(self, cnt):
        if self.rooms_count - cnt < 1:
            return False
        else:
            self.rooms_count -= cnt
            return True


    def add_inhabitant(self, inhab):
        if self.rooms_count == self.inhabs_count:
            return False # maximum 1 inhab 1 room
        else:
            tit = inhab
            tit.parent = self
            self.__dict__[hex(self.inhabs_count)[1:]] = tit
            self.inhabs_count += 1

    def sub_inhabitants(self, ids: list):
        if self.inhabs_count == 0:
            return False #room is empty
        for k in ids:
            self.root.outrooms.append(self.__dict__[hex(k)[1:]])
            del self.__dict__[hex(k)[1:]]
            self.inhabs_count -= 1
        return True


