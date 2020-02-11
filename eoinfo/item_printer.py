from tabulate import tabulate
from item_type import Type

class ItemPrinter:
    def __init__(self):
        self.item = None 

    def print_stats(self):
        if self.item.is_equipable():
            print("Stats:")
            table = [["HP", f"+{self.item.hp}", "TP", f"+{self.item.tp}", "Damage",
                  f"{self.item.min_damage} - {self.item.max_damage}"],
                 ["STR", f"+{self.item.str}", "INT", f"+{self.item.int}", "Accuracy",
                  f"{self.item.accuracy}"],
                 ["WIS", f"+{self.item.wis}", "AGI", f"+{self.item.agi}", "Armor",
                  f"{self.item.armor}"],
                 ["CON", f"+{self.item.con}", "CHA", f"+{self.item.cha}", "Evade",
                  f"{self.item.evade}"]]
            print(tabulate(table, tablefmt="fancy_grid"))

    def print_requirements(self):
        if self.item.is_equipable():
            table = []
            if self.item.level_req > 0:
                table.append(["Level", self.item.level_req])
            if self.item.class_req > 0:
                table.append(["Class", self.item.class_req]) # todo: use class name
            if self.item.str_req > 0:
                table.append(["Str", self.item.str_req])
            if self.item.int_req > 0:
                table.append(["Int", self.item.int_req])
            if self.item.wis_req > 0:
                table.append(["Wis", self.item.wis_req])
            if self.item.agi_req > 0:
                table.append(["Agi", self.item.agi_req])
            if self.item.con_req > 0:
                table.append(["Con", self.item.con_req])
            if self.item.cha_req > 0:
                table.append(["Cha", self.item.cha_req])
            if len(table) > 0:
                print("Requirements:")
                print(tabulate(table, tablefmt="fancy_grid"))

    def print_effect(self):
        if self.item.type == Type.Teleport:
            print(f"Map: {self.item.scroll_map}, X: {self.item.scroll_x}, Y: {self.item.scroll_y}")
        elif self.item.type == Type.Heal and self.item.hp + self.item.tp > 0:
            print(tabulate([["HP", f"+{self.item.hp}"], ["TP", f"+{self.item.tp}"]],
                tablefmt="fancy_grid"))
        elif self.item.type == Type.EXPReward:
            print(f"EXP: {self.item.exp_reward}")

    def print(self, item):
        self.item = item
        print(f"{self.item.id} - {self.item.name}")
        self.print_stats()
        self.print_requirements()
        self.print_effect()

