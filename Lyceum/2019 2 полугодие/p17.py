def vini_puh(inText):
    print(inText)
    phraze = inText.split()  # делим на фразы
    print(phraze)

# считаем число гласных в каждой фразе
    chislo_glasnih = [sum(x in 'аеиоуыэюя' for x in phr) for phr in phraze]

    print(*chislo_glasnih)

# теперь если преобразовать список во множество set в котором могут быть только уникальные значения
    если все значения одинаковые - т.е. количество гласных в каждой фразе совпадает
    то во множестве останется только ОДНО значение!

    if len(set(chislo_glasnih)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"


print(vini_puh(input().lower()))

#  пара-ра-рам рам-пам-папам па-ра-па-дам
