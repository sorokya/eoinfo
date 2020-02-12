from npc_type import Type


class Npc:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.graphic = 0
        self.boss = 0
        self.child = 0
        self.type = Type.NPC
        self.vendor_id = 0
        self.hp = 0
        self.exp = 0
        self.min_damage = 0
        self.max_damage = 0
        self.accuracy = 0
        self.evade = 0
        self.armor = 0
