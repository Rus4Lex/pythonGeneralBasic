from Nodes.Node import *


class InhabitantNode(Node):
    def __init__(self, pib, age, root):
        super().__init__(root)
        self.__PIB = pib
        self.__Age = age

    def edit(self, pib, age):
        self.__PIB = pib
        self.__Age = age

    def get(self):
        return self.__PIB, self.__Age
