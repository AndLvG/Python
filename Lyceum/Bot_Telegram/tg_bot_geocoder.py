from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import requests
import logging

TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def ya_translate(mytext, lang='ru-en'):
    URL = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    KEY = "trnsl.1.1.20200511T163423Z.b33f24575bcce593.ca5642bae3777446ce37b47eca18526f907b808b"
    params = {
        "key": KEY,
        "text": mytext,
        "lang": lang  # Здесь мы указываем с какого языка на какой мы делаем переводим
    }
    response_json = requests.get(URL, params=params).json()
    return ''.join(response_json["text"])


def start(update, context):
    t_keyboard = [[InlineKeyboardButton("С русского на английский", callback_data='ru-en'),
                   InlineKeyboardButton("С английского на русский", callback_data='en-ru')]]
    reply_markup = InlineKeyboardMarkup(t_keyboard)

    update.message.reply_text(
        "Я бот-Переводчик. Какой тип перевода вас интересует?",
        reply_markup=reply_markup
    )
    return 1


def button(update, context):
    query = update.callback_query
    context.user_data['translate_type'] = query.data
    query.answer()
    query.edit_message_text("Введите текст для перевода")
    return 2


def translate(update, context):
    print(update.message.text)
    translated_text = ya_translate(update.message.text, lang=context.user_data['translate_type'])
    update.message.reply_text(translated_text)
    return ConversationHandler.END


def stop(update, context):
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


updater = Updater(TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)
dp = updater.dispatcher

# dp.add_handler(CommandHandler("start", start))
# dp.add_handler(CallbackQueryHandler(button))
dp.add_error_handler(error)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [CallbackQueryHandler(button)],
        2: [MessageHandler(Filters.text, translate)]
    },
    fallbacks=[CommandHandler('stop', stop)]
)
dp.add_handler(conv_handler)

updater.start_polling()
updater.idle()
