import requests

point = input(
    "Введите адрес (например: 'Москва, ул.Ленина, д.1' или 'Россия, Санкт-Петербург, Невский проспект, д.2'): ")

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

response = requests.get(
    f"https://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={toponym_coodrinates}&kind=metro&format=json")
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_metro = f'Ближайшее к Вам метро: {toponym["name"]}'
    print(toponym_metro)
else:
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
