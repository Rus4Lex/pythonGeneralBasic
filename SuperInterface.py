from abc import abstractmethod
class SuperInterface:


    def ishex(self, x):
        try:
            int(x, 16)
            return True
        except ValueError:
            return False

    @abstractmethod
    def about(self) -> str:
        """Get info from House"""
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
        
        
    #apartment MENU

    @abstractmethod
    def qenter(self) -> str:
        """Enter to apartment menu section"""

    @abstractmethod
    def ainfo(self) -> str:
        """show apartment statistics"""

    @abstractmethod
    def alist(self) -> str:
        """list of inhabitant"""

    @abstractmethod
    def sdown(self) -> str:
        """settle down inhabitant"""

    @abstractmethod
    def outlist(self) -> str:
        """show inhabitant from outrooms"""
    @abstractmethod
    def sreg(self) -> str:
        """settle down inhabitant from outrooms"""

    @abstractmethod
    def sevict(self) -> str:
        """evict inhabitants to outrooms"""

    @abstractmethod
    def roomset(self) -> str:
        """set rooms count"""

    @abstractmethod
    def sedit(self) -> str:
        """edit inhabitant data"""
        
    #info MENU

    @abstractmethod
    def finfo(self) -> str:
        """Enter to info menu"""

    @abstractmethod
    def iilist(self) -> str:
        """Full list of inhabitants"""

    @abstractmethod
    def ialist(self) -> str:
        """Full list of apartments"""


    @abstractmethod
    def inft(self) -> str:
        """Info from apartments any type (characteristics)"""


    # file saving, loading and deleting

    @abstractmethod
    def mdp(self) -> str:
        """Enter to file menu"""
    @abstractmethod
    def mdplist(self) -> str:
        """list of mdp files here"""
    @abstractmethod
    def mdpload(self) -> str:
        """load file from list mdp files"""
    @abstractmethod
    def mdpsave(self) -> str:
        """save database to new file"""
    @abstractmethod
    def mdpres(self) -> str:
        """rewrite file from list mdp files"""
    @abstractmethod
    def mdpdel(self) -> str:
        """delete file from list mdp files"""



