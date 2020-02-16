import requests
import distance
import math

point = input(
    "Введите ваш адрес (например: 'Обнинск, ул.Королева, д.1 (~100 км до башни)' или 'Россия, Калуга, ул.Тарутинская, д.192'): ")

ostank_bashnya_coord = '37.611706,55.819845'

response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={point}&format=json")
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_coodrinates = ','.join(toponym_coodrinates.split())
else:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")

# Расстояние в км от Останкинской башни до точки
l = int(distance.lonlat_distance(map(float, ostank_bashnya_coord.split(',')),
                                    map(float, toponym_coodrinates.split(',')))) / 1000
print(f'Расстояние от вас до Останкинской башни l = {l} километров')
print(f'Формула для расчёта высоты приемной антенны: h2 = ((l/3.6 - sqrt(525)) ** 2')
h1 = 525
h2 = int((l / 3.6 - math.sqrt(h1)) ** 2)

print(f'Для получения сигнала Вам нужно поднять антенну на {h2} метров')
