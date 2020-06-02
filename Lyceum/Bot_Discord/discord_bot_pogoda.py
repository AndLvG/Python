from discord.ext import commands
import requests
import datetime
from dateutil import parser
import locale

locale.setlocale(locale.LC_ALL, "ru")

TOKEN = "NzA5NzAzNTgwNzIxODcyODk2.XrpyDA.WUjTDTnD8zoxAKabhFQ9wJQHvEg"


def get_coordinates(toponym_to_find):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()
    if json_response["response"]["GeoObjectCollection"]["featureMember"]:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    else:
        return None
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    return toponym_lattitude, toponym_longitude


def get_pogoda(place):
    APIKEY = "3151d868-62ec-4452-9374-c10e411dd8d0"
    weather_api_server = "https://api.weather.yandex.ru/v1/forecast"
    lat, lon = get_coordinates(place)
    params = {
        "lat": lat,
        "lon": lon,
        "extra": "true"}

    response = requests.get(weather_api_server, params=params, headers={"X-Yandex-API-Key": APIKEY})
    return response.json()


class WeatherBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.place = ""

    @commands.command(name='help_bot')
    async def help(self, ctx):
        message = 'Команды:\n' \
                  '"#!place" задает место прогноза. Например <#!place Калуга>\n' \
                  '"#!current" текущая погода. Например <#!current>\n' \
                  '"#!forecast {days}" прогноз дневной температуры и осадков на указанное количество дней \n' \
                  '       Например <#!forecast 3>'
        await ctx.send(message)

    @commands.command(name='place')
    async def numerals(self, ctx, place):
        self.place = place
        await ctx.send(f'Место прогноза установлено на {place}')

    @commands.command(name='current')
    async def alive(self, ctx):
        if self.place == "":
            await ctx.send('Сначала установите город командой "#!place"')
            return

        resp = get_pogoda(self.place)
        dt = parser.parse(resp["now_dt"])
        print(dt.date())
        mes = f"Текущая погода в {self.place} сегодня {dt.date()} на {dt.time()}\n"
        mes += f"Температура {resp['fact']['temp']}\nДавление {resp['fact']['pressure_mm']} мм\n"
        mes += f"Влажность {resp['fact']['humidity']}%\n"
        mes += f"Ветер направление {resp['fact']['wind_dir']} сила {resp['fact']['wind_speed']}м/с"

        await ctx.send(mes)

    @commands.command(name='forecast')
    async def noun(self, ctx, days):
        if self.place == "":
            await ctx.send('Сначала установите город командой "#!place"')
            return

        prognoz_date = (datetime.date.today() + datetime.timedelta(days=int(days))).strftime("%Y-%m-%d")
        print(prognoz_date)
        resp = get_pogoda(self.place)
        prog_resp = list(filter(lambda x: x['date'] == prognoz_date, resp['forecasts']))
        print(prog_resp)
        prognoz = prog_resp[0]['parts']['day']
        print(prognoz)
        mes = f"Прогноз погоды в {self.place} на {prognoz_date}\n"
        mes += f"Температура от {prognoz['temp_min']} до {prognoz['temp_max']} днём\n"
        mes += f"Давление {prognoz['pressure_mm']} мм\n"
        mes += f"Влажность {prognoz['humidity']}%\n"
        mes += f"Ветер направление {prognoz['wind_dir']} сила {prognoz['wind_speed']}м/с"

        await ctx.send(mes)


bot = commands.Bot(command_prefix='#!')
bot.add_cog(WeatherBot(bot))
bot.run(TOKEN)

# pip install yandex-weather-api


t = {'date': '2020-05-12', 'date_ts': 1589230800, 'week': 20, 'sunrise': '04:34', 'sunset': '20:29',
     'rise_begin': '03:48', 'set_end': '21:15', 'moon_code': 3, 'moon_text': 'decreasing-moon', 'parts': {
        'night': {'_source': '0,1,2,3,4,5', 'temp_min': 12, 'temp_max': 13, 'temp_avg': 13, 'feels_like': 9,
                  'icon': 'skc_n', 'condition': 'clear', 'daytime': 'n', 'polar': False, 'wind_speed': 3.6,
                  'wind_gust': 8.7, 'wind_dir': 's', 'pressure_mm': 735, 'pressure_pa': 980, 'humidity': 60,
                  'uv_index': 0, 'soil_temp': 12, 'soil_moisture': 0.3, 'prec_mm': 0, 'prec_period': 360,
                  'prec_prob': 0},
        'morning': {'_source': '6,7,8,9,10,11', 'temp_min': 13, 'temp_max': 20, 'temp_avg': 17, 'feels_like': 13,
                    'icon': 'bkn_d', 'condition': 'cloudy', 'daytime': 'd', 'polar': False, 'wind_speed': 5.6,
                    'wind_gust': 13.3, 'wind_dir': 's', 'pressure_mm': 733, 'pressure_pa': 978, 'humidity': 54,
                    'uv_index': 4, 'soil_temp': 13, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 360,
                    'prec_prob': 0},
        'day': {'_source': '12,13,14,15,16,17', 'temp_min': 16, 'temp_max': 21, 'temp_avg': 19, 'feels_like': 15,
                'icon': 'ovc_ra', 'condition': 'cloudy-and-rain', 'daytime': 'd', 'polar': False, 'wind_speed': 6.3,
                'wind_gust': 14.7, 'wind_dir': 's', 'pressure_mm': 731, 'pressure_pa': 975, 'humidity': 60,
                'uv_index': 2, 'soil_temp': 17, 'soil_moisture': 0.28, 'prec_mm': 3.7, 'prec_period': 360,
                'prec_prob': 80},
        'evening': {'_source': '18,19,20,21,22,23', 'temp_min': 9, 'temp_max': 15, 'temp_avg': 12, 'feels_like': 8,
                    'icon': 'ovc_-ra', 'condition': 'overcast-and-light-rain', 'daytime': 'd', 'polar': False,
                    'wind_speed': 5.5, 'wind_gust': 12.5, 'wind_dir': 's', 'pressure_mm': 729, 'pressure_pa': 972,
                    'humidity': 86, 'uv_index': 0, 'soil_temp': 15, 'soil_moisture': 0.29, 'prec_mm': 0.4,
                    'prec_period': 360, 'prec_prob': 80},
        'day_short': {'_source': '8,9,10,11,12,13,14,15,16,17,18,19,20', 'temp': 21, 'temp_min': 14,
                      'feels_like': 18, 'icon': 'ovc_ra', 'condition': 'cloudy-and-rain', 'wind_speed': 6.3,
                      'wind_gust': 14.7, 'wind_dir': 's', 'pressure_mm': 731, 'pressure_pa': 975, 'humidity': 63,
                      'uv_index': 2, 'soil_temp': 15, 'soil_moisture': 0.29, 'prec_mm': 3.8, 'prec_prob': 80},
        'night_short': {'temp': 12, 'feels_like': 8, 'icon': 'skc_n', 'condition': 'clear', 'wind_speed': 3.6,
                        'wind_gust': 8.7, 'wind_dir': 's', 'pressure_mm': 735, 'pressure_pa': 980, 'humidity': 60,
                        'uv_index': 0, 'soil_temp': 12, 'soil_moisture': 0.3, 'prec_mm': 0, 'prec_prob': 0}},
     'hours': [
         {'hour': '0', 'hour_ts': 1589230800, 'temp': 13, 'feels_like': 10, 'icon': 'skc_n', 'condition': 'clear',
          'wind_speed': 2.7, 'wind_gust': 7.4, 'wind_dir': 's', 'pressure_mm': 736, 'pressure_pa': 982,
          'humidity': 57, 'uv_index': 0, 'soil_temp': 12, 'soil_moisture': 0.3, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '1', 'hour_ts': 1589234400, 'temp': 13, 'feels_like': 10, 'icon': 'skc_n', 'condition': 'clear',
          'wind_speed': 3.1, 'wind_gust': 7.4, 'wind_dir': 's', 'pressure_mm': 736, 'pressure_pa': 982,
          'humidity': 60, 'uv_index': 0, 'soil_temp': 12, 'soil_moisture': 0.3, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '2', 'hour_ts': 1589238000, 'temp': 12, 'feels_like': 9, 'icon': 'skc_n', 'condition': 'clear',
          'wind_speed': 3, 'wind_gust': 7.4, 'wind_dir': 's', 'pressure_mm': 736, 'pressure_pa': 982,
          'humidity': 61, 'uv_index': 0, 'soil_temp': 12, 'soil_moisture': 0.3, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '3', 'hour_ts': 1589241600, 'temp': 13, 'feels_like': 10, 'icon': 'skc_n', 'condition': 'clear',
          'wind_speed': 3.1, 'wind_gust': 8.7, 'wind_dir': 's', 'pressure_mm': 735, 'pressure_pa': 980,
          'humidity': 60, 'uv_index': 0, 'soil_temp': 11, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '4', 'hour_ts': 1589245200, 'temp': 12, 'feels_like': 8, 'icon': 'skc_n', 'condition': 'clear',
          'wind_speed': 3.6, 'wind_gust': 8.7, 'wind_dir': 's', 'pressure_mm': 734, 'pressure_pa': 979,
          'humidity': 62, 'uv_index': 0, 'soil_temp': 11, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '5', 'hour_ts': 1589248800, 'temp': 12, 'feels_like': 8, 'icon': 'skc_d', 'condition': 'clear',
          'wind_speed': 3.6, 'wind_gust': 8.7, 'wind_dir': 's', 'pressure_mm': 734, 'pressure_pa': 979,
          'humidity': 62, 'uv_index': 0, 'soil_temp': 11, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '6', 'hour_ts': 1589252400, 'temp': 13, 'feels_like': 9, 'icon': 'skc_d', 'condition': 'clear',
          'wind_speed': 3.9, 'wind_gust': 10.3, 'wind_dir': 's', 'pressure_mm': 734, 'pressure_pa': 979,
          'humidity': 59, 'uv_index': 0, 'soil_temp': 11, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '7', 'hour_ts': 1589256000, 'temp': 15, 'feels_like': 11, 'icon': 'skc_d', 'condition': 'clear',
          'wind_speed': 4.7, 'wind_gust': 10.3, 'wind_dir': 's', 'pressure_mm': 734, 'pressure_pa': 979,
          'humidity': 58, 'uv_index': 1, 'soil_temp': 11, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '8', 'hour_ts': 1589259600, 'temp': 17, 'feels_like': 13, 'icon': 'skc_d', 'condition': 'clear',
          'wind_speed': 4.8, 'wind_gust': 10.3, 'wind_dir': 's', 'pressure_mm': 733, 'pressure_pa': 978,
          'humidity': 55, 'uv_index': 1, 'soil_temp': 11, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '9', 'hour_ts': 1589263200, 'temp': 18, 'feels_like': 14, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 5.6, 'wind_gust': 13.3, 'wind_dir': 's', 'pressure_mm': 732, 'pressure_pa': 976,
          'humidity': 53, 'uv_index': 2, 'soil_temp': 14, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '10', 'hour_ts': 1589266800, 'temp': 19, 'feels_like': 15, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 5.6, 'wind_gust': 12.2, 'wind_dir': 's', 'pressure_mm': 732, 'pressure_pa': 976,
          'humidity': 51, 'uv_index': 3, 'soil_temp': 14, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '11', 'hour_ts': 1589270400, 'temp': 20, 'feels_like': 17, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 5.6, 'wind_gust': 12.2, 'wind_dir': 's', 'pressure_mm': 732, 'pressure_pa': 976,
          'humidity': 50, 'uv_index': 4, 'soil_temp': 14, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '12', 'hour_ts': 1589274000, 'temp': 21, 'feels_like': 18, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 5.8, 'wind_gust': 14.7, 'wind_dir': 's', 'pressure_mm': 731, 'pressure_pa': 975,
          'humidity': 48, 'uv_index': 4, 'soil_temp': 17, 'soil_moisture': 0.28, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '13', 'hour_ts': 1589277600, 'temp': 21, 'feels_like': 17, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 6.3, 'wind_gust': 14.7, 'wind_dir': 's', 'pressure_mm': 731, 'pressure_pa': 975,
          'humidity': 51, 'uv_index': 1, 'soil_temp': 17, 'soil_moisture': 0.28, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0},
         {'hour': '14', 'hour_ts': 1589281200, 'temp': 20, 'feels_like': 16, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 6.2, 'wind_gust': 14.7, 'wind_dir': 's', 'pressure_mm': 731, 'pressure_pa': 975,
          'humidity': 52, 'uv_index': 1, 'soil_temp': 17, 'soil_moisture': 0.28, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0}, {'hour': '15', 'hour_ts': 1589284800, 'temp': 17, 'feels_like': 14, 'icon': 'ovc_ra',
                            'condition': 'cloudy-and-rain', 'wind_speed': 4.9, 'wind_gust': 12.3, 'wind_dir': 's',
                            'pressure_mm': 730, 'pressure_pa': 974, 'humidity': 66, 'uv_index': 1, 'soil_temp': 17,
                            'soil_moisture': 0.28, 'prec_mm': 1.5, 'prec_period': 60, 'prec_prob': 60,
                            '_nowcast': True},
         {'hour': '16', 'hour_ts': 1589288400, 'temp': 17, 'feels_like': 14, 'icon': 'ovc_ra',
          'condition': 'cloudy-and-rain', 'wind_speed': 5.5, 'wind_gust': 12.3, 'wind_dir': 's', 'pressure_mm': 730,
          'pressure_pa': 974, 'humidity': 69, 'uv_index': 1, 'soil_temp': 17, 'soil_moisture': 0.28, 'prec_mm': 1.7,
          'prec_period': 60, 'prec_prob': 80, '_nowcast': True},
         {'hour': '17', 'hour_ts': 1589292000, 'temp': 16, 'feels_like': 12, 'icon': 'ovc_ra',
          'condition': 'cloudy-and-rain', 'wind_speed': 5.4, 'wind_gust': 12.3, 'wind_dir': 's', 'pressure_mm': 730,
          'pressure_pa': 974, 'humidity': 71, 'uv_index': 1, 'soil_temp': 17, 'soil_moisture': 0.28, 'prec_mm': 0.5,
          'prec_period': 60, 'prec_prob': 60, '_nowcast': True},
         {'hour': '18', 'hour_ts': 1589295600, 'temp': 15, 'feels_like': 12, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 5, 'wind_gust': 12.5, 'wind_dir': 's', 'pressure_mm': 729, 'pressure_pa': 972,
          'humidity': 82, 'uv_index': 0, 'soil_temp': 15, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0, '_nowcast': True},
         {'hour': '19', 'hour_ts': 1589299200, 'temp': 15, 'feels_like': 12, 'icon': 'ovc', 'condition': 'overcast',
          'wind_speed': 5.2, 'wind_gust': 12.5, 'wind_dir': 's', 'pressure_mm': 729, 'pressure_pa': 972,
          'humidity': 83, 'uv_index': 0, 'soil_temp': 15, 'soil_moisture': 0.29, 'prec_mm': 0, 'prec_period': 60,
          'prec_prob': 0, '_nowcast': True},
         {'hour': '20', 'hour_ts': 1589302800, 'temp': 14, 'feels_like': 11, 'icon': 'ovc_-ra',
          'condition': 'overcast-and-light-rain', 'wind_speed': 5.1, 'wind_gust': 12.5, 'wind_dir': 's',
          'pressure_mm': 729, 'pressure_pa': 972, 'humidity': 84, 'uv_index': 0, 'soil_temp': 15,
          'soil_moisture': 0.29, 'prec_mm': 0.1, 'prec_period': 60, 'prec_prob': 80},
         {'hour': '21', 'hour_ts': 1589306400, 'temp': 13, 'feels_like': 10, 'icon': 'ovc_-ra',
          'condition': 'overcast-and-light-rain', 'wind_speed': 4.7, 'wind_gust': 11.9, 'wind_dir': 'sw',
          'pressure_mm': 729, 'pressure_pa': 972, 'humidity': 89, 'uv_index': 0, 'soil_temp': 14,
          'soil_moisture': 0.29, 'prec_mm': 0.1, 'prec_period': 60, 'prec_prob': 80},
         {'hour': '22', 'hour_ts': 1589310000, 'temp': 10, 'feels_like': 6, 'icon': 'ovc_-ra',
          'condition': 'overcast-and-light-rain', 'wind_speed': 5.5, 'wind_gust': 11.9, 'wind_dir': 'sw',
          'pressure_mm': 728, 'pressure_pa': 971, 'humidity': 89, 'uv_index': 0, 'soil_temp': 14,
          'soil_moisture': 0.29, 'prec_mm': 0.1, 'prec_period': 60, 'prec_prob': 80},
         {'hour': '23', 'hour_ts': 1589313600, 'temp': 9, 'feels_like': 4, 'icon': 'ovc_-ra',
          'condition': 'overcast-and-light-rain', 'wind_speed': 5.5, 'wind_gust': 11.9, 'wind_dir': 'sw',
          'pressure_mm': 728, 'pressure_pa': 971, 'humidity': 88, 'uv_index': 0, 'soil_temp': 14,
          'soil_moisture': 0.29, 'prec_mm': 0.1, 'prec_period': 60, 'prec_prob': 80}]}
