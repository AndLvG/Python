# import re

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
        n = "+7" + n[1:]
    return n


if tel_check_7_8(tel) and tel_check_skobki(tel) and tel_check_znak(tel) and len(tel_format(tel)) == 12:
    print(tel_format(tel))
else:
    print('error')
