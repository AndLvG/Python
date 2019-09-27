import pymorphy2

morph = pymorphy2.MorphAnalyzer()

word = input()
# word = morph.parse(word)[0].normal_form
word = morph.parse(word)[0]
# print(word)
pos = word.tag.POS

CASES = {
    ('past', 'Прошедшее время:'): [
        {'masc'}, {'femn'}, {'neut'}, {'plur'}
    ],
    ('pres', 'Настоящее время:'): [
        {'1per', 'sing'},
        {'1per', 'plur'},
        {'2per', 'sing'},
        {'2per', 'plur'},
        {'3per', 'sing'},
        {'3per', 'plur'}
    ]
}

if word.tag.POS in {'INFN', 'VERB'}:
    for key, val in CASES.items():
        print(key[1])
        for cases in val:
            cases.add(key[0])
            w = word.inflect(cases).word
            print(w)

else:
    print('Не глагол')
