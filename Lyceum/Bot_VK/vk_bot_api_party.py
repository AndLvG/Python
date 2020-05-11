import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import datetime

TOKEN = 'aeea642e6d43e6a3ff5e068a1e455a7746f928aec2a3a771c4566a841eac45e620fed710abe7a14971ac6'


def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, 195095163)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            user = get_user(event.obj.message['from_id'], vk)
            mes = f"Привет {user[0]}! Спасибо, что написали нам. Мы обязательно ответим."
            if user[1]:
                mes += f"\nКак поживает {user[1]}?" 
            
            dt = dt = datetime.datetime.today()
            if 'время' in event.obj.message['text'] or 'число' in event.obj.message['text'] or 'дата' in event.obj.message['text'] or 'день' in event.obj.message['text']:
                mes += f"\nДата {dt.date()}, Время {dt.time()}, День недели {dt.isoweekday()}"
            else:
                mes += "\nЯ могу сказать текущую дату и время если что. Скажи только 'дата'"
            print(f"date: {dt.strftime('%Y-%m-%d')}, time {dt.strftime('%H:%M:%S')}")

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
