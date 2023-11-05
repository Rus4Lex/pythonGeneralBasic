from .Node import *
#мешканець

class InhabitantNode(Node):
    def __init__(self, pib, age, root):
        super().__init__(root)
        self.id = self.root.get_maxID()
        self.__PIB = pib
        self.__Age = age
        del self.inhabs_count

    def edit(self, pib, age):
        self.__PIB = pib
        self.__Age = age

    def get(self):
        return self.__PIB, self.__Age

    def sizeof(self) -> int:
        # elem count(4 bytes),
        # [0x2(1 bytes), address(4 bytes)],
        # [0x3(1 bytes), address(4 bytes)],
        # [size(4 bytes), word(size bytes)],
        # [age(4 bytes)]
        return 21+len(self.__PIB)  # bytes
