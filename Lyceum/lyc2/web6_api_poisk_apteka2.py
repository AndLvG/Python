import sys
from io import BytesIO

import requests
from PIL import Image

toponym_to_find = " ".join(sys.argv[1:])  # 'г.Калуга, пл.Победы, 2'
delta = '0.03'  

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

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
address_ll = ",".join([toponym_longitude, toponym_lattitude])
search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz"
}

response = requests.get(search_api_server, params=search_params)
json_response = response.json()

organizations = json_response["features"][:10]
pt = ""
for org in organizations:
    point = org["geometry"]["coordinates"]
    org_point = "{0},{1}".format(point[0], point[1])
    # print(org['properties']['CompanyMetaData']['Hours']) 
    if 'text' in org['properties']['CompanyMetaData']['Hours']:
        if  org['properties']['CompanyMetaData']['Hours']['text'] == 'ежедневно, круглосуточно':
            pt += f'{org_point},pm2dgm~'
        else:
            pt += f'{org_point},pm2blm~'
    else:
        pt += f'{org_point},pm2grm~'
pt = pt[:-1]

map_params = {
    "ll": address_ll,
    "spn": ",".join([delta, delta]),
    "l": "map",
    "pt": pt
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

print(response.url)
Image.open(BytesIO(
    response.content)).show()

# python web6_api_poisk_apteka2.py Калуга, пл.Победы, 2