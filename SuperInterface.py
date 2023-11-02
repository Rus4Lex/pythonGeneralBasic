from abc import abstractmethod
class SuperInterface:

    @abstractmethod
    def adrand(self):
        """Add a random floors, apartments and rooms"""

    @abstractmethod
    def frem(self):
        """"Remove list of floors"""

    @abstractmethod
    def frs(self):
        """Show all floors"""

    @abstractmethod
    def fadd(self):
        """Adding one floor inside one apartment have one room"""


