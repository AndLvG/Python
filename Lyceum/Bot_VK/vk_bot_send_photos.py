import vk_api
import random
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.tools import VkTools
import sys
from io import BytesIO
import requests

api_server = 'https://api.vk.com/method/photos.get'


params = {"owner_id": -195095163, "album_id": 274660470, "photo_sizes": 1,
          "access_token": 'aeea642e6d43e6a3ff5e068a1e455a7746f928aec2a3a771c4566a841eac45e620fed710abe7a14971ac6', "v": 5.125}
response = requests.get(api_server, params=params)
print(response.url)
print(response)

json_response = response.json()

j_test = {
    "response": {
        "count": 2,
        "items": [{
            "id": 457239017,
            "album_id": 274660470,
            "owner_id": -195095163,
            "user_id": 453922371,
            "sizes": [{
                "type": "m",
                "url": "https://sun9-72.u...900/w7iANadLFb8.jpg",
                "width": 130,
                "height": 68
            }, {
                "type": "o",
                "url": "https://sun9-11.u...904/KWa1lPrA8_I.jpg",
                "width": 130,
                "height": 87
            }, {
                "type": "p",
                "url": "https://sun9-56.u...905/kBJRBKygUcc.jpg",
                "width": 200,
                "height": 133
            }, {
                "type": "q",
                "url": "https://sun9-72.u...906/lQZQSzsLiJs.jpg",
                "width": 320,
                "height": 213
            }, {
                "type": "r",
                "url": "https://sun9-36.u...907/NLirwt-jrbM.jpg",
                "width": 510,
                "height": 340
            }, {
                "type": "s",
                "url": "https://sun9-24.u...8ff/fN66BUjDewg.jpg",
                "width": 75,
                "height": 39
            }, {
                "type": "x",
                "url": "https://sun9-62.u...901/UzFC_2AYJAU.jpg",
                "width": 604,
                "height": 316
            }, {
                "type": "y",
                "url": "https://sun9-37.u...902/sgDum_F1Oa8.jpg",
                "width": 807,
                "height": 422
            }, {
                "type": "z",
                "url": "https://sun9-18.u...903/U_t0Dr1Q5j8.jpg",
                "width": 1200,
                "height": 627
            }],
            "text": "",
            "date": 1588872399,
            "has_tags": False
        }, {
            "id": 457239018,
            "album_id": 274660470,
            "owner_id": -195095163,
            "user_id": 453922371,
            "sizes": [{
                "type": "m",
                "url": "https://sun9-43.u...909/OWY1qVLn0QY.jpg",
                "width": 130,
                "height": 65
            }, {
                "type": "o",
                "url": "https://sun9-23.u...90c/fkHmcUJiOlk.jpg",
                "width": 130,
                "height": 87
            }, {
                "type": "p",
                "url": "https://sun9-20.u...90d/ukY9qydvw0s.jpg",
                "width": 200,
                "height": 133
            }, {
                "type": "q",
                "url": "https://sun9-35.u...90e/C3j42_VrESU.jpg",
                "width": 320,
                "height": 213
            }, {
                "type": "r",
                "url": "https://sun9-24.u...90f/VQY9oNX9OsQ.jpg",
                "width": 510,
                "height": 340
            }, {
                "type": "s",
                "url": "https://sun9-50.u...908/Wo3nGffa3eA.jpg",
                "width": 75,
                "height": 37
            }, {
                "type": "x",
                "url": "https://sun9-28.u...90a/DTF_alxRVgI.jpg",
                "width": 604,
                "height": 302
            }, {
                "type": "y",
                "url": "https://sun9-70.u...90b/660JpxKxdYA.jpg",
                "width": 800,
                "height": 400
            }],
            "text": "",
            "date": 1588872399,
            "has_tags": False
        }]
    }
}

photos = [
    f"photo{item['owner_id']}_{item['id']}" for item in json_response['response']['items']]

TOKEN = 'aeea642e6d43e6a3ff5e068a1e455a7746f928aec2a3a771c4566a841eac45e620fed710abe7a14971ac6'


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, 195095163)
    vk = vk_session.get_api()
    t = vk_session.

    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            user = get_user(event.obj.message['from_id'], vk)
            mes = f"Привет {user[0]}!"

            attachments = photos[random.randint(0, len(photos) - 1)]

            vk.messages.send(
                user_id=event.obj.message['from_id'],
                attachment=attachments,
                random_id=get_random_id(),
                message=mes
            )


def get_user(u_id, vk):
    response = vk.users.get(user_id=u_id, fields="city")
    print(response)
    return (response[0]['first_name'], response[0]['city']['title'])


if __name__ == '__main__':
    main()
