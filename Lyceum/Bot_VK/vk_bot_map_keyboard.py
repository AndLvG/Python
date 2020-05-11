import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api import VkUpload
import sys
from io import BytesIO
import requests


TOKEN = 'aeea642e6d43e6a3ff5e068a1e455a7746f928aec2a3a771c4566a841eac45e620fed710abe7a14971ac6'


empty_kl = {"buttons": [], "one_time": True}


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, 195095163)
    upload = VkUpload(vk_session)
    vk = vk_session.get_api()

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            vk.messages.send(
                user_id=event.obj.message['from_id'],
                random_id=get_random_id(),
                message="Введи название местности которую хочешь увидеть. Например Калуга"
            )

            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    toponim = event.obj.message['text']

                    keyboard = VkKeyboard(one_time=True)

                    keyboard.add_button(
                        'map (схема)', color=VkKeyboardColor.DEFAULT)
                    keyboard.add_button(
                        'sat (спутник)', color=VkKeyboardColor.POSITIVE)
                    keyboard.add_button(
                        'skl (гибрид)', color=VkKeyboardColor.NEGATIVE)
                    keyboard.add_line()
                    keyboard.add_location_button()

                    vk.messages.send(user_id=event.obj.message['from_id'],
                                     message="Выберите тип карты на клавиатуре",
                                     keyboard=keyboard.get_keyboard(),
                                     random_id=get_random_id())

                    for event in longpoll.listen():
                        if event.type == VkBotEventType.MESSAGE_NEW:
                            map_type = {
                                'map (схема)': 'map', 'sat (спутник)': 'sat', 'skl (гибрид)': 'skl'}
                            im = get_image(
                                toponim, map_type[event.obj.message['text']])

                            photo = upload.photo_messages(photos=im)[0]

                            attachments = 'photo{}_{}'.format(
                                photo['owner_id'], photo['id'])

                            vk.messages.send(
                                user_id=event.obj.message['from_id'],
                                attachment=attachments,
                                random_id=get_random_id(),
                                message=f"Это {toponim}. Что вы еще хотите увидеть?"
                            )
                            break
                    

        else:
            print(event.type)


def get_image(toponym_to_find, map_type):
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
    delta = "0.005"
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta, delta]),
        "l": map_type
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    return BytesIO(response.content)


if __name__ == '__main__':
    main()
