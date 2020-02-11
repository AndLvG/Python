import requests

cities = ["Хабаровск",
          "Уфа",
          "Нижний Новгород",
          "Калининград"]

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
        print(toponym_name + ",", toponym_address)