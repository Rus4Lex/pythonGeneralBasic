from Nodes import *
from Interface import Interface
from SuperInterface import SuperInterface

class IManager(SuperInterface):
    def __init__(self):
        self.ui_home = Interface(self)  # home interface
        self.ui_home.add("adrand")
        self.ui_home.add_help("створити пустий дім з випадковими квартирами")
        self.ui_home.add("frem")
        self.ui_home.add_help("видалити список поверхів")
        self.ui_home.add("frs")
        self.ui_home.add_help("показати список поверхів")

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

        return "Рандомні поверхи з квартирами створено."


    def frem(self):
        floors = self.main_home.get_floors()
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
        res = "Нічого не вибрано."
        if len(sfloors) > 0:
            res, frs, drs = self.main_home.del_floors(sfloors)
            if res:
                res = "Усі задані поверхи видалено.\nid = "+"\nid = ".join(drs)
            else:
                res = "Не всі поверхи видалено!\nid = "+"\nid = ".join(frs)


        return res

    def frs(self):
        floors = self.main_home.get_floors()
        if len(floors) == 0:
            return "Дім пустий."
        out = ""
        cnt = 1

        for i in floors:
            out += f"floor {cnt}: id={hex(i.id)}\n"
            cnt += 1

        return out


