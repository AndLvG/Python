def print_operation_table(operation, num_rows=9, num_columns=9):
    #  Запускаем цикл i по строкам
    for i in range(1, num_rows + 1):
        #  Внутри щапускаем цикл по столбцам для каждой строки
        #  Берём элемент (i, k) и посылаем его в указанную операция
        #  В первом случае lambda x, y: x * y получает 2 элемента и возвращает их умножение

        #  Во втором случае тоже самое только ограничено числом 5 - lambda x, y: x * y, 5 (не понимаю как это работает - ты мне обясниш тогда при случае)
        print(*(operation(i, k) for k in range(1, num_columns + 1)))


print_operation_table(lambda x, y: x * y)

print_operation_table(lambda x, y: x * y, 5)
