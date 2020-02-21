import argparse

parser = argparse.ArgumentParser()

parser.add_argument('source_file', type=str, help='файл источник')
parser.add_argument('destination_file', type=str, help='файл для записи')
parser.add_argument('--upper', action="store_true", required=False, help='привести к верхнему регистру')
parser.add_argument('--lines', type=int, required=False, help='количество строк')

args = parser.parse_args()

with open(args.source_file, 'rt') as file_s:
    data = file_s.read().split('\n')
    print(args.lines)
    if args.lines:
        strok = min(args.lines, len(data))
    else:
        strok = len(data)
    print(strok)
    data = data[:strok]
    if args.upper:
        data = [x.upper() for x in data]
    print(data)

with open(args.destination_file, 'wt') as file_d:
    file_d.writelines("%s\n" % line for line in data)
