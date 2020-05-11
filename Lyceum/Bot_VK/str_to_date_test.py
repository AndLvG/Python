import datetime as DT
from dateutil import parser
import locale
locale.setlocale(locale.LC_ALL, "ru")

text = "20180819"

date = DT.datetime.strptime(text, '%Y%m%d').date()
print(date)

s = '2017-06-08'
try:
    dt = parser.parse(s)
    print(dt.date())
    print(dt.strftime("%A"))
except:
    print('Не удалось выделить дату')
