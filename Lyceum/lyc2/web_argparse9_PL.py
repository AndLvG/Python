import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--barbie', default=50, type=int,
                    help='отношение к куклам от 0 до 100')
parser.add_argument('--cars', default=50, type=int,
                    help='отношение к машинам от 0 до 100')
parser.add_argument('--movie', default='other', type=str,
                    choices=('melodrama', 'football', 'other'),
                    help='любимая ТВ программа')

args = parser.parse_args()

barbie = args.barbie
cars = args.cars
mov = args.movie

if mov == 'melodrama':
    movie = 0
elif mov == 'football':
    movie = 100
elif mov == 'other':
    movie = 50

boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - boy

print(f'boy: {boy}')
print(f'girl: {girl}')

# python web_argparse2.py --cars 80 --barbie 0 --movie football