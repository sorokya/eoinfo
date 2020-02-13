from tabulate import tabulate
from spell_type import Type


class SpellPrinter:
    def __init__(self):
        self.spell = None
    
    def print(self, spell):
        self.spell = spell
        print(f"{self.spell.id} - {self.spell.name}")
