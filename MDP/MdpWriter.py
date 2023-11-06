import io
import struct as st
from Nodes import *
from .Writer import *
class MdpWriter(Writer):
    def __init__(self, home: HomeNode, name: str):
        self.name = name
        self.home: HomeNode = home
        self.dataBlock = io.BytesIO()
        self.headSet()
        self.innerSet()  # write all other data


    def __x(self, h: str):
        return int(h, 16)

    def write(self):
        try:
            with open(self.name, "wb") as f:
                self.dataBlock.seek(0)
                f.write(self.dataBlock.read())
        except IOError as e:
            print("MDPWriter Error:")
            print(e)

    def headSet(self):
        self.dataBlock.write(b"MDP")
        self.dataBlock.write(st.pack("<II", self.home.id, 0))
        self.dataBlock.write(st.pack("<B", 6))  # num elements

        self.dataBlock.write(st.pack("<BI", self.__x("0x14"), 0))  # floo rcount
        self.dataBlock.write(st.pack("<BI", self.__x("0x15"), 4))  # aprtments count
        self.dataBlock.write(st.pack("<BI", self.__x("0x13"), 8))  # inhabs count
        self.dataBlock.write(st.pack("<BI", self.__x("0x16"), 12))  # maxID
        self.dataBlock.write(st.pack("<BI", self.__x("0x2"), 16))  # outrooms position

        # calc outrooms sizes
        tsze = 4  # info about elements count
        for o in self.home.outrooms:
            tsze += 8 + o.sizeof()

        self.dataBlock.write(st.pack("<BI", self.__x("0x1"), 16 + tsze))  # floors position
        # header data writing
        self.dataBlock.write(st.pack("<I", self.home.floor_count))  # floor count
        self.dataBlock.write(st.pack("<I", self.home.apartmens_count))  # aprtments count
        self.dataBlock.write(st.pack("<I", self.home.inhabs_count))  # inhabs count
        self.dataBlock.write(st.pack("<I", self.home.maxID))  # maxID
        self.outSet()  # write outrooms

    def outSet(self):
        prew_size = 0
        self.dataBlock.write(st.pack("<I", len(self.home.outrooms)))  # outrooms inhabs count
        # write address list
        for ap in self.home.outrooms:
            self.dataBlock.write(st.pack("<II", ap.id, prew_size))  # address & id write
            prew_size += ap.sizeof()
        for ap in self.home.outrooms:
            self.inhabSet(ap)

    def inhabSet(self, inh: InhabitantNode):
        pib, ag = inh.get()
        pib = pib.encode("utf-8")
        # header
        self.dataBlock.write(st.pack("<B", 2))
        self.dataBlock.write(st.pack("<BI", self.__x("0x10"), 0))  # PIB position
        self.dataBlock.write(st.pack("<BI", self.__x("0x11"), 4 + len(pib)))  # age position
        # data
        self.dataBlock.write(st.pack("<I", len(pib)))  # PIB size
        self.dataBlock.write(pib)  # PIB
        self.dataBlock.write(st.pack("<I", ag))  # age


    def apartmentsSet(self, aps: ApartmentNode):
        self.dataBlock.write(st.pack("<B", 3))
        self.dataBlock.write(st.pack("<BI", self.__x("0x12"), 0))  # rooms count
        self.dataBlock.write(st.pack("<BI", self.__x("0x13"), 4))  # inhabs count
        self.dataBlock.write(st.pack("<BI", self.__x("0x1"), 8))  # inhabs ids&positions

        self.dataBlock.write(st.pack("<I", aps.rooms_count))  # rooms count
        self.dataBlock.write(st.pack("<I", aps.inhabs_count))  # inhabitants count


        habs = aps.get_habitants()
        self.dataBlock.write(st.pack("<I", len(habs)))  # inhabitants startpos
        prew_size = 0
        for inh in habs:
            self.dataBlock.write(st.pack("<II", inh.id, prew_size))
            prew_size += inh.sizeof()

        for inh in habs:
            self.inhabSet(inh)

    def floorSet(self, fr: FloorNode):
        # header
        self.dataBlock.write(st.pack("<B", 3))
        self.dataBlock.write(st.pack("<BI", self.__x("0x13"), 0))  # inhabs count
        self.dataBlock.write(st.pack("<BI", self.__x("0x15"), 4))  # apartments count
        self.dataBlock.write(st.pack("<BI", self.__x("0x1"), 8))  # apartments id&position
        # data
        self.dataBlock.write(st.pack("<I", fr.inhabs_count))
        self.dataBlock.write(st.pack("<I", fr.apartmens_count))

        aps = fr.get_apartments()
        self.dataBlock.write(st.pack("<I", len(aps)))  # apartmets count
        prew_size = 0
        for ans in aps:
            self.dataBlock.write(st.pack("<II", ans.id, prew_size))
            prew_size += ans.sizeof()

        for ans in aps:
            self.apartmentsSet(ans)

    def innerSet(self):
        frs = self.home.get_floors()
        self.dataBlock.write(st.pack("<I", len(frs)))  # floors count
        prew_size = 0
        for fs in frs:
            self.dataBlock.write(st.pack("<II", fs.id, prew_size))  # address & id write
            prew_size += fs.sizeof()
        for fs in frs:
            self.floorSet(fs)
