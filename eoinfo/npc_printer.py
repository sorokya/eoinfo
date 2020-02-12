from tabulate import tabulate
from npc_type import Type


class NpcPrinter:
    def __init__(self):
        self.npc = None

    def print(self, npc):
        self.npc = npc
        print(f"{self.npc.id} - {self.npc.name}")
