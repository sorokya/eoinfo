from spell import Spell
from spell_type import Type
from spell_target import Target
from spell_target_restrict import TargetRestrict
import utils


class SpellReader:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.data_size = 51
        self.length = 0
        self.position = 0
        self._spell = None

    def __del__(self):
        if self.file:
            self.file.close()

    def open_file(self):
        self.file = open(self.path, "rb")
        self.file.seek(7)
        self.length = utils.decode_number(self.file.read(2))
        self.file.seek(1, 1)
        self.position = 1

    def read(self):
        if self.file is None:
            self.open_file()

        if self.position > self.length:
            return False

        spell = Spell()
        spell.id = self.position
        name_size = utils.decode_number(self.file.read(1))
        shout_size = utils.decode_number(self.file.read(1))
        spell.name = self.file.read(name_size).decode("utf-8")
        spell.shout = self.file.read(shout_size).decode("utf-8")

        if spell.name == "eof":
            return False

        buf = self.file.read(self.data_size)
        spell.icon = utils.decode_number([buf[0], buf[1]])
        spell.graphic = utils.decode_number([buf[2], buf[3]])
        spell.tp = utils.decode_number([buf[4], buf[5]])
        spell.sp = utils.decode_number([buf[6], buf[7]])
        spell.cast_time = utils.decode_number([buf[8]])
        spell.type = Type(utils.decode_number([buf[11]]))
        spell.target_restrict = TargetRestrict(utils.decode_number([buf[17]]))
        spell.target = Target(utils.decode_number([buf[18]]))
        spell.min_damage = utils.decode_number([buf[23], buf[24]])
        spell.max_damage = utils.decode_number([buf[25], buf[26]])
        spell.accuracy = utils.decode_number([buf[27], buf[28]])
        spell.hp = utils.decode_number([buf[34], buf[35]])

        self._spell = spell
        self.position += 1
        return True

    @property
    def spell(self):
        return self._spell
