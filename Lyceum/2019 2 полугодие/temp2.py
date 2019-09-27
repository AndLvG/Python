n = int(input())
words = [input().lower() for _ in range(n)]
words.sort()

new_words = {}

for i in range(len(words)):
    w = ''.join(sorted(words[i]))
    if w in new_words.keys():
        if words[i] not in new_words.get(w, []):
            new_words[w].append(words[i])
    else:
        new_words[w] = [words[i]]

for v in new_words.values():
    if len(v) > 1:
        print(*v)
