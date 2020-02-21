import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file', type=str)
parser.add_argument('--count', action="store_true")
parser.add_argument('--num', action="store_true")
parser.add_argument('--sort', action="store_true")

args = parser.parse_args()

try:
    filename = args.file

    with open(filename, 'rt') as file:
        data = file.read().split('\n')
        if args.sort:
            data = sorted(data)

        for i, el in enumerate(data):
            if args.num:
                print(i, el)
            else:
                print(el)

        if args.count:
            print(f'rows count: {len(data)}')

except Exception:
    print('ERROR')

# python web_argparse6.py --num text1.txt
# python web_argparse6.py --count --sort text1.txt
