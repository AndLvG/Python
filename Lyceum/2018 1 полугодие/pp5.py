s = []
for i in range(30001):
    s.append(0)
pos = 0
for j in input():
    if j == ">":
        pos = pos + 1
    elif j == "<":
        pos = pos - 1
    elif j == ".":
        print(s[pos])
    elif j == "+":
        s[pos] = s[pos] + 1
    elif j == "-":
        s[pos] = s[pos] - 1


# +.>.+>+>+>+++>+++++<[-].>.

