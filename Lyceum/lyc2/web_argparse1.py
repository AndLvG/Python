import argparse
import sys

c = 1
arg = []
parser = argparse.ArgumentParser()
if len(sys.argv[1:]) > 1:
    for el in sys.argv[1:]:
        parser.add_argument(f"arg{c}")
        arg.append(f"arg{c}")
    args = parser.parse_args()
    for el in arg:
        print(args.el)
else:
    print("no args")