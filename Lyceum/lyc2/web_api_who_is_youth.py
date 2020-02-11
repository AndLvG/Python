import requests

ug = ""
ug_cord = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999
cityes = input().split(", ")
for city in cityes:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={city}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        toponym_coodrinates = toponym["Point"]["pos"]
        toponym_coodrinates = toponym_coodrinates.split(" ")
        if float(toponym_coodrinates[1]) < ug_cord:
            ug = city
            ug_cord = float(toponym_coodrinates[1])
print(ug)