import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--per-day', type=float)
parser.add_argument('--per-week', type=float)
parser.add_argument('--per-month', type=float)
parser.add_argument('--per-year', type=float)
parser.add_argument('--get-by', default='day', type=str,
                    choices=['day', 'month', 'year'])

args = parser.parse_args()

# print(args)


def is_none(arg):
    if arg is None:
        return 0
    return arg


if args.get_by == 'month':
    result = int(is_none(args.per_day * 30 + is_none(args.per_week) / 7 * 30))
elif args.get_by == 'day':
    result = int(is_none(args.per_day) + is_none(args.per_year) / 360)
elif args.get_by == 'year':
    result = int(is_none(args.per_day) * 360 + is_none(args.per_week) / 7 * 360
                 + is_none(args.per_month) / 30 * 360 + is_none(args.per_year))

print(result)

# python web_argparse9_PL.py --per-day +1 --per-week -7 --get-by month

# python web_argparse9_PL.py --per-day 1 --per-week -14 --per-year 360 --per-month 7 --get-by what
# python web_argparse9_PL.py --per-year +360 --per-day -2
# python web_argparse9_PL.py --per-day 1 --per-week -14 --per-year 360 --per-month 7 --get-by year
