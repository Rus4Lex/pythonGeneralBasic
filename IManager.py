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
        self.ui_home.add("about")
        self.ui_home.add_help("загальна інформація про будинок.")
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
        self.ui_floor.add_help("список квартир на поверсі.")
        self.ui_floor.add("qenter")
        self.ui_floor.add_help("увійти у квартиру на поверсі.")

        self.ui_apart = Interface(self)  # apartment interface
        self.ui_apart.help += "---APARTMENT MENU---\n"
        self.ui_apart.onExit = self.ui_floor.info
        self.ui_apart.add("ainfo")
        self.ui_apart.add_help("показати статистику квартири.")
        self.ui_apart.add("alist")
        self.ui_apart.add_help("показати список мешканців квартири.")
        self.ui_apart.add("outlist")
        self.ui_apart.add_help("показати список виселених мешканців.")
        self.ui_apart.add("sdown")
        self.ui_apart.add_help("поселити мешканця.")
        self.ui_apart.add("sreg")
        self.ui_apart.add_help("поселити мешканця із списку виселених.")
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
        self.ui_infos.add("ialist")
        self.ui_infos.add_help("вивести інформацію про усі квартири.")
        self.ui_infos.add("inft")
        self.ui_infos.add_help("вивести типізовану інформацію про квартири.")
        self.ui_infos.add("outlist")
        self.ui_infos.add_help("вивести список виселених мешканців.")


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
        #self.main_home = MdpFile.read("testingHome.mdp")

        self.ui_home.walk()



    def about(self):
        out = f"""\rІнформація:
максимальний ідетнифікатор - {hex(self.main_home.maxID)[2:]}
ідентифікатор - {hex(self.main_home.id)[2:]}
поверхів - {self.main_home.floor_count}
квартир - {self.main_home.apartmens_count}
жителів - {self.main_home.inhabs_count}
виселених жителів - {len(self.main_home.outrooms)}
        """
        return out

    def fradd(self):
        self.main_home.new_rand()

        return "Рандомні поверхи з квартирами створено."


    def frem(self):
        floors = self.main_home.get_floors()
        sfloors = []
        while True:
            inp = input("Введіть нуль для виходу або\nномера поверхів які ви хочете видалити\n>>> ")
            inp = "0x" + inp
            if self.ishex(inp):
                inp = int(inp, 16)
                if inp == 0:
                    break
                elif len([rf for rf in floors if rf.id == inp]) == 0:
                    print("Помилка\nнемає такого поверху!")
                elif len([rf for rf in sfloors if rf.id == inp]) == 1:
                    print("Помилка\nповерх уже додано!")
                else:
                    sfloors.append(self.main_home.__dict__[hex(inp)[1:]])
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

        for i in floors:
            out += f"поверх: {hex(i.id)[2:]}\n квартир - {i.apartmens_count}\n жителів - {i.inhabs_count}\n\n"

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
            inp = input("Введіть нуль для виходу або\nid поверху на який ви хочете зайти\n>>> ")
            inp = "0x"+inp
            if self.ishex(inp):
                inp = int(inp, 16)
                if inp == 0:
                    return res
                elif len([rf for rf in floors if rf.id == inp]) == 0:
                    print("Помилка\nнемає такого поверху!")
                else:
                    self.__current_floor = self.main_home.__dict__[hex(inp)[1:]]
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
        out = ""
        alist = self.__current_floor.get_apartments()
        for i in alist:
            out += f"квартира: {hex(i.id)[2:]}, \nкімнат {i.rooms_count}\nжителів {i.inhabs_count}\n\n"

        return out

    def qrem(self):
        aps = self.__current_floor.get_apartments()
        saps = []
        while True:
            inp = input("Введіть нуль для виходу або\nномера квартир які ви хочете видалити\n>>> ")
            inp = "0x" + inp
            if self.ishex(inp):
                inp = int(inp, 16)
                if inp == 0:
                    break
                elif len([rf for rf in aps if rf.id == inp]) == 0:
                    print("Помилка\nнемає такої квартири!")
                elif len([rf for rf in saps if rf.id == inp]) == 1:
                    print("Помилка\nквартиру уже додано!")
                else:
                    saps.append(self.__current_floor.__dict__[hex(inp)[1:]])
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
            inp = "0x" + inp
            if self.ishex(inp):
                inp = int(inp, 16)
                if inp == 0:
                    return res
                elif len([rf for rf in aps if rf.id == inp]) == 0:
                    print("Помилка\nнемає такої квартири!")
                else:
                    self.__current_apartment = self.__current_floor.__dict__[hex(inp)[1:]]
                    break
            else:
                print("Помилка вводу!")

        if self.__current_apartment is not None:
            res = self.ui_apart.walk()
            self.__current_apartment = None

        return res

    def ainfo(self):
        out = f"""\rквартира {hex(self.__current_apartment.id)}
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

    def outlist(self):
        return "".join([f"житель {hex(rs.id)[2:]}\n{rs.get()[0]}\nроків {rs.get()[1]}\n\n" for rs in self.main_home.outrooms])

    def sreg(self):
        nhbs = self.main_home.outrooms
        if len(nhbs) == 0:
            return "Виселені жителі відсутні!"
        while True:
            inp = input("Введіть нуль для виходу або\nномер жителя якого ви хочете поселити\n>>> ")
            inp = "0x" + inp
            if self.ishex(inp):
                inp = int(inp, 16)
                if inp == 0:
                    break
                elif len([rf for rf in nhbs if rf.id == inp]) == 0:
                    print("Помилка\nнемає такого жителя!")
                else:
                    if self.__current_apartment.rooms_count == self.__current_apartment.inhabs_count:
                        return "У квартирі більше немає місця!"
                    pl = [rf for rf in nhbs if rf.id == inp]
                    self.__current_apartment.add_inhabitant(pl[0])
                    for rf in range(len(nhbs)):
                        if nhbs[rf].id == inp:
                            del nhbs[rf]
                            break

                    return f"{hex(pl[0].id)[2:]} заселено."
        return "Нічого не вибрано."


    def alist(self):
        out = ""
        nhbs = self.__current_apartment.get_habitants()
        if len(nhbs) == 0:
            return "У квартирі ніхто не прожииває."
        for h in nhbs:
            out += f"мешканець {hex(h.id)[2:]}: {h.get()[0]}, років {h.get()[1]}\n"

        return out

    def sevict(self):
        nhbs = self.__current_apartment.get_habitants()
        if len(nhbs) == 0:
            return "У квартирі немає кого виселяти!"
        saps = []
        while True:
            inp = input("Введіть нуль для виходу або\nномера жителів яких ви хочете виселити\n>>> ")
            inp = "0x" + inp
            if self.ishex(inp):
                inp = int(inp, 16)
                if inp == 0:
                    break
                elif len([rf for rf in nhbs if rf.id == inp]) == 0:
                    print("Помилка\nнемає такого жителя!")
                elif len([rf for rf in saps if rf.id == inp]) == 1:
                    print("Помилка\nжитель уже кандидат на виселення!")
                else:
                    saps.append(self.__current_apartment.__dict__[hex(inp)[1:]])
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
            inp = "0x" + inp
            if self.ishex(inp):
                inp = int(inp, 16)
                if inp == 0:
                    return "Нічого не вибрано."
                elif len([rf for rf in nhbs if rf.id == inp]) == 0:
                    print("Помилка\nнемає такого жителя!")
                else:
                    saps.append(self.__current_apartment.__dict__[hex(inp)[1:]])
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
                for inh in aps.get_habitants():
                    out2 += f"поверх - {hex(fs.id)[2:]}\nквартира - {hex(aps.id)[2:]}\n"
                    out2 += f"житель - {hex(inh.id)[2:]}\n{inh.get()[0]}, років {inh.get()[1]}\n\n"
        if out2 == "Заселені жителі\n":
            out2 += "відсутні.\n"
        return out+out2


    def ialist(self):
        out = "Списки квартир:\n"
        floors = self.main_home.get_floors()
        for fs in floors:
            for aps in fs.get_apartments():
                out += f"поверх - {hex(fs.id)[2:]}\n"
                out += f"квартира - {hex(aps.id)[2:]}\nжителів - {aps.inhabs_count}, кімнат - {aps.rooms_count}\n\n"
        if out == "Списки квартир:\n":
            out += "квартири відсутні.\n"
        return out

    def inft(self):
        floors = self.main_home.get_floors()
        out = ""
        while True:
            inp = input("Введіть тип пошуку\n (i - кімнат, a - жителів , ia - усе разом)\n>>> ")
            if inp == "i":
                inp_a = input("Введіть кількість кімнат >>> ")
                if inp_a.isdigit():
                    inp_a = int(inp_a)
                    for fs in floors:
                        for aps in fs.get_apartments(rooms=inp_a):
                            out += f"поверх - {hex(fs.id)[2:]}\n"
                            out += f"квартира - {hex(aps.id)[2:]}\nжителів - {aps.inhabs_count}\n\n"
                else:
                    return "помилка вводу"
            elif inp == "a":
                inp_i = input("Введіть кількість жителів >>> ")
                if inp_i.isdigit():
                    inp_i = int(inp_i)
                    for fs in floors:
                        for aps in fs.get_apartments(inhabs=inp_i):
                            out += f"поверх - {hex(fs.id)[2:]}\n"
                            out += f"квартира - {hex(aps.id)[2:]}\nкімнат - {aps.rooms_count}\n\n"
                else:
                    return "помилка вводу"
            elif inp == "ia":
                inp_i = input("Введіть кількість жителів >>> ")
                inp_a = input("Введіть кількість кімнат >>> ")
                if inp_i.isdigit() and inp_a.isdigit():
                    inp_i = int(inp_i)
                    inp_a = int(inp_a)
                    for fs in floors:
                        for aps in fs.get_apartments(inp_i, inp_a):
                            out += f"поверх - {hex(fs.id)[2:]}\n"
                            out += f"квартира - {hex(aps.id)[2:]}\n\n"
                else:
                    return "помилка вводу"
            else:
                return "помилка вводу"
            return out if len(out)>0 else "Нічого не знайдено."

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
