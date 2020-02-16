import re

ENG = "qwertyuiopasdfghjklzxcvbnm"
RUS = "йцукенгшщзхъфывапролджэячсмитьбю"




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


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass  # если длина пароля меньше 9 символов.


class LetterError(PasswordError):
    pass  # если в пароле все символы одного регистра.


class DigitError(PasswordError):
    pass  # если в пароле нет ни одной цифры.


class SequenceError(PasswordError):
    # если пароль нарушает требование к последовательности из подряд идущих трех символов (указано в предыдущей задаче).
    pass


def Length(p):
    if len(p) < 9:
        raise LengthError()


def Letter(p):
    if p == p.lower() or p == p.upper():
        raise LetterError()


def Digit(p):
    if not check_number(p):
        raise DigitError()


def Sequence(p):
    if not check_klawa(p):
        raise SequenceError()


def check_password(password):
    for func in (Length, Letter, Digit, Sequence):
        try:
            func(password)
        except PasswordError as pe:
            print(pe.__class__.__name__)
            return False
    return True
           
def process():
    while True:
        try:
            passwd = input('Введите пароль: ')
            if passwd == 'Ctrl+Break':
                raise KeyboardInterrupt
            if check_password(passwd):
                print("ok")
                break
        except KeyboardInterrupt:
            print("Bye-Bye")
            break


process()

# check_password(passwd)
