import pandas as pd


# Function removes holidays and not working trade houres from etalon calendar
def only_work_period(etalon_calendar):
    """     :param etalon_calendar: Эталонный календарь типа DateTimeIndex
                    """
    # Take only working houres and bussines days
    etalon_calendar = etalon_calendar[etalon_calendar.dayofweek < 5]

    etalon_calendar = etalon_calendar[etalon_calendar.indexer_between_time('10:00:00', '18:45:00')]

    # Если раскоментировать то будет добавлена вечерняя сессия
    # etalon_calendar = etalon_calendar.append(
    #     etalon_calendar[etalon_calendar.indexer_between_time('19:05:00', '23:49:59')])

    # print(etalon_calendar)
    return etalon_calendar


# Function will compare etalon calendar with missing dates and fill entry data
def fill_empty_dates(etalon_calendar, data):
    """     :param etalon_calendar: Эталонный календарь типа DateTimeIndex ограниченный по рабочим дням и часам
            :param data: Исходный DataFrame в котором возможно пропущены записи по времени
                        """
    # Make index by datetime
    s = pd.Series(data.groupby(['datetime']).size())
    s.index = pd.DatetimeIndex(s.index)

    # Compare entry data with etalon calendar with filling 0 for missing values
    compared_calendar = s.reindex(etalon_calendar, fill_value=0)

    # Will take only missing values to return
    missing_dates = compared_calendar[compared_calendar == 0]

    for m_date in missing_dates.index:

        # Find first occurrence of not missing date
        i = 1
        prev_value = compared_calendar.iloc[compared_calendar.index.get_loc(m_date) - 1]
        while prev_value == 0:
            i += 1
            prev_value = compared_calendar.iloc[compared_calendar.index.get_loc(m_date) - i]

        previous_date = compared_calendar.index[compared_calendar.index.get_loc(m_date) - i]
        row = data.loc[data['datetime'] == previous_date].copy()

        # Replace date in datetime column with missing date
        row['datetime'] = m_date
        # Add row with missing date to entry DataFrame
        data = data.append(row)

    # !!! ОБРАТИТЬ ВНИМАНИЕ !!!
    # Согласно требованиям ТЗ возвращаться должно не более 20000 записей после восстановления алгоритмом
    # head(20000)
    # Если требования изменятся то удалить/исправить эту строку

    return missing_dates, data.sort_values(by='datetime').reset_index(drop=True).head(20000)


def find_missing_dates(Key, data):
    """
            Prepare dates to pass filling empty ticks

            Parameters
            ----------
            key: str
                Ключ поиска Day / H  (Houres) / 30min / 15min / 10min / 5min / 1min
            data: DataFrame
                DataFrame с выборкой

            Raise Error
            ----------
                Key not in ('Day', 'H',  '30min', '15min', '10min', '5min', '1min')
            """
    # Check valid Key
    if Key not in ('Day', 'H', '30min', '15min', '10min', '5min', '1min'):
        raise ValueError("Key not in ('Day', 'H' (Houres),  '30min', '15min', '10min', '5min', '1min')")

    # Get relevant dates according DataFrame
    # start_date = max(TradeDate_Start, data['datetime'].min())
    # end_date = min(TradeDate_End, data['datetime'].max())

    # Convert data in datetime field to explicit Date type so it will be able to compare with etalon_calendar
    data['datetime'] = pd.to_datetime(data['datetime'])

    # !!! ОБРАТИТЬ ВНИМАНИЕ !!!
    # Временно удаляем вечернюю сессию если вдруг появится!!!
    # Только если ключ выборки не Day
    if Key != "Day":
        mask = (data['datetime'].dt.strftime('%H:%M') >= '10:00') & (data['datetime'].dt.strftime('%H:%M') <= '18:45')
        data = data.loc[mask]

    # Если в результате данных не осталось возвращаем Null
    if data.count == 0:
        return None, None

    start_date = data['datetime'].min()
    end_date = data['datetime'].max()

    if Key == "Day":
        # Create etalon calendar only from bussines days between start and end dates
        etalon_calendar = pd.date_range(start_date, end_date, freq="D")
        etalon_calendar = etalon_calendar[etalon_calendar.dayofweek < 5]
        # print(etalon_calendar)

    else:
        etalon_calendar = pd.date_range(start_date, end_date, freq=Key)
        # Take only working houres and bussines days
        etalon_calendar = only_work_period(etalon_calendar)

    return fill_empty_dates(etalon_calendar, data)
