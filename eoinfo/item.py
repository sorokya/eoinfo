from enum import Enum
from tabulate import tabulate

class Item:
    def __init__(self):
        self.id = 0

    def is_equipable(self):
        if self.type in [Type.Weapon, Type.Shield, Type.Armor, Type.Hat, Type.Boots,
                         Type.Gloves, Type.Accessory, Type.Belt, Type.Necklace,
                         Type.Ring, Type.Armlet, Type.Bracer]:
            return True

        return False

    def print_stats(self):
        if self.is_equipable():
            print("Stats:")
            table = [["HP", f"+{self.hp}", "TP", f"+{self.tp}", "Damage",
                  f"{self.min_damage} - {self.max_damage}"],
                 ["STR", f"+{self.str}", "INT", f"+{self.int}", "Accuracy",
                  f"{self.accuracy}"],
                 ["WIS", f"+{self.wis}", "AGI", f"+{self.agi}", "Armor",
                  f"{self.armor}"],
                 ["CON", f"+{self.con}", "CHA", f"+{self.cha}", "Evade",
                  f"{self.evade}"]]
            print(tabulate(table, tablefmt="fancy_grid"))

    def print_requirements(self):
        if self.is_equipable():
            table = []
            if self.level_req > 0:
                table.append(["Level", self.level_req])
            if self.class_req > 0:
                table.append(["Class", self.class_req]) # todo: use class name
            if self.str_req > 0:
                table.append(["Str", self.str_req])
            if self.int_req > 0:
                table.append(["Int", self.int_req])
            if self.wis_req > 0:
                table.append(["Wis", self.wis_req])
            if self.agi_req > 0:
                table.append(["Agi", self.agi_req])
            if self.con_req > 0:
                table.append(["Con", self.con_req])
            if self.cha_req > 0:
                table.append(["Cha", self.cha_req])
            if len(table) > 0:
                print("Requirements:")
                print(tabulate(table, tablefmt="fancy_grid"))

    def print_effect(self):
        if self.type == Type.Teleport:
            print(f"Map: {self.scroll_map}, X: {self.scroll_x}, Y: {self.scroll_y}")
        elif self.type == Type.Heal and self.hp + self.tp > 0:
            print(tabulate([["HP", f"+{self.hp}"], ["TP", f"+{self.tp}"]],
                tablefmt="fancy_grid"))
        elif self.type == Type.EXPReward:
            print(f"EXP: {self.exp_reward}")


    def print(self):
        print(f"{self.id} - {self.name}")
        self.print_stats()
        self.print_requirements()
        self.print_effect()
        print('')

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
