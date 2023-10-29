from FloorNode import *



class HomeNode(Node):
    floor_max = 100
    def __init__(self):
        super().__init__(self)
        self.floor_count = 0
        self.outrooms = []#виселені жителі
        self.maxID = 0

    def get_maxID(self):
        self.maxID += 1
        return self.maxID

    def add_floor(self, rand=False):
        if self.floor_count >= HomeNode.floor_max:
            return False
        tfn = FloorNode(self)
        # додає поверх із випадковою кількістю квартир та кімнат в них
        if rand:
            for i in range(rint(1, HomeNode.floor_max)):
                tfn.add_apartmet()
        # додає поверх із одною квартирою з випадковою кількістю кімнат
        else:
            tfn.add_apartmet()
        self.floor_count += 1
        return True

    def add_floor(self):
        pass






