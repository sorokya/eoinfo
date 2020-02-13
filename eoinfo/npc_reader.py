from npc import Npc
from npc_type import Type
import utils

class NpcReader:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.data_size = 39 # data buffer size for one npc
        self.length = 0
        self.position = 0
        self._npc = None

    def __del__(self):
        if self.file:
            self.file.close()

    def open_file(self):
        self.file = open(self.path, "rb")

        # skips the file identifier and revision ID
        self.file.seek(7)
        self.length = utils.decode_number(self.file.read(2))
        self.file.seek(1, 1)
        self.position = 1

    def read(self):
        if self.file is None:
            self.open_file()

        # kills the loop if we've reached the end of the file
        if self.position > self.length:
            return False

        npc = Npc()
        npc.id = self.position
        
        # name is dynamic, so we need to find the size each time
        name_size = utils.decode_number(self.file.read(1))
        npc.name = self.file.read(name_size).decode("utf-8")

        # eof means end of file. It should be the last "record"
        # and we can safely ignore it.
        if npc.name == "eof":
            return False

        buf = self.file.read(self.data_size)
        npc.graphic = utils.decode_number([buf[0], buf[1]])
        npc.boss = utils.decode_number([buf[3], buf[4]])
        npc.child = utils.decode_number([buf[5], buf[6]])
        npc.type = Type(utils.decode_number([buf[7], buf[8]]))
        npc.vendor_id = utils.decode_number([buf[9], buf[10]])
        npc.hp = utils.decode_number([buf[11], buf[12], buf[13]])
        npc.min_damage = utils.decode_number([buf[16], buf[17]])
        npc.max_damage = utils.decode_number([buf[18], buf[19]])
        npc.accuracy = utils.decode_number([buf[20], buf[21]])
        npc.evade = utils.decode_number([buf[22], buf[23]])
        npc.armor = utils.decode_number([buf[24], buf[25]])
        npc.exp = utils.decode_number([buf[36], buf[37]])
        
        self._npc = npc
        self.position += 1
        return True

    @property
    def npc(self):
        return self._npc
