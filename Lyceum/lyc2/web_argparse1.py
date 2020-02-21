import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
args = parser.parse_args()

if len(args.arg) > 0:
    for i in args.arg:
        print(i)
else:
    print('no args')
