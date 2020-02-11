import requests


response = requests.get(
    f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Москва, Петровка, 38&format=json")
if response:
    json_response = response.json()
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    toponym_address = \
        toponym["metaDataProperty"]["GeocoderMetaData"]['Address']['Components'][1]['name']
    toponym_name = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_olast = toponym['metaDataProperty']['GeocoderMetaData'][
        'AddressDetails']['Country']['AdministrativeArea']['AdministrativeAreaName']
    toponym_index = toponym['metaDataProperty']['GeocoderMetaData']['Address']['postal_code']
    print(toponym_name + ", Почтовый индекс: ", toponym_index)
else:
# Произошла ошибка выполнения запроса. Обрабатываем http-статус.
    print("Ошибка выполнения запроса:")
    print("Http статус:", response.status_code, "(", response.reason, ")")
