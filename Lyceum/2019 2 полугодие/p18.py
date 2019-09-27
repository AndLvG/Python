def same_by(pravilo, objects):
    #  Используем функцию высшего порядка MAP которая преобразует каждый элемент списка
    #  по правилу pravilo и формирует новый список
    #  правило lambda x: x % 2
    #  значит map будет формировать список TRUE (1) если число делится на цело на 2
    #  и FALSE (0) если не делится
    #  Вот что она сделает:
    print(*map(pravilo, objects))

    # здесь опять мы список превращаем во множество SET
    # и если его длина 1 т.е. в данном случае все значения нацело делятся на 2
    return len(set(map(pravilo, objects))) == 1


values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
