import pymorphy2

morph = pymorphy2.MorphAnalyzer()

# word = input()
# word = morph.parse(word)[0]
word = morph.parse('Живой')[0]
cases = {'masc','nomn', 'plur'}
w = word.inflect(cases).word
print(w)
