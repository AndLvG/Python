import os


def human_read_format(size):
    c = 0
    bites = ["Б", "КБ", "МБ", "ГБ"]
    while size // 1024 > 0:
        size = size / 1024
        c += 1
    return f"{round(size)}{bites[c]}"


def get_ﬁles_sizes():
    files = []
    for el in next(os.walk(os.getcwd()))[2]:
        size = os.path.getsize(f"{os.getcwd()}/{el}")
        files.append(f"{el} {human_read_format(size)}")
    return "\n".join(files)


def get_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def get_dir_sizes(start_path=os.getcwd()):
    files = {}
    for f in os.listdir(start_path):
        if os.path.isdir(f):
            files[f] = get_size(f)
    return files


dirs = get_dir_sizes()
dirs = sorted(dirs.items(), key=lambda x: x[1], reverse=True)[:10]
max_l = len(max(dirs, key=lambda x: len(x[0]))[0])
for el in dirs:
    name = el[0] + ' ' * (max_l - len(el[0]) + 1) + '-'
    print(f"{name} {human_read_format(el[1])}")
