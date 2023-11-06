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
