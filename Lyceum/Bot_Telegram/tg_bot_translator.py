from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import requests
from bs4 import BeautifulSoup
from emoji import emojize
from random import choice

TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'
SMILE = ['😊', '😀', '😇', '🤠', '😎', '🤓', '👶', '🧑‍🚀', '👮', '🦸', '🧟']

def help(update, context):
    smile = emojize(choice(SMILE), use_aliases=True)
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.{}".format(smile))


def address(update, context):
    smile = emojize(choice(SMILE), use_aliases=True)
    update.message.reply_text(
        "Адрес: г. Москва, ул. Льва Толстого, 16 {}".format(smile))


def phone(update, context):
    update.message.reply_text("Телефон: +7(495)776-3030")


def site(update, context):
    update.message.reply_text("Сайт: http://www.yandex.ru/company")


def work_time(update, context):
    update.message.reply_text("Рабочее время с 8 до 17")


def start(update, context):
    update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )

def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )

# функция парсит анекдоты
def get_anecdote(bot, update):
    receive = requests.get('http://anekdotme.ru/random')  # отправляем запрос к странице
    page = BeautifulSoup(receive.text, "html.parser")  # подключаем html парсер, получаем текст страницы
    find = page.select('.anekdot_text')  # из страницы html получаем class="anekdot_text"
    for text in find:
        page = (text.getText().strip())  # из class="anekdot_text" получаем текс и убираем пробелы по сторонам
    bot.message.reply_text(page)  # отправляем один анекдот, последний


updater = Updater(TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)
dp = updater.dispatcher

dp.add_handler(CommandHandler("address", address))
dp.add_handler(CommandHandler("phone", phone))
dp.add_handler(CommandHandler("site", site))
dp.add_handler(CommandHandler("work_time", work_time))

reply_keyboard = [['/address', '/phone'],
                  ['/site', '/work_time']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
dp.add_handler(CommandHandler("start", start))

dp.add_handler(CommandHandler("close", close_keyboard))

dp.add_handler(MessageHandler(Filters.regex('Анекдот'), get_anecdote))  # обрабатываем текс кнопки

# Запускаем цикл приема и обработки сообщений.
updater.start_polling()

# Ждём завершения приложения.
# (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
updater.idle()





