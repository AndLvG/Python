from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import logging
import time

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'


# REQUEST_KWARGS = {
#     'proxy_url': 'socks4://171.103.9.22:4145/',
#     # Optional, if you need authentication:
#     'urllib3_proxy_kwargs': {
#         'assert_hostname': 'False',
#         'cert_reqs': 'CERT_NONE'
#         # 'username': 'user',
#         # 'password': 'password'
#     }
# }


# Определяем функцию-обработчик сообщений.
# У неё два параметра, сам бот и класс updater, принявший сообщение.
def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    update.message.reply_text(f'Я получил сообщение <{update.message.text}>')


def start(update, context):
    update.message.reply_text(
        "Привет! Я эхо-бот. Напишите мне что-нибудь, и я пришлю это назад!")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def timee(update, context):
    update.message.reply_text(
        f"Текущее время {time.strftime('%X')}")


def date(update, context):
    update.message.reply_text(
        f"Текущая дата {time.strftime('%x')}")


def set_timer(update, context):
    update.message.reply_text(
        f"Заведён таймер на  {int(context.args[0])} секунд")
    time.sleep(int(context.args[0]))
    update.message.reply_text(
        f"Таймер сработал")


def main():
    # Создаём объект updater.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    updater = Updater(TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)

    # Получаем из него диспетчер сообщений.
    dp = updater.dispatcher

    # Создаём обработчик сообщений типа Filters.text
    # из описанной выше функции echo()
    # После регистрации обработчика в диспетчере
    # эта функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(Filters.text, echo)

    # Регистрируем обработчик в диспетчере.
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("date", date))
    dp.add_handler(CommandHandler("time", timee))
    dp.add_handler(CommandHandler("set_timer", set_timer, pass_args=True))
    dp.add_handler(text_handler)

    # Запускаем цикл приема и обработки сообщений.
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
