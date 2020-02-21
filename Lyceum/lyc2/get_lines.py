import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file', type=str)
args = parser.parse_args()
filename = args.file


def count_lines(file_path):
    try:
        with open(file_path, 'rt') as file:
            data = file.read().split('\n')
            print(len(data))
    except Exception as pe:
        print('0')


if __name__ == "__main__":
    count_lines(filename)

# python get_lines.py --file text1.txt"

# from get_lines import count_lines
#
# print(count_lines('text1.txt'))
