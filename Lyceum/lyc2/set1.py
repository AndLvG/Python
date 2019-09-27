from sys import stdin

lines = []

for el in stdin:
    lines.append(el)
print('Залили в список')
print(lines)
print()
print('Теперь все элементы соединим в одну строку заменив конец строки на пробел')
line = "".join(lines).replace("\n", " ")
print(line)
print()

#  Создаём множества для каждого варианта
tochka_set = set()
vopros_set = set()
voskl_set = set()

print('Теперь можем сделать список из слов')
words = line.split()
print(words)
print()

#  Временный список куда будем класть слова пока не поймем какое это предложение . ! ?
temp = []

for w in words:
    if w[-1] not in '.?!':  # Если слово не кончается на .!? то это не конец предложения. Просто добавляем
        temp.append(w.lower())
    else:  # Если кончается то по последнему символу определяем тип предложения и добавялем
        #  в соответствующее множество
        temp.append(w[:-1].lower())
        if w[-1] == '.':
            tochka_set.update(temp)
        elif w[-1] == '?':
            vopros_set.update(temp)
        elif w[-1] == '!':
            voskl_set.update(temp)
        temp.clear()  # не забыть очистить временный список
print('Вот получились какие множества')
print('Предложения с точкой: ', *tochka_set)
print('Предложения с вопросом: ', *vopros_set)
print('Предложения с воскл знаком: ', *voskl_set)
print()

#  Теперь самое интересное. Делаем пересечение множества с точкой и вопросом
#  Т.е. получаем элементы которые есть в обеих множествах
new_set = tochka_set.intersection(vopros_set)
print('Вот остались слова которые есть и в повествовательных, и в вопросительных предложениях')
print(new_set)
print()
#  Теперь из них вычитаем те слова которые есть в восклицательных (по условию задачи)
diff_set = new_set.difference(voskl_set)
print(
    'Остались только те слова которые встречаются одновременно и в повествовательных, и в вопросительных предложениях, но не встречаются в восклицательных')
print(diff_set)
