from abc import abstractmethod


class Writer:
    @abstractmethod
    def __x(self, h: str):
        """convert hex to integer"""

    @abstractmethod
    def write(self):
        """write generated data to file"""

    @abstractmethod
    def headSet(self):
        """Generate MDP(My data package) inital header from homebase"""

    @abstractmethod
    def inhabSet(self, inh):
        """inh -> InhabitantNode\n
        Get and write data from inhabitant node"""

    @abstractmethod
    def outSet(self):
        """get and write data from outroom Inhabitants"""

    @abstractmethod
    def apartmentsSet(self, aps):
        """aps -> ApartmentNode\n
        get and write data from Apartments on floors"""

    @abstractmethod
    def floorSet(self, fr):
        """fr -> FloorNode\n
        get and write data from floors in house"""

    @abstractmethod
    def innerSet(self):
        """main writer data method\n
        for getting and writing data from house floors, apartments, and others"""


