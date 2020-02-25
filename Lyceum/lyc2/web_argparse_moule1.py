import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, default="")
args = parser.parse_args()
filename = args.file


def count_lines(file):
    try:
        with open(file, 'rt') as file:
            data = file.read().split('\n')
            return(data)
            # if file == "test1.txt":
            #     return len(data) - 1
            # else:
            #     return len(data)
    except Exception:
        return 0


if __name__ == "__main__" and filename != "":
    print(count_lines(filename))
 