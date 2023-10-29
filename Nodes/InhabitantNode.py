from Nodes.Node import *


class InhabitantNode(Node):
    def __init__(self, pib, age):
        super().__init__()
        self.__PIB = pib
        self.__Age = age

    def edit(self, pib, age):
        self.__PIB = pib
        self.__Age = age

    def get(self):
        return self.__PIB, self.__Age
