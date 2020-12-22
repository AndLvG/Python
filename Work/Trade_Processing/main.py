from CHP_api import CHP_api
import pandas as pd
import processing
import datetime

# ITI Invest
localhost = '85.143.79.6:5000'
login = 'YKYVZLDP'
password = '1YWKTX'
key = '12345'

# Shortcut
Shortcut1 = "SBER"
Shortcut2 = "GAZP"

# TradeDates
TradeDate = '2020-09-18'
TradeDate_Frame = 100

DataTimeFrame = 9  # 9 - Days / 6 - Hours / 5 - 30min / 4 - 15min / 3 - 10min / 2 - 5min / 1 - 1min


def ITI_Invest(localhost, login, password, key, Shortcut, TradeDate, TD_Frame, TimeFrame):
    api = CHP_api(localhost)
    api.login(login, password, key)
    resp = api.get_portfolio_list()
    bars = api.get_bars(Shortcut, TimeFrame, TradeDate, TD_Frame)
    bars = pd.DataFrame(bars)
    return bars.sort_values(by='datetime').reset_index(drop=True)


# Test missing Days
df_day = ITI_Invest(localhost, login, password, key, Shortcut1, TradeDate, TradeDate_Frame, DataTimeFrame)
print(df_day.to_markdown())
df_day = df_day.drop(df_day[df_day.datetime == '2020-09-19T23:59:59'].index)

dates_list, ready_df = processing.find_missing_dates("Day", df_day)
print(dates_list)
if ready_df is not None:
    print(ready_df.to_markdown())


# Test missing Houres
# df_hour = ITI_Invest(localhost, login, password, key, Shortcut1, TradeDate, TradeDate_Frame, 6)
# df_hour = df_hour.drop(df_hour[df_hour.datetime == '2020-09-20T12:00:00'].index)
# # print(df_hour.to_markdown())
#
# dates_list, ready_df = processing.find_missing_dates("H", df_hour)
# print(dates_list)
# print(ready_df.to_markdown())

# Test missing 30min
# df_30min = ITI_Invest(localhost, login, password, key, Shortcut1, TradeDate, TradeDate_Frame, 5)
# df_30min = df_30min.drop(df_30min[df_30min.datetime == '2020-09-20T12:00:00'].index)
# # print(df_30min.to_markdown())
#
# dates_list, ready_df = processing.find_missing_dates( "30min", df_30min)
# print(dates_list)
# print(ready_df.to_markdown())

# Test missing 15min
# df_15min = ITI_Invest(localhost, login, password, key, Shortcut1, TradeDate, TradeDate_Frame, 4)
# df_15min = df_15min.drop(df_15min[df_15min.datetime == '2020-09-20T18:00:00'].index)
# # print(df_15min.to_markdown())
# 
# dates_list, ready_df = processing.find_missing_dates("15min", df_15min)
# print(dates_list)
# print(ready_df.to_markdown())

# Test missing 5min
# df_5min = ITI_Invest(localhost, login, password, key, Shortcut1, TradeDate, TradeDate_Frame, 2)
# df_5min = df_5min.drop(df_5min[df_5min.datetime == '2020-09-20T18:00:00'].index)
# # print(df_5min.to_markdown())
#
# dates_list, ready_df = processing.find_missing_dates("5min", df_5min)
# print(dates_list)
# print(ready_df.to_markdown())

# Test missing 1min
print(f'start download {datetime.datetime.now()}')
df_1min = ITI_Invest(localhost, login, password, key, Shortcut1, TradeDate, TradeDate_Frame, 1)
# df_1min = df_1min.drop(df_1min[df_1min.datetime == '2020-09-20T18:00:00'].index)
print(f'ready download {datetime.datetime.now()}')
# print(df_1min.to_markdown())

dates_list, ready_df = processing.find_missing_dates("1min", df_1min)
print(dates_list)
if ready_df is not None:
    print(ready_df.to_markdown())

print(f'ready processing {datetime.datetime.now()}')

# pip install git+https://github.com/talestorm-com/CHP_api.git
# pip install pandas
# pip install tabulate

# Вопросы
# в выборках нет вечерней сессии 19:05:00 – 23:49:59 Это вызывает условие пропущенных тиков
# Так же есть период 19:00 которого нет в рабочем диапазоне 10:00:00 - 18:50:00
# т.е. обратная ситуация когда есть данные которых нет в эталонном каледаре

# Переделал поиск первого не пустого значения по индексу в эталонном календаре
# Вынес как просили функцию заполнения датафрема в отдельную
# Протестировал по выпадающим значениям по всем ключам
# Так же сделал поиск первого реального значения пузырьком так как могут попасться несколько подряд пропущенных
# Предложение - не учитывать параметры по диапазону дат на вход а брать начальную и конечную дату датасета

# Нужны реальные данные с выпадающими ключами. Пока не могу протестировать по ним так как нет правильных диапазонов работы биржи.
# Функция доливает значения по эталонному каледарю которые шире рабочих часов

# Для тестирования можно взять реальные данные на утро 2020-09-17
# Первые полчаса был сбой у брокера с 10 до 10-30
# Алгоритм восстанавливает потерянные данные по всем ключам выборки