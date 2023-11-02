from abc import abstractmethod
class SuperInterface:

    @abstractmethod
    def adrand(self) -> str:
        """Add a random floors, apartments and rooms"""

    @abstractmethod
    def frem(self) -> str:
        """"Remove list of floors"""

    @abstractmethod
    def frs(self) -> str:
        """Show all floors"""

    @abstractmethod
    def fadd(self) -> str:
        """Adding one floor inside one apartment have one room"""

    @abstractmethod
    def delete_all_in_home(self) -> str:
        """Delete all floors and inhabitants there"""

    @abstractmethod
    def efloor(self) -> str:
        """Enter to floor menu section"""

    @abstractmethod
    def qadd(self) -> str:
        """Add Apartment to floor with one room"""


