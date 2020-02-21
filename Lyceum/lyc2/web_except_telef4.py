from itertools import chain

OPERATOR = chain(range(910, 919), range(980, 989), range(920, 939), range(902, 906), range(960, 969))

tel = input().replace(" ", "").replace("\t", "")


def tel_check_7_8(n):
    return n[:2] == "+7" or n[0] == "8"


def tel_check_skobki(n):
    i = 0
    s = 0
    for el in n:
        if el == "(":
            i += 1
        elif el == ")":
            i -= 1
            if i == 0:
                s += 1
        if i < 0 or s > 1:
            break
    return i == 0 and s in (0, 1)


def tel_check_znak(n):
    return "--" not in n and n[0] != "-" and n[-1] != "-"


def tel_format(n):
    # n = re.sub("\D", "", n)
    n = ''.join(i for i in n if i.isdigit())
    if n[0] == "8":
        n = "7" + n[1:]
    return "+" + n


def err_tel_check_7_8(n):
    if n[:2] != "+7" and n[0] != "8":
        raise NameError


def err_tel_check_skobki(n):
    i = 0
    s = 0
    for el in n:
        if el == "(":
            i += 1
        elif el == ")":
            i -= 1
            if i == 0:
                s += 1
        if i < 0 or s > 1:
            break
    if i != 0 or s not in (0, 1):
        raise NameError


def err_tel_check_znak(n):
    if "--" in n or n[0] == "-" or n[-1] == "-":
        raise NameError


def err_tel_len(n):
    if len(tel_format(tel)) != 12:
        raise IndexError


def err_tel_operator(n):
    tel = n[2:5]
    if tel not in OPERATOR:
        raise IndentationError


def check_telef(telef):
    for func in (err_tel_check_7_8, err_tel_check_skobki, err_tel_check_znak, err_tel_len, err_tel_operator):
        try:
            func(telef)
        except NameError:
            return 'неверный формат'
        except IndexError:
            return 'неверное количество цифр'
        except IndentationError:
            return 'не определяется оператор сотовой связи'
    return tel_format(tel)


print(check_telef(tel))
