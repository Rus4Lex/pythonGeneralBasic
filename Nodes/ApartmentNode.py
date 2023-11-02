from .InhabitantNode import *
#квартира
class ApartmentNode(Node):

    room_max = 4
    def __init__(self,root):
        super().__init__(root)
        self.id = self.root.get_maxID()
        self.rooms_count: int = 1
        self.inhabs_count: int = 0

    def __checkMinMax(self, cnt):
        if self.rooms_count + cnt < 1:
            self.rooms_count = 1
        if self.rooms_count + cnt > ApartmentNode.room_max:
            self.rooms_count = ApartmentNode.room_max

    # додати кімнати
    def add_rooms(self, cnt):
        self.__checkMinMax(cnt)
        self.rooms_count += cnt
        return True

    # видалити кімнати
    def sub_rooms(self, cnt):
        if self.rooms_count - cnt < self.inhabs_count:#жителів не може бути більше кімнат
            return False
        self.__checkMinMax(cnt)
        self.rooms_count -= cnt
        return True

    # поселити мешканця
    def add_inhabitant(self, inhab):
        if self.rooms_count >= self.inhabs_count:
            return False # maximum 1 inhab 1 room
        else:
            tit = inhab
            tit.parent = self
            self.__dict__[hex(tit.id)[1:]] = tit
            self.inhabs_count += 1
        return True


    # виселити мешканців
    def sub_inhabitants(self, ids=None):
        if self.inhabs_count == 0:
            return False #room is empty
        if ids is None:# if ids is None delete all inhabitants
            ids = [self.__dict__[x].id for x in self.__dict__ if x[0] == 'x']
        for k in ids:
            tit = self.__dict__[hex(k)[1:]]
            tit.parent = self.root
            self.root.outrooms.append(tit)
            del self.__dict__[hex(k)[1:]]
            self.inhabs_count -= 1
        return True

    # список жителів цієї квартири
    def get_habitants(self):
        out = []
        for k in self.__dict__:
            if k[0] == 'x':
                out.append(self.__dict__[k])
        return out


