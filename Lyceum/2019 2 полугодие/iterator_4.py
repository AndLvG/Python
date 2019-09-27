from functools import reduce

text = ['котик', 'тюлень', 'кашалот', 'нарвал']


def reducer_func(el_prev, el):
    # el_prev — предшествующий элемент
    # el — текущий элемент
    return min(el_prev, el)


print(reduce(reducer_func, text))
