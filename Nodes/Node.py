

class Node:
    def __init__(self, root):
        self.id: int = 0
        self.root: Node = root
        self.parent: Node = None
        self.inhabs_count: int = 0

    def clear(self):
        for k in self.__dict__:
            if k != "id" or k != "parent":
                del(self.__dict__[k])

