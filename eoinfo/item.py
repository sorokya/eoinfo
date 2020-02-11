from item_type import Type
from item_sub_type import SubType
from item_special import Special
from item_size import Size


class Item:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.graphic = 0
        self.type = Type.Static
        self.sub_type = SubType.Nil
        self.special = Special.Normal
        self.hp = 0
        self.tp = 0
        self.min_damage = 0
        self.max_damage = 0
        self.accuracy = 0
        self.evade = 0
        self.armor = 0
        self.str = 0
        self.int = 0
        self.wis = 0
        self.agi = 0
        self.con = 0
        self.cha = 0
        self.light = 0
        self.dark = 0
        self.earth = 0
        self.air = 0
        self.water = 0
        self.fire = 0
        self.scroll_map = 0
        self.exp_reward = 0
        self.hair_color = 0
        self.effect = 0
        self.key = 0
        self.doll_graphic = 0
        self.scroll_x = 0
        self.gender = 0
        self.scroll_y = 0
        self.dual_wield_doll_graphic = 0
        self.level_req = 0
        self.class_req = 0
        self.str_req = 0
        self.int_req = 0
        self.wis_req = 0
        self.agi_req = 0
        self.con_req = 0
        self.cha_req = 0
        self.weight = 0
        self.size = Size.Size1x1

    def is_equipable(self):
        return self.type in [Type.Weapon, Type.Shield, Type.Armor, Type.Hat, Type.Boots,
                             Type.Gloves, Type.Accessory, Type.Belt, Type.Necklace, Type.Ring,
                             Type.Armlet, Type.Bracer]

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
                table.append(["Class", self.class_req])  # todo: use class name
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
            print(
                f"Map: {self.scroll_map}, X: {self.scroll_x}, Y: {self.scroll_y}")
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
