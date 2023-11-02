from Nodes import *
from Interface import Interface

class IManager:
    def __init__(self):
        self.ui_datbe = Interface()#database interface
        self.ui_home = Interface()#home interface
        self.ui_home.add("addrand", )

        self.ui_floor = Interface()#floor interface
        self.ui_apart = Interface()#apartament interface
        self.ui_inhub = Interface()#inhubitant interface
        self.ui_infos = Interface()#statistics interface

        self.main_home = HomeNode()

        self.ui_home.walk()
        # self.main_database = None

    def

