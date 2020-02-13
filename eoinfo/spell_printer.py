from tabulate import tabulate
from spell_type import Type


class SpellPrinter:
    def __init__(self):
        self.spell = None

    def print_stats(self):
        if self.spell.type != Type.Bard:
            print("Stats:")
            table = [["TP Cost", f"{self.spell.tp}",
                      "SP Cost", f"{self.spell.sp}"]]

            if self.spell.type == Type.Heal:
                table.append(["HP", f"{self.spell.hp}"])
            else:
                min_damage = self.spell.min_damage
                max_damage = self.spell.max_damage
                table.append(["Damage", f"{min_damage} - {max_damage}",
                              "Accuracy", f"{self.spell.accuracy}"])

            print(tabulate(table, tablefmt="fancy_grid"))

    def print(self, spell):
        self.spell = spell
        print(f"{self.spell.id} - {self.spell.name}")
        self.print_stats()
