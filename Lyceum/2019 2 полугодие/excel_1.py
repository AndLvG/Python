import xlsxwriter


def export_check(text):
    text = text.split('\n---\n')
    workbook = xlsxwriter.Workbook('res.xlsx')
    for el in text:
        c = 0
        text1 = el.split('\n')
        text2 = []
        for el2 in text1:
            el2 = el2.split("\t")
            flag = True
            for el3 in text2:
                if el3[0] == el2[0] and el3[1] == el2[1]:
                    flag = False
                    break
            if flag:
                text2.append(el2)
            else:
                text2[text2.index(el3)][2] = str(int(text2[text2.index(el3)][2]) + int(el2[2]))
                c += 1
        worksheet = workbook.add_worksheet()
        # Данные
        for i in range(len(text1) - c):
            worksheet.write(i, 0, text2[i][0])
            worksheet.write(i, 1, int(text2[i][1]))
            worksheet.write(i, 2, int(text2[i][2]))
            worksheet.write(i, 3, '=B' + str(i + 1) + '*C' + str(i + 1))
            worksheet.write(len(text1) - c, 0, 'Итого')
            worksheet.write(len(text1) - c, 3, '=SUM(D1:D' + str(len(text1) - c) + ')')
    workbook.close()

# t = 'Картошка 1	50	3\nКартошка 1	50	2\nСок 2	80	3---Картошка	50	3\nКартошка	50	5\nСок	80	3'
t = 'товар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\nтовар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\n---\nтовар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\nтовар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500\nтовар 1\t100\t5\nтовар 2\t200\t6\nтовар 3\t7\t500'

export_check(t)
