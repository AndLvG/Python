from sys import stdin

Rasp = {}

for el in stdin:
    line = el.strip()  # убираем пробелы со всех сторон
    if line != "" and line[-1].isdigit():  # проверяем что строка не пустая и первый символ с конца это цифра
        ind = line.rfind(" ")  # находим первый пробел с конца - по нему и будем отделять номер кабинета
        lesson = line[:ind]  # это название урока до последнего пробела
        # print(lesson)
        kabinet = line[ind + 1:]  # это номер кабинета от последнего пробела
        # print(kabinet)
        if kabinet in Rasp.keys():  # если такой ключ уже есть в словаре
            if lesson not in Rasp[kabinet]:  # смотрим может такой предмет уже есть в этом ключе и это повтор
                Rasp[kabinet] = Rasp[kabinet] + ', ' + lesson  # через запятую доавялем урок
        else:  # если нет - просто добавляем новый
            Rasp[kabinet] = lesson

print(Rasp)
