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
    except Exception:
        print(0)


if __name__ == "__main__":
    count_lines(filename)
