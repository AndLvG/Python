import xlrd
import csv

wb = xlrd.open_workbook("data.xlsx")
sh = wb.sheet_by_index(0)
with open("output.csv", "w") as fh:
    writer = csv.writer(fh, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row_number in range(sh.nrows):
        writer.writerow(sh.row_values(row_number))
