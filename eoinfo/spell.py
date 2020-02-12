from spell_type import Type
from spell_target import Target
from spell_target_restrict import TargetRestrict


class Spell:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.shout = ""
        self.icon = 0
        self.graphic = 0
        self.tp = 0
        self.sp = 0
        self.cast_time = 0
        self.type = Type.Damage
        self.target_restrict = TargetRestrict.Npc_Only
        self.target = Target.Normal
        self.min_damage = 0
        self.max_damage = 0
        self.accuracy = 0
        self.hp = 0
