from InhabitantNode import *

class ApartmentNode(Node):
    def __init__(self, id):
        super().__init__()
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
            return False
        else:
            tit = inhab
            tit.parent = self
            self.__dict__[hex(self.rooms_count)[2:]] = tit
            self.inhabs_count += 1

    def sub_inhabitants(self, ids:list):
        pass


