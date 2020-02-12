from tabulate import tabulate
from npc_type import Type


class NpcPrinter:
    def __init__(self):
        self.npc = None
    
    def print_stats(self):
        if self.npc.type in [Type.Passive, Type.Aggressive]:
            print("Stats:")
            min_damage = self.npc.min_damage
            max_damage = self.npc.max_damage
            table = [["HP", f"{self.npc.hp}",
                      "EXP", f"{self.npc.exp}"],

                     ["Damage", f"{min_damage} - {max_damage}",
                      "Accuracy", f"{self.npc.accuracy}"],

                     ["Armor", f"{self.npc.armor}",
                      "Evade", f"{self.npc.evade}"]]

            print(tabulate(table, tablefmt="fancy_grid"))

    def print(self, npc):
        self.npc = npc
        print(f"{self.npc.id} - {self.npc.name}")
        self.print_stats()
