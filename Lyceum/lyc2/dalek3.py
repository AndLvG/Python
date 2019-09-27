from sys import stdin
import string

list = ['далеки', 'далека', 'далеков', 'далеку', 'далекам', 'далека', 'далеков ',
        'далеком', 'далеками', 'далеке', 'далеках', 'далек']

words = []
k = 0
for el in stdin:
    words = el.split()
    flag = 0
    for w in words:
        if w.rstrip(string.punctuation).lower() in list and flag == 0:
            k += 1
            flag = 1

print(k)
