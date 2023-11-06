import io
import struct as st
from Nodes import *
from .Reader import *


class MdpReader(Reader):
    mask = {
        "0x10": "_InhabitantNode__PIB",
        "0x11": "_InhabitantNode__Age",
        "0x12": "rooms_count",
        "0x13": "inhabs_count",
        "0x14": "floor_count",
        "0x15": "apartmens_count",
        "0x16": "maxID"
    }

    def __init__(self, home: HomeNode, name):
        self.name: str = name
        self.home: HomeNode = home
        self.dataBlock = io.BytesIO()
        self.load()

    def __x(self, h: str):
        return int(h, 16)


    def load(self):
        try:
            with open(self.name, 'rb') as f:
                self.dataBlock.write(f.read())
        except IOError as e:
            print("MDP reader Error!")
            print(e)

    def get(self, form):
        return st.unpack(form, self.dataBlock.read(st.calcsize(form)))

    def read_list(self, func, parent=None):
        icnt, = self.get("<I")
        startPos = self.dataBlock.tell() + (icnt * 8)
        for oin in range(icnt):
            _id, _pos = self.get("<II")
            curPos = self.dataBlock.tell()
            self.dataBlock.seek(startPos + _pos)
            func(_id, parent)
            self.dataBlock.seek(curPos)

    def read_inhabitant(self, identifier, parent=None):
        icnt, = self.get("<B")
        inab = InhabitantNode("", 20, self.home)
        inab.id = identifier
        inab.parent = parent
        startPos = self.dataBlock.tell() + (icnt * 5)
        for hda in range(icnt):
            _id, _pos = self.get("<BI")
            curPos = self.dataBlock.tell()
            self.dataBlock.seek(startPos + _pos)
            if _id == self.__x("0x10"):
                ts, = self.get("<I")
                inab.__dict__[MdpReader.mask[hex(_id)]] = self.dataBlock.read(ts).decode("utf-8")
            elif _id == self.__x("0x11"):
                inab.__dict__[MdpReader.mask[hex(_id)]], = self.get("<I")
            self.dataBlock.seek(curPos)
        if parent is None:
            self.home.outrooms.append(inab)
        else:
            inab.parent.__dict__[hex(identifier)[1:]] = inab



    def read_apartment(self, identifier, parent=None):
        icnt, = self.get("<B")
        apar = ApartmentNode(self.home)
        apar.id = identifier
        apar.parent = parent
        startPos = self.dataBlock.tell() + (icnt * 5)
        for hda in range(icnt):
            _id, _pos = self.get("<BI")
            curPos = self.dataBlock.tell()
            self.dataBlock.seek(startPos + _pos)
            if _id >= self.__x("0x10"):
                apar.__dict__[MdpReader.mask[hex(_id)]], = self.get("<I")
            elif _id == self.__x("0x1"):
                self.read_list(self.read_inhabitant, apar)
            self.dataBlock.seek(curPos)
        apar.parent.__dict__[hex(identifier)[1:]] = apar


    def read_floor(self, identifier, parent=None):
        icnt, = self.get("<B")
        flor = FloorNode(self.home)
        flor.id = identifier
        flor.parent = self.home
        startPos = self.dataBlock.tell() + (icnt * 5)
        for hda in range(icnt):
            _id, _pos = self.get("<BI")
            curPos = self.dataBlock.tell()
            self.dataBlock.seek(startPos + _pos)
            if _id >= self.__x("0x10"):
                flor.__dict__[MdpReader.mask[hex(_id)]], = self.get("<I")
            elif _id == self.__x("0x1"):
                self.read_list(self.read_apartment, flor)
            self.dataBlock.seek(curPos)
        self.home.__dict__[hex(identifier)[1:]] = flor


    def read_header(self):
        self.dataBlock.seek(0)
        if self.dataBlock.read(3).decode('utf-8') != "MDP":
            raise Exception("Error Format\nUnknown file!")
        self.home.id, pos = self.get("<II")
        dc, = self.get("<B")
        startPos = self.dataBlock.tell()+(dc*5)
        for ds in range(dc):
            _id, _pos = self.get("<BI")
            curPos = self.dataBlock.tell()
            self.dataBlock.seek(startPos + _pos)
            if _id >= self.__x("0x10"):
                self.home.__dict__[MdpReader.mask[hex(_id)]], = self.get("<I")
            elif _id == self.__x("0x2"):
                self.read_list(self.read_inhabitant)
            elif _id == self.__x("0x1"):
                self.read_list(self.read_floor)
            self.dataBlock.seek(curPos)




