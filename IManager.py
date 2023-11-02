from Nodes import *
from Interface import Interface
from SuperInterface import SuperInterface

class IManager(SuperInterface):
    def __init__(self):
        self.ui_datbe = Interface(self)  # database interface
        self.ui_home = Interface(self)  # home interface
        self.ui_home.add("addrand")
        self.ui_home.add_help("addrand - створити пустий дім з випадковими квартирами")

        self.ui_floor = Interface(self)  # floor interface
        self.ui_apart = Interface(self)  # apartment interface
        self.ui_inhub = Interface(self)  # inhabitant interface
        self.ui_infos = Interface(self)  # statistics interface

        self.main_home = HomeNode()

        self.ui_home.walk()
        # self.main_database = None

    def addrand(self):
        print("adding")

        return ""

