from Nodes import *
from Interface import Interface
from SuperInterface import SuperInterface
import re

class IManager(SuperInterface):
    def __init__(self):
        self.ui_home = Interface(self)  # home interface
        self.ui_home.help += "---HOME MENU---\n"
        self.ui_home.add("fradd")
        self.ui_home.add_help("створити пустий дім з випадковими квартирами.")
        self.ui_home.add("frem")
        self.ui_home.add_help("видалити список поверхів.")
        self.ui_home.add("flist")
        self.ui_home.add_help("показати список поверхів.")
        self.ui_home.add("fadd")
        self.ui_home.add_help("додати поверх з одною квартирою.")
        self.ui_home.add("fenter")
        self.ui_home.add_help("увійти на поверх")
        self.ui_home.add("delete_all_in_home")
        self.ui_home.add_help("очистити будинок!")

        self.ui_floor = Interface(self)  # floor interface
        self.ui_floor.help += "---FLOOR MENU---\n"
        self.ui_floor.onExit = self.ui_home.info
        self.ui_floor.add("qadd")
        self.ui_floor.add_help("додати квартиру на поверсі.")
        self.ui_floor.add("qrem")
        self.ui_floor.add_help("видалити квартири на поверсі.")
        self.ui_floor.add("qlist")
        self.ui_floor.add_help("додати квартиру на поверсі.")
        self.ui_floor.add("qenter")
        self.ui_floor.add_help("увійти у квартиру на поверсі.")

        self.ui_apart = Interface(self)  # apartment interface
        self.ui_apart.help += "---APARTMENT MENU---\n"
        self.ui_apart.onExit = self.ui_floor.info
        self.ui_apart.add("ainfo")
        self.ui_apart.add_help("показати статистику квартири.")
        self.ui_apart.add("sdown")
        self.ui_apart.add_help("поселити мешканця.")

        self.ui_inhab = Interface(self)  # inhabitant interface
        self.ui_inhab.help += "---INHABITANT MENU---\n"
        self.ui_infos = Interface(self)  # statistics interface

        self.ui_datbe = Interface(self)  # database interface

        self.main_home = HomeNode()

        self.ui_home.walk()
        # self.main_database = None


        self.__current_floor = None
        self.__current_apartment = None
        self.__current_inhabitant = None

    def fradd(self):
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

    def flist(self):
        floors = self.main_home.get_floors()
        if len(floors) == 0:
            return "Дім пустий."
        out = ""
        cnt = 1

        for i in floors:
            out += f"floor {cnt}: id={hex(i.id)}\n"
            cnt += 1

        return out


    def fadd(self):
        self.main_home.add_floor()
        return "Поверх з квартирою створено."


    def delete_all_in_home(self):  # довга назва для запобігання випадковому вводу
        inp = input("Ви впевнені, що хочете видалити всі поверхи та мешканців у них?\nдля підтвердження натисніть 'Enter'\nдля відміни будь'який символ та підтвердіть\n>>> ")
        if len(inp) == 0:
            self.main_home = HomeNode()
            return "Дім очищено."
        else:
            return "Операцію відмінено."


    def fenter(self):
        res = "Нічого не вибрано."
        floors = self.main_home.get_floors()
        while True:
            inp = input("Введіть нуль для виходу або\nномер поверху на який ви хочете зайти\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    return res
                elif inp > len(floors):
                    print("Помилка\nнемає такого поверху!")
                else:
                    self.__current_floor = floors[inp - 1]
                    break
            else:
                print("Помилка вводу!")

        if self.__current_floor is not None:
            res = self.ui_floor.walk()
            self.__current_floor = None

        return res

    def qadd(self):
        if self.__current_floor.apartmens_count > FloorNode.apartmens_max:
            return f"Помилка забагато квартир на поверсі!\nмаксисмум = {FloorNode.apartmens_max}."
        rooms = 0
        while True:
            inp = input("Введіть нуль для виходу або\nкількість кімнат\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    break
                elif inp > ApartmentNode.room_max:
                    print(f"Помилка\nкімнат забагато, максимум = {ApartmentNode.room_max}!")
                else:
                    rooms = inp-1
                    break
            else:
                print("Помилка вводу!")
        self.__current_floor.add_apartment(rooms)
        return f"Квартиру id = {hex(self.main_home.maxID)} додано."

    def qlist(self):
        cnt = 1
        out = ""
        alist = self.__current_floor.get_apartments()
        for i in alist:
            out += f"квартира {cnt}: id = {hex(i.id)}, кімнат {i.rooms_count}\n"
            cnt += 1

        return out

    def qrem(self):
        aps = self.__current_floor.get_apartments()
        saps = []
        while True:
            inp = input("Введіть нуль для виходу або\nномера квартир які ви хочете видалити\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    break
                elif inp > len(aps):
                    print("Помилка\nнемає такої квартири!")
                elif aps[inp - 1] in saps:
                    print("Помилка\nквартиру уже додано!")
                else:
                    saps.append(aps[inp - 1])
        res = "Нічого не вибрано."
        if len(saps) > 0:
            res, frs, drs = self.__current_floor.sub_apartment(saps)
            if res:
                res = "Усі задані квартири видалено.\nid = " + "\nid = ".join(drs)
            else:
                res = "Не всі квартири видалено!\nid = " + "\nid = ".join(frs)

        return res

    def qenter(self) -> str:
        res = "Нічого не вибрано."
        aps = self.__current_floor.get_apartments()
        while True:
            inp = input("Введіть нуль для виходу або\nномер квартири на яку ви хочете зайти\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    return res
                elif inp > len(aps):
                    print("Помилка\nнемає такої квартири!")
                else:
                    self.__current_apartment = aps[inp - 1]
                    break
            else:
                print("Помилка вводу!")

        if self.__current_apartment is not None:
            res = self.ui_apart.walk()
            self.__current_apartment = None

        return res

    def ainfo(self):
        out = f"""\rid - {hex(self.__current_apartment.id)}
кімнат - {self.__current_apartment.rooms_count}
мешканців - {self.__current_apartment.inhabs_count}"""

        return out

    def sdown(self):
        out = "Скасовано."
        while True:
            inp = input("Введіть нуль для виходу або\nП І Б вік мешканця через пробіл\n>>> ")
            tin = re.findall("^\w+\s\w+\s\w+\s\d{2}$", inp)
            if inp == '0':
                break
            elif len(tin) == 1:
                ag = int(inp.split(' ')[-1])
                if 16 > ag > 100:
                    print("Вік неправильний.\n 16-99")
                    continue
                tin = InhabitantNode(inp.split(' ')[:2], ag, self.main_home.root)
                rslt = self.__current_apartment.add_inhabitant(tin)
                if rslt:
                    out = f"Мещканця id - {hex(tin.id)} створено."
                else:
                    out = f"У квартирі більше немає місця!"
                    self.main_home.maxID -= 1
                break
            else:
                print("Помилка вводу даних.")

        return out


