from Node import Node

class ApartmentNode(Node):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.rooms_count: int = 0

    def add_inhabitant(self, pib, age):
        pass
