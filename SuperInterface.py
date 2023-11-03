from abc import abstractmethod
class SuperInterface:

    @abstractmethod
    def fradd(self) -> str:
        """Add a random floors, apartments and rooms"""

    @abstractmethod
    def frem(self) -> str:
        """"Remove list of floors"""

    @abstractmethod
    def flist(self) -> str:
        """Show all floors"""

    @abstractmethod
    def fadd(self) -> str:
        """Adding one floor inside one apartment have one room"""

    @abstractmethod
    def delete_all_in_home(self) -> str:
        """Delete all floors and inhabitants there"""

    @abstractmethod
    def fenter(self) -> str:
        """Enter to floor menu section"""

    @abstractmethod
    def qadd(self) -> str:
        """Add Apartment to floor with one room"""

    @abstractmethod
    def qlist(self) -> str:
        """Show list of apartments with rooms count"""

    @abstractmethod
    def qrem(self) -> str:
        """Remove list of apartments"""

    @abstractmethod
    def qenter(self) -> str:
        """Enter to apartment menu section"""

    @abstractmethod
    def ainfo(self):
        """show apartment statistics"""


