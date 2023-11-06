from Nodes import *
from Interface import Interface
from SuperInterface import SuperInterface
from MdpFile import *
import re


class IManager(SuperInterface):
    def __init__(self):

        self.__current_floor: FloorNode = None
        self.__current_apartment: ApartmentNode = None
        self.__current_inhabitant: InhabitantNode = None
        # self.main_database = None


        self.ui_home = Interface(self)  # home interface
        self.ui_home.help += "---HOME MENU---\n"
        self.ui_home.add("mdp")
        self.ui_home.add_help("перейти у файлове меню.")
        self.ui_home.add("finfo")
        self.ui_home.add_help("перейти у розділ статистики.")
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
        self.ui_apart.add("alist")
        self.ui_apart.add_help("показати список мешканців квартири.")
        self.ui_apart.add("sdown")
        self.ui_apart.add_help("поселити мешканця.")
        self.ui_apart.add("sedit")
        self.ui_apart.add_help("редагувати мешканця.")
        self.ui_apart.add("sevict")
        self.ui_apart.add_help("виселити мешканців.")
        self.ui_apart.add("roomset")
        self.ui_apart.add_help("встановити кількість кімнат у квартирі.")


        self.ui_infos = Interface(self)  # statistics interface
        self.ui_infos.help += "---HOUSE INFO MENU---\n"
        self.ui_infos.onExit = self.ui_home.info
        self.ui_infos.add("iilist")
        self.ui_infos.add_help("вивести інформацію про усіх жителів.")


        self.ui_datbe = Interface(self)  # database interface
        self.ui_datbe.help += "---FILE MENU---\n"
        self.ui_datbe.onExit = self.ui_home.info
        self.ui_datbe.add("mdplist")
        self.ui_datbe.add_help("показати список збережених файлів.")
        self.ui_datbe.add("mdpload")
        self.ui_datbe.add_help("завантажити файл зі списку.")
        self.ui_datbe.add("mdpsave")
        self.ui_datbe.add_help("зберегти файл.")
        self.ui_datbe.add("mdpres")
        self.ui_datbe.add_help("перезаписати файл зі списку.")
        self.ui_datbe.add("mdpdel")
        self.ui_datbe.add_help("видалити файл зі списку.")

        self.main_home = HomeNode()
        self.ui_home.walk()





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
                if 16 > ag or ag > 100:
                    print("Вік неправильний.\n 16-99")
                    continue
                tin = InhabitantNode(" ".join(inp.split(' ')[:-1]), ag, self.main_home.root)
                rslt = self.__current_apartment.add_inhabitant(tin)
                if rslt:
                    out = f"Мещканець id - {hex(tin.id)}."
                else:
                    out = f"У квартирі більше немає місця!"
                    self.main_home.maxID -= 1
                break
            else:
                print("Помилка вводу даних.")

        return out


    def alist(self):
        cnt = 1
        out = ""
        nhbs = self.__current_apartment.get_habitants()
        if len(nhbs) == 0:
            return "У квартирі ніхто не прожииває."
        for h in nhbs:
            out += f"мешканець {cnt}: {h.get()[0]}, років {h.get()[1]}\n"
            cnt += 1

        return out

    def sevict(self):
        nhbs = self.__current_apartment.get_habitants()
        if len(nhbs) == 0:
            return "У квартирі немає кого виселяти!"
        saps = []
        while True:
            inp = input("Введіть нуль для виходу або\nномера жителів яких ви хочете виселити\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    break
                elif inp > len(nhbs):
                    print("Помилка\nнемає такого жителя!")
                elif nhbs[inp - 1] in saps:
                    print("Помилка\nжитель уже кандидат на виселення!")
                else:
                    saps.append(nhbs[inp - 1])
        res = "Нічого не вибрано."
        if len(saps) > 0:
            self.__current_apartment.sub_inhabitants(saps)
            res = "Вказаних жителів виселено."

        return res

    def roomset(self):
        while True:
            inp = input("Введіть нуль для виходу або\nкількість кімнат яку ви хочете встановити\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    return "Скасовано."
                else:
                    res = self.__current_apartment.set_rooms(inp-1)
                    if res:
                        return f"Встановлено кімнат {self.__current_apartment.rooms_count}"
                    else:
                        return f"Кімнат не може бути меньше ніж жителів"
            else:
                print("Помилка вводу!")

    def sedit(self):
        nhbs = self.__current_apartment.get_habitants()
        if len(nhbs) == 0:
            return "У квартирі немає кого редагувати!"
        saps = []
        while True:
            inp = input("Введіть нуль для виходу або\nномер жителя якого ви хочете редагувати\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    return "Нічого не вибрано."
                elif inp > len(nhbs):
                    print("Помилка\nнемає такого жителя!")
                else:
                    saps.append(nhbs[inp - 1])
                    break
        self.__current_apartment.sub_inhabitants(saps, True)

        return self.sdown()


    def finfo(self):
        return self.ui_infos.walk()

    def iilist(self):
        out = "Списки жителів:\nВиселені жителі\n"
        if len(self.main_home.outrooms) == 0:
            out += "відсутні.\n"
        for i in self.main_home.outrooms:
            out += f"id - {i.id}\n{i.get()[0]}, років {i.get()[1]}\n"
        out2 = "Заселені жителі\n"
        floors = self.main_home.get_floors()
        for fs in floors:
            for aps in fs.get_apartments(True):
                for inh in aps:
                    out2 += f"id - {inh.id}\n{inh.get()[0]}, років {inh.get()[1]}\n"
        if out2 == "Заселені жителі\n":
            out2 += "відсутні.\n"
        return out+out2


    def ialist(self):
        """Full list of apartments"""

    def infa(self):
        """Info from apartment"""

    def inft(self):
        """Info from apartments any type (characteristics)"""

    def mdp(self):
        return self.ui_datbe.walk()

    def mdplist(self):
        lst = MdpFile.get_files()
        return "".join([f"{i+1}. {lst[i]}\n" for i in range(len(lst))])

    def mdpload(self):
        lst = MdpFile.get_files()
        if len(lst) == 0:
            return "Файли відсутні."
        while True:
            inp = input("Введіть нуль для виходу або\nномер файлу для завантаження\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    break
                elif inp > len(lst):
                    print("Помилка\nнемає такого файлу!")
                elif not MdpFile.file_exist(lst[inp-1]):
                    print("Помилка\nнемає такого файлу!")
                else:
                    try:
                        self.main_home = MdpFile.read(lst[inp-1])
                        return f"Файл {lst[inp-1]} завантажено."
                    except Exception as e:
                        return e
            else:
                print("Помилка вводу!")
        return "Нічого не вибрано."

    def mdpsave(self):
        while True:
            inp = input("Підтвердіть для виходу або\nвведіть назву файлу для збереження\n>>> ")
            if not all([(c in "\\/.") for c in inp]):
                inp += ".mdp"
                if len(inp)==0:
                    return "Нічого не вибрано."
                elif MdpFile.file_exist(inp):
                    print("Помилка\nцей файл уже існує!")
                else:
                    try:
                        MdpFile.write(self.main_home, inp)
                        return f"Файл {inp} збережено."
                    except Exception as e:
                        return e
            else:
                print("Помилка вводу!")

    def mdpres(self):
        lst = MdpFile.get_files()
        if len(lst) == 0:
            return "Файли відсутні."
        while True:
            inp = input("Введіть нуль для виходу або\nномер файлу для збереження\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    break
                elif inp > len(lst):
                    print("Помилка\nнемає такого файлу!")
                elif not MdpFile.file_exist(lst[inp - 1]):
                    print("Помилка\nнемає такого файлу!")
                else:
                    try:
                        MdpFile.write(self.main_home, lst[inp - 1])
                        return f"Файл {lst[inp - 1]} збережено."
                    except Exception as e:
                        return e
            else:
                print("Помилка вводу!")
        return "Нічого не вибрано."

    def mdpdel(self):
        lst = MdpFile.get_files()
        if len(lst) == 0:
            return "Файли відсутні."
        while True:
            inp = input("Введіть нуль для виходу або\nномер файлу для видалення\n>>> ")
            if inp.isdigit():
                inp = int(inp)
                if inp == 0:
                    break
                elif inp > len(lst):
                    print("Помилка\nнемає такого файлу!")
                elif not MdpFile.file_exist(lst[inp - 1]):
                    print("Помилка\nнемає такого файлу!")
                else:
                    try:
                        MdpFile.file_remove(lst[inp - 1])
                        return f"Файл {lst[inp - 1]} видалено."
                    except Exception as e:
                        return e
            else:
                print("Помилка вводу!")
        return "Нічого не вибрано."
