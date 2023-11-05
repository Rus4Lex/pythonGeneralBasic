from abc import abstractmethod


class Reader:

    @abstractmethod
    def __x(self, h: str):
        """convert hex to integer"""
    @abstractmethod
    def load(self):
        """open and read file to memory"""
    @abstractmethod
    def get(self, form) -> tuple:
        """read data from memory"""
    @abstractmethod
    def read_list(self, func, parent=None):
        """read list of data array"""
    @abstractmethod
    def read_inhabitant(self, identifier, parent=None):
        """read and load node to object"""
    @abstractmethod
    def read_apartment(self, identifier, parent=None):
        """read and load node to object"""
    @abstractmethod
    def read_floor(self, identifier, parent=None):
        """read and load node to object"""
    @abstractmethod
    def read_header(self):
        """read header section and load node to main object"""