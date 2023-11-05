import struct as st
from Nodes import *
from random import randint, choice
import string


class MdpFile:

    def __init__(self):
        pass

def random_word(length):
    letters = string.ascii_lowercase
    word = ''.join(choice(letters) for _ in range(length))
    return word.capitalize()

# Macro auto testing
if __name__ == '__main__':
    main_home = HomeNode()
    for i in range(5):
        main_home.add_floor(True)

    floors = main_home.get_floors()

    for i in floors:
        aps = i.get_apartments()
        for j in aps:
            for k in range(randint(1, 4)):
                j.add_inhabitant(InhabitantNode(f"{random_word(randint(3, 12))} {random_word(randint(5, 12))} {random_word(randint(5, 15))}",randint(10, 75), main_home))
