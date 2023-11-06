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

    @abstractmethod
    def alist(self):
        """list of inhabitant"""

    @abstractmethod
    def sdown(self):
        """settle down inhabitant"""

    @abstractmethod
    def sevict(self):
        """evict inhabitants to outrooms"""

    @abstractmethod
    def roomset(self):
        """set rooms count"""

    @abstractmethod
    def sedit(self):
        """edit inhabitant data"""

    @abstractmethod
    def finfo(self):
        """Enter to info menu"""

    @abstractmethod
    def iilist(self):
        """Full list of inhabitants"""

    @abstractmethod
    def ialist(self):
        """Full list of apartments"""

    @abstractmethod
    def infa(self):
        """Info from apartment"""

    @abstractmethod
    def inft(self):
        """Info from apartments any type (characteristics)"""


    # file saving, loading and deleting

    @abstractmethod
    def mdp(self):
        """Enter to file menu"""
    @abstractmethod
    def mdplist(self):
        """list of mdp files here"""
    @abstractmethod
    def mdpload(self):
        """load file from list mdp files"""
    @abstractmethod
    def mdpsave(self):
        """save database to new file"""
    @abstractmethod
    def mdpres(self):
        """rewrite file from list mdp files"""
    @abstractmethod
    def mdpdel(self):
        """delete file from list mdp files"""



