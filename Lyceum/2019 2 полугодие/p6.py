def print_long_words(t):
    sss = []
    word = ""
    flag = False
    for a in t:
        if a.isalpha():
            flag = True
            word += a
        else:
            if flag:
                sss.append(word)
                word = ""
    sss.append(word)

    for el in sss:
        c = 0
        for let in el:
            if let in "уУаАоОеЕёЁыЫэЭяЯиИюЮeEyYuUiIoOa":
                c += 1
        if c >= 4:
            print(el)


print_long_words('"""whatever.wherever1solution;solut1onal"""')
