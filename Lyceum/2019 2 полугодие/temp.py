def test(a, b):
    return len(a) == len(b) and all(t in b for t in a)


n = int(input())
words = []
for _ in range(n):
    words.append(input().lower())
# words = sorted(words)

words = set(words)
words = sorted(list(words), reverse=True)

while len(words) > 0:
    w = [words.pop()]
    k = 0
    while k < len(words):
        word2 = words[k]
        if test(w[0], word2):
            w.append(word2)
            words.remove(word2)
        else:
            k += 1
    if len(w) > 1:
        print(*w)
