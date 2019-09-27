def arithmetic_operation(oper):
    def func(a, b):
        return eval('{}{}{}'.format(a, oper, b))
    return func


operation = arithmetic_operation('')

#  print(operation(1, 4))