import sys
import requests

toponym_to_find = sys.argv[-1]  #'Калуга, пл.Победы, 2'  
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "kind": "district",
    "format": "json",
    "geocode": ",".join([toponym_longitude, toponym_lattitude])
}

response = requests.get(geocoder_api_server, params=geocoder_params)
json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]["metaDataProperty"]["GeocoderMetaData"]["Address"]["Components"]
district = list(filter(lambda x: x['kind'] == 'district', toponym))[0]
print(f'Название района - {district["name"]}')

# python web6_api_poisk2.py "Калуга, пл.Победы, 2"