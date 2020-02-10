from enum import Enum

class Item:
    def __init__(self):
        self.id = 0

    def print(self):
        print(f"{self.id} - {self.name}")

class Special(Enum):
    Normal = 0
    Rare = 1
    UnknownSpecial = 2
    Unique = 3
    Lore = 4
    Cursed = 5

class Type(Enum):
    Static = 0
    UnknownType1 = 1
    Money = 2
    Heal = 3
    Teleport = 4
    Spell = 5
    EXPReward = 6
    StatReward = 7
    SkillReward = 8
    Key = 9
    Weapon = 10
    Shield = 11
    Armor = 12
    Hat = 13
    Boots = 14
    Gloves = 15
    Accessory = 16
    Belt = 17
    Necklace = 18
    Ring = 19
    Armlet = 20
    Bracer = 21
    Beer = 22
    EffectPotion = 23
    HairDye = 24
    CureCurse = 25

class SubType(Enum):
    Nil = 0
    Ranged = 1
    Arrows = 2
    Wings = 3
    TwoHanded = 4

class Size(Enum):
    Size1x1 = 0
    Size1x2 = 1
    Size1x3 = 2
    Size1x4 = 3
    Size2x1 = 4
    Size2x2 = 5
    Size2x3 = 6
    Size2x4 = 7
