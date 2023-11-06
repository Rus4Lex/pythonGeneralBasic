import unittest
from MdpFile import *

class MdpFileTestCase(unittest.TestCase):

    def random_word(self, length, eng=False):
        # letters = string.ascii_lowercase
        letters = string.ascii_lowercase if eng else "".join([chr(a) for a in range(ord('а'), ord('я'))])
        word = ''.join(choice(letters) for _ in range(length))
        return word.capitalize()
    def test_empty_file_a(self):
        try:
            MdpFile.write(HomeNode(), "test.mdp")
        except Exception as e:
            self.fail(f"Raised writer!\n{e}")
    def test_empty_file_b(self):
        try:
            MdpFile.read("test.mdp")
        except Exception as e:
            self.fail(f"Raised reader!\n{e}")

    def test_big_data_file_a(self):
        try:
            main_home = HomeNode()
            HomeNode.floor_max = 10000
            for i in range(10000):
                main_home.add_floor(True)

            floors = main_home.get_floors()

            for i in floors:
                aps = i.get_apartments()
                for j in aps:
                    for k in range(randint(0, j.rooms_count)):
                        j.add_inhabitant(InhabitantNode(
                            f"{self.random_word(randint(1, 52))} {self.random_word(randint(1, 52))} {self.random_word(randint(1, 55), True)}",
                            randint(1, 99), main_home))
                        if randint(0, 10) > 9:
                            ti = j.get_habitants()
                            j.sub_inhabitants([ti[0]])
            MdpFile.write(main_home, "bigFile.mdp")
        except Exception as e:
            self.fail(f"Raised writer big_data_file!\n{e}")
    def test_big_data_file_b(self):
        try:
            MdpFile.read("bigFile.mdp")
        except Exception as e:
            self.fail(f"Raised reader big_data_file!\n{e}")

    def test_unknown_file_reading(self):
        with self.assertRaises(Exception):
            MdpFile.read("test2.mdp")
