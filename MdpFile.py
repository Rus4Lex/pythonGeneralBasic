from Nodes import *
from MDP import *
from random import randint, choice
import string
import os
import os.path


class MdpFile:
    @staticmethod
    def write(home: HomeNode, name: str):
        MdpWriter(home, name).write()

    @staticmethod
    def read(name: str) -> HomeNode:
        home = MdpReader(HomeNode(), name)
        home.read_header()
        return home.home

    @staticmethod
    def get_files() -> list[str]:
        out = []
        for root, dirs, files in os.walk("."):
            out += [filename for filename in files if filename.endswith(".mdp")]
        return out

    @staticmethod
    def file_exist(name):
        return name in MdpFile.get_files()

    @staticmethod
    def file_remove(name):
        os.remove(name)


def random_word(length):
    # letters = string.ascii_lowercase
    letters = "".join([chr(a) for a in range(ord('а'), ord('я'))])
    word = ''.join(choice(letters) for _ in range(length))
    return word.capitalize()


# Macro auto testing
if __name__ == '__main__':
    main_home = HomeNode()
    for i in range(10):
        main_home.add_floor(True)

    floors = main_home.get_floors()

    for i in floors:
        aps = i.get_apartments()
        for j in aps:
            for k in range(randint(0, j.rooms_count)):
                j.add_inhabitant(InhabitantNode(
                    f"{random_word(randint(3, 12))} {random_word(randint(3, 12))} {random_word(randint(3, 15))}",
                    randint(17, 65), main_home))
                if randint(0, 10) > 9:
                    ti = j.get_habitants()
                    j.sub_inhabitants([ti[0]])

    MdpFile.write(main_home, "testingHome.mdp")
    mdp = MdpFile.read("testingHome.mdp")
