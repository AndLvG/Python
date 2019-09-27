n = int(input())
words = [[input().lower(), 1] for _ in range(n)]

for i in range(len(words)):
    if words[i][1] != 0:
        w = [words[i][0]]
        words[i][1] = 0
        for k in range(len(words)):
            if words[k][1] != 0:
                if sorted(words[i][0]) == sorted(words[k][0]) and words[i][0] != words[k][0]:
                    w.append(words[k][0])
                    words[k][1] = 0
        if len(w) > 1:
            print(*w)

