def human_read_format(size):
    c = 0
    bites = ["Б", "КБ", "МБ", "ГБ"]
    while size // 1024 > 0:
        size = size / 1024
        c += 1
    return f"{round(size)}{bites[c]}"

print(human_read_format(100025))