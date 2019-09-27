import pymorphy2
from sys import stdin

morph = pymorphy2.MorphAnalyzer()

for el in stdin:
    word = el.replace("\n", "")

    parse_word = morph.parse(word)[0]

    if parse_word.tag.POS in {'NOUN'}:

        cases = {parse_word.tag.number, parse_word.tag.gender}

        # Во множественном числе род имен прилагательных не выражен
        if parse_word.tag.number == 'plur':
            cases.discard(parse_word.tag.gender)  # поэтому род удаляем

        # согласуем прилагательное со словом по числу и роду
        anim = morph.parse('Живая')[0].inflect(cases)

        if parse_word.tag.animacy == 'anim':
            print(anim.word.title())
        else:
            print('Не', anim.word)

    else:
        print('Не существительное')
