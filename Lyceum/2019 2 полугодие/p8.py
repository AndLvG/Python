def letter_to_num(f):
    a = f[:1]
    b = f[1:]
    r = int(b)
    c = 'ABCDEFGH'.find(a) + 1
    return (c, r)


def num_to_letter(k):
    (c, r) = k
    return 'ABCDEFGH'[c - 1] + str(r)


def possible_turns(f):
    (c, r) = letter_to_num(f)
    tmp = []
    tmp.append((c + 2, r + 1))
    tmp.append((c + 2, r - 1))
    tmp.append((c - 2, r + 1))
    tmp.append((c - 2, r - 1))
    tmp.append((c + 1, r + 2))
    tmp.append((c - 1, r + 2))
    tmp.append((c + 1, r - 2))
    tmp.append((c - 1, r - 2))
    koor = []
    for ((a, b)) in tmp:
        if (a > 0) & (b > 0) & (a <= 8) & (b <= 8):
            koor += [num_to_letter((a, b))]
    return sorted(koor)


print(str(possible_turns("B1")))
