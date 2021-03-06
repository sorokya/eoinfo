from item import Item
from item_type import Type
from item_sub_type import SubType
from item_special import Special
from item_size import Size
import utils


class ItemReader:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.data_size = 58
        self.length = 0
        self.position = 0
        self._item = None

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

        item = Item()
        item.id = self.position
        name_size = utils.decode_number(self.file.read(1))
        item.name = self.file.read(name_size).decode("utf-8")

        if item.name == "eof":
            return False

        buf = self.file.read(self.data_size)
        item.graphic = utils.decode_number([buf[0], buf[1]])
        item.type = Type(utils.decode_number([buf[2]]))
        item.sub_type = SubType(utils.decode_number([buf[3]]))
        item.special = Special(utils.decode_number([buf[4]]))

        item.hp = utils.decode_number([buf[5], buf[6]])
        item.tp = utils.decode_number([buf[7], buf[8]])

        item.min_damage = utils.decode_number([buf[9], buf[10]])
        item.max_damage = utils.decode_number([buf[11], buf[12]])
        item.accuracy = utils.decode_number([buf[13], buf[14]])
        item.evade = utils.decode_number([buf[15], buf[16]])
        item.armor = utils.decode_number([buf[17], buf[18]])

        item.str = utils.decode_number([buf[20]])
        item.int = utils.decode_number([buf[21]])
        item.wis = utils.decode_number([buf[22]])
        item.agi = utils.decode_number([buf[23]])
        item.con = utils.decode_number([buf[24]])
        item.cha = utils.decode_number([buf[25]])

        item.light = utils.decode_number([buf[26]])
        item.dark = utils.decode_number([buf[27]])
        item.earth = utils.decode_number([buf[28]])
        item.air = utils.decode_number([buf[29]])
        item.water = utils.decode_number([buf[30]])
        item.fire = utils.decode_number([buf[31]])

        temp = utils.decode_number([buf[32], buf[33], buf[34]])
        if item.type == Type.Teleport:
            item.scroll_map = temp
        elif item.type == Type.EXPReward:
            item.exp_reward = temp
        elif item.type == Type.HairDye:
            item.hair_color = temp
        elif item.type == Type.EffectPotion:
            item.effect = temp
        elif item.type == Type.Key:
            item.key = temp
        else:
            item.doll_graphic = temp

        temp = utils.decode_number([buf[35]])
        if item.type == Type.Teleport:
            item.scroll_x = temp
        else:
            item.gender = temp

        temp = utils.decode_number([buf[36]])
        if item.type == Type.Teleport:
            item.scroll_y = temp
        else:
            item.dual_wield_doll_graphic = temp

        if item.is_equipable():
            item.level_req = utils.decode_number([buf[37], buf[38]])
            item.class_req = utils.decode_number([buf[39], buf[40]])
            item.str_req = utils.decode_number([buf[41], buf[42]])
            item.int_req = utils.decode_number([buf[43], buf[44]])
            item.wis_req = utils.decode_number([buf[45], buf[46]])
            item.agi_req = utils.decode_number([buf[47], buf[48]])
            item.con_req = utils.decode_number([buf[49], buf[50]])
            item.cha_req = utils.decode_number([buf[51], buf[52]])

        item.weight = utils.decode_number([buf[55]])
        item.size = Size(utils.decode_number([buf[57]]))

        self._item = item
        self.position += 1
        return True

    @property
    def item(self):
        return self._item
