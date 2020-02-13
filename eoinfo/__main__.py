import argparse
import sys
from item_reader import ItemReader
from item_printer import ItemPrinter
from npc_reader import NpcReader
from npc_printer import NpcPrinter
from spell_reader import SpellReader
from spell_printer import SpellPrinter


def get_args():
    description = "eoinfo - your offline data explorer for Endless Online"
    arg = argparse.ArgumentParser(description=description)

    arg.add_argument("-i", help="Search for items")
    arg.add_argument("-n", help="Search for NPCs")
    arg.add_argument("-s", help="Search for spells")
    arg.add_argument("-c", help="Search for classes")

    arg.add_argument("-p", help="Path to Endless Online directory")

    return arg


def parse_args_exit(parser):
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()
        sys.exit(1)


def print_items(search_term):
    item_reader = ItemReader("pub/dat001.eif")
    item_printer = ItemPrinter()
    while item_reader.read():
        item_printer.print(item_reader.item)


def print_npcs(search_term):
    npc_reader = NpcReader("pub/dtn001.enf")
    npc_printer = NpcPrinter()
    while npc_reader.read():
        npc_printer.print(npc_reader.npc)


def print_spells(search_term):
    spell_reader = SpellReader("pub/dsl001.esf")
    spell_printer = SpellPrinter()
    while spell_reader.read():
        spell_printer.print(spell_reader.spell)

def print_classes(search_term):
    print(search_term)


def parse_args(parser):
    args = parser.parse_args()

    if args.i:
        print_items(args.i)

    if args.n:
        print_npcs(args.n)

    if args.s:
        print_spells(args.s)

    if args.c:
        print_classes(args.c)


def main():
    parser = get_args()
    parse_args_exit(parser)
    parse_args(parser)


if __name__ == "__main__":
    main()
