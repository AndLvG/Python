import requests

cities = ["Калуга", "Обнинск", "Тула", "Барнаул", "Мелеуз", "Йошкар-Ола"]

for citi in cities:
    response = requests.get(
        f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={citi}&format=json")
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = \
            toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][1]['name']
        toponym_name = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_olast = toponym['metaDataProperty']['GeocoderMetaData'][
            'AddressDetails']['Country']['AdministrativeArea']['AdministrativeAreaName']
        
        print(toponym_name + ",", toponym_olast)
    else:
    # Произошла ошибка выполнения запроса. Обрабатываем http-статус.
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
