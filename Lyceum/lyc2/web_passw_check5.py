import re

ENG = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
RUS = ["йцукенгшщзхъ", "фывапролджэ", "ячсмитьбю", "фывапролджэё"]

top_passwd = open("top 10000 passwd.txt").read().split()
top_words = open("top-9999-words.txt").read().split()
exceptions = {}


def check_len(p):
    return len(p) > 8


def check_letters(p):
    return re.search('[A-ZА-Я]', p) and re.search('[a-zа-я]', p)


def check_number(p):
    return re.search('[0-9]', p)


def check_klawa(p):
    for i in range(0, len(p) - 2):
        for el in ENG:
            for y in range(len(el) - 2):
                if el[y] + el[y + 1] + el[y + 2] in p.lower():
                    return False
        for el in RUS:
            for y in range(len(el) - 2):
                if el[y] + el[y + 1] + el[y + 2] in p.lower():
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
    # если пароль нарушает требование к последовательности из подряд идущих трех символов
    # (указано в предыдущей задаче).
    pass


class WordError(PasswordError):
    # В пароле должны отсутствовать словарные слова
    pass


def Length(p):
    if len(p) < 9:
        exceptions['LengthError'] = exceptions.get('LengthError', 0) + 1
        raise LengthError()


def Letter(p):
    if not check_letters(p):
        exceptions['LetterError'] = exceptions.get('LetterError', 0) + 1
        raise LetterError()


def Digit(p):
    if not check_number(p):
        exceptions['DigitError'] = exceptions.get('DigitError', 0) + 1
        raise DigitError()


def Sequence(p):
    if not check_klawa(p):
        exceptions['SequenceError'] = exceptions.get('SequenceError', 0) + 1
        raise SequenceError()


def Word_Er(p):
    if p in top_words:
        exceptions['WordError'] = exceptions.get('WordError', 0) + 1
        raise WordError()


def check_password(password):
    for func in (Length, Letter, Digit, Sequence, Word_Er):
        try:
            func(password)
        except PasswordError:
            pass


for passwd in top_passwd:
    check_password(passwd)

for k in sorted(exceptions.keys()):
    print(k, '-', exceptions[k])
