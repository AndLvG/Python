import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--per-day', type=float)
parser.add_argument('--per-week', type=float)
parser.add_argument('--per-month', type=float)
parser.add_argument('--per-year', type=float)
parser.add_argument('--get-by', default='day', type=str,
                    choices=['day', 'month', 'year'],
                    help='любимая ТВ программа')

args = parser.parse_args()

print(args)


# python web_argparse9_PL.py --per-day +1 --per-week -7 --get-by month