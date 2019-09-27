one = input()
two = input()
if one == two:
    print('ничья')
elif one == 'камень':
    if two == 'ножницы':
        print('первый')
    elif two == 'ром':
        print('первый')
    elif two == 'пират':
        print('второй')
    else:
        print('второй')
elif one == 'ножницы':
    if two == 'бумага':
        print('первый')
    elif two == 'ром':
        print('первый')
    elif two == 'пират':
        print('второй')
    else:
        print('второй')
elif one == 'бумага':
    if two == 'ножницы':
        print('второй')
    elif two == 'ром':
        print('второй')
    elif two == 'пират':
        print('первый')
    else:
        print('первый')
elif one == 'ром':
    if two == 'бумага':
        print('первый')
    elif two == 'камень':
        print('второй')
    elif two == 'ножницы':
        print('второй')
    else:
        print('первый')
elif one == 'пират':
    if two == 'ножницы':
        print('первый')
    elif two == 'камень':
        print('первый')
    elif two == 'бумага':
        print('второй')
    else:
        print('второй')
