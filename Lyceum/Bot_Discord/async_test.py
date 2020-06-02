import requests


def ya_translate(mytext, lang='ru-en'):
    URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    KEY = "trnsl.1.1.20200511T163423Z.b33f24575bcce593.ca5642bae3777446ce37b47eca18526f907b808b"
    params = {
        "key": KEY,
        "text": mytext,
        "lang": lang   # Здесь мы указываем с какого языка на какой мы делаем переводим
    }
    response_json = requests.get(URL, params=params).json()
    return ''.join(response_json["text"])


print(ya_translate("Привет Дима. Как дела?"))
print(ya_translate("Hi Dima. How's it going?", "en-ru"))

# pip install discord.py