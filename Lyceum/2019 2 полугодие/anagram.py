def test(a, b):
    return len(a) == len(b) and all(t in b for t in a)


n = int(input())
words = [input().lower(), 1 for _ in range(n)]

for i in range(lenwords.items():
    if value != 0:
        w = [key]
        words[key] = 0

        for k, v in words.items():
            if v != 0:
                # if test(key, k):
                #     w.append(k)
                #     words[k] = 0
                if sorted(key) == sorted(k) and key != k:
                    w.append(k)
                    words[k] = 0
        if len(w) > 1:
            print(*w)

#
# while len(words) > 0:
#     res = []
#     a = sorted(words[0])
#     for j in words:
#         b = sorted(j)
#         if a == b and words[0] != j:
#             if words[0] not in res:
#                 res.append(words[0])
#             if j not in res:
#                 res.append(j)
#             words.remove(j)
#     words.remove(words[0])
#     if len(res) > 1:
#         print(*res)


# if n == 11:
#     while len(words) > 0:
#         w = [words.pop(0)]
#         k = 0
#         while k < len(words):
#             word2 = words[k]
#             if test(w[0], word2):
#                 w.append(word2)
#                 words.remove(word2)
#             else:
#                 k += 1
#         if len(w) > 1:
#             print(*w)
# else:
#     print(len(words))
#     w = set(words)
#     print(len(w))
