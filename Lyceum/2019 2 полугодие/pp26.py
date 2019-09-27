from random import choice
import string


def generate_password(num):
    m = ""
    for el in range(num):
        m += choice(string.ascii_letters + string.digits)
    return m


def main(num, ln):
    a1 = []
    for i in range(num):
        n = generate_password(ln)
        # if n in a1:
        #     flag = True
        #     while flag:
        #         if n in a1:
        #             flag = True
        #         else:
        #             a1.append(n)
        # else:
        a1.append(n)
    return a1

# print("Случайный пароль из 7 символов:", generate_password(7))
# print("10 случайных паролей длиной 15 символов:")
# print(*main(5, 1), sep="\n")
