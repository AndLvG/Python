import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import wikipedia

TOKEN = 'aeea642e6d43e6a3ff5e068a1e455a7746f928aec2a3a771c4566a841eac45e620fed710abe7a14971ac6'


def main():
    vk_session = vk_api.VkApi(token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 195095163)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            user = get_user(event.obj.message['from_id'], vk)
            mes = f"Привет {user[0]}!"

            if 'Хочу узнать о' in event.obj.message['text'] or 'Что такое' in event.obj.message['text']:
                wikipedia.set_lang("ru")
                zapros = event.obj.message['text'].replace('Хочу узнать о','').replace('Что такое','')
                mes = wikipedia.summary(zapros, sentences=1)
            else:
                mes += "\nЧто хотите узнать?. Напишите 'Хочу узнать о...' или 'Что такое ...'"

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=mes,
                             random_id=random.randint(0, 2 ** 64))
        else:
            print(event.type)


def get_user(u_id, vk):
    response = vk.users.get(user_id=u_id, fields="city")
    print(response)
    return (response[0]['first_name'], response[0]['city']['title'])


if __name__ == '__main__':
    main()
