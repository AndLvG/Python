from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import random, time

TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'


def start(update, context):
    update.message.reply_text(
        "Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!\n"
        "Мжете пройти в зал 1")
    return 1


def zal_1(update, context):
    update.message.reply_text(
        "Вы находитесь в зале 1\n"
        "можете пройти в зал 2")
    return 2

def zal_2(update, context):
    update.message.reply_text(
        "Вы находитесь в зале 2\n"
        "можете пройти в зал 3")
    return 3

def zal_3(update, context):
    update.message.reply_text(
        "Вы находитесь в зале 3\n"
        "можете пройти в зал 1 или 4")
    zal = update.message.text
    return int(zal)

def zal_4(update, context):
    update.message.reply_text(
        "Вы находитесь в зале 4\n"
        "можете пройти в зал 1")
    return 1


def stop(update, context):
    return ConversationHandler.END


updater = Updater(TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)
dp = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        1: [MessageHandler(Filters.text, zal_1)],
        2: [MessageHandler(Filters.text, zal_2)],
        3: [MessageHandler(Filters.text, zal_3)],
        4: [MessageHandler(Filters.text, zal_4)]
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)
dp.add_handler(conv_handler)

# Запускаем цикл приема и обработки сообщений.
updater.start_polling()

# Ждём завершения приложения.
# (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
updater.idle()
