import re

ENG = "qwertyuiopasdfghjklzxcvbnm"
RUS = "йцукенгшщзхъфывапролджэячсмитьбю"

passwd = input('Введите пароль: ')


def check_len(p):
    return len(p) > 8


def check_letters(p):
    return re.search('[A-ZА-Я]', p) and re.search('[a-zа-я]', p)


def check_number(p):
    return re.search('[0-9]', p)


def check_klawa(p):
    for i in range(0, len(p) - 3):
        if p[i:i + 2].lower() in ENG or p[i:i + 2].lower() in RUS:
            return False
    return True

           
if all((check_len(passwd), check_letters(passwd), check_number(passwd), check_klawa(passwd))):
    print('ok')
else:
    print('error')

