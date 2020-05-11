import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
from dateutil import parser
import locale
locale.setlocale(locale.LC_ALL, "ru")

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

            try:
                dt = parser.parse(event.obj.message['text'])
                mes = dt.strftime("%A")
            except:
                mes = 'Напишите дату - я скажу день недели'

            vk.messages.send(user_id=event.obj.message['from_id'],
                             message=mes,
                             random_id=random.randint(0, 2 ** 64))
        else:
            print(event.type)


if __name__ == '__main__':
    main()
