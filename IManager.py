from Nodes import *
from Interface import Interface
from SuperInterface import SuperInterface

class IManager(SuperInterface):
    def __init__(self):
        self.ui_home = Interface(self)  # home interface
        self.ui_home.add("adrand")
        self.ui_home.add_help("створити пустий дім з випадковими квартирами")
        self.ui_home.add("fremove")
        self.ui_home.add_help("видалити список поверхів")

        self.ui_floor = Interface(self)  # floor interface
        self.ui_apart = Interface(self)  # apartment interface
        self.ui_inhub = Interface(self)  # inhabitant interface
        self.ui_infos = Interface(self)  # statistics interface

        self.ui_datbe = Interface(self)  # database interface

        self.main_home = HomeNode()

        self.ui_home.walk()
        # self.main_database = None

    def adrand(self):
        self.main_home.new_rand()

        return "Apartments and floors created."


    def fremove(self):
        cnt = 1
        floors = self.main_home.get_floors()
        for i in floors:
            print(f"floor {cnt}: id={hex(i.id)}")
            cnt += 1
        sfloors = []
        while True:
            inp = input("Введіть нуль для виходу або\nномера поверхів які ви хочете видалити\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    break
                elif inp > len(floors):
                    print("Помилка\nнемає такого поверху!")
                elif floors[inp-1] in sfloors:
                    print("Помилка\nповерх уже додано!")
                else:
                    sfloors.append(floors[inp-1])
        res = self.main_home.del_floors(sfloors)
        if res:
            res = "Усі задані поверхи видалено."
        else:
            res = "Не всі поверхи видалено!"


        return res

