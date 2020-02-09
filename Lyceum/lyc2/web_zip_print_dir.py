# import os
from zipfile import ZipFile
# import shutil
# import tempfile


# def printRootStructure(dirname, indent=0):
#     if indent != 0:
#         for _ in range(indent - 2):
#             print(" ", end='')
#         print(os.path.basename(dirname))
#     if os.path.isdir(dirname):
#         for files in os.listdir(dirname):
#             printRootStructure(os.path.join(
#                 dirname, files), indent + 2)


def human_read_format(size):
    c = 0
    bites = ["Б", "КБ", "МБ", "ГБ"]
    while size // 1024 > 0:
        size = size / 1024
        c += 1
    return f"{round(size)}{bites[c]}"


with ZipFile('input.zip') as myzip:
    # temp_dir = f'{tempfile.gettempdir()}\\tt'
    # myzip.extractall(temp_dir)
    # printRootStructure(temp_dir)
    # shutil.rmtree(temp_dir)
    files = []
    f = {}
    # print(myzip.infolist())
    for el in myzip.infolist():
        files.append(el.filename.split('/'))
        if not el.is_dir():
            f[el.filename.split('/')[-1]] = el.file_size
    # print(f)


root = files[0][0]
indent = 2

ready = list()

print(root)


def printZip(root, level, indent):
    filtr1 = list(filter(lambda x: len(x) > level, files))
    filtr2 = list(filter(lambda x: x[level] == root, filtr1))
    for el in filtr2[1:]:
        if el not in ready:
            if el[-1] != '':
                add = f" {human_read_format(f[el[level + 1]])}"
            else:
                add = ''
            print(indent * ' ' + el[level + 1] + add)
            ready.append(el)
        if el[-1] == '':
            printZip(el[level + 1], level + 1, indent + 2)


printZip(root, 0, indent)
