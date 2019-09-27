from sys import stdin

word = input()
words = []
for el in stdin:
    words.append(el.replace('\n', ''))

filt = list(filter(lambda x: all(l in word for l in x), words))
print(words)
print(filt)

Result = []
for el in filt:
    temp_word = word
    flag = 0
    for let in el:
        ind = temp_word.find(let)
        if ind == -1:
            flag = 1
            break
        else:
            temp_word = temp_word.replace(let, '', 1)
    if flag == 0:
        Result.append(el)

print(len(Result))
print(*Result, sep='\n')

