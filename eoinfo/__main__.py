import argparse
import sys

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

def main():
    parser = get_args()
    parse_args_exit(parser)

if __name__ == "__main__":
    main()
