import os


def human_read_format(size):
    c = 0
    bites = ["Б", "КБ", "МБ", "ГБ"]
    while size // 1024 > 0:
        size = size / 1024
        c += 1
    return f"{round(size)}{bites[c]}"


def get_ﬁles_sizes(filenames):
    files = []
    for el in filenames:
        size = os.path.getsize(f"{os.getcwd()}/{el}")
        files.append(f"{el} {human_read_format(size)}")
    return "\n".join(files)


filenames = next(os.walk(os.getcwd()))[2]
files_size = get_ﬁles_sizes(filenames)

print(files_size)
