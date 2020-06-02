from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, CallbackQueryHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
import requests
import logging
from io import BytesIO

TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

err_json = {'ok': True, 'result': {'message_id': 391,
                                   'from': {'id': 1035631059, 'is_bot': True, 'first_name': 'Testing Lyceum',
                                            'username': 'Testing_Lyceum_bot'},
                                   'chat': {'id': 476285247, 'first_name': 'Андрей', 'last_name': 'Львов',
                                            'username': 'LvovAndrey', 'type': 'private'}, 'date': 1589273600, 'photo': [
        {
            'file_id': 'AgACAgIAAxkDAAIBh166ZAABvF-KMjOpCwYBNIY_0NqhYgACZq0xGzGz2EmQfA0e8Se2OhgS6JEuAAMBAAMCAANtAAO1zQEAARkE',
            'file_unique_id': 'AQADGBLokS4AA7XNAQAB', 'file_size': 21792, 'width': 320, 'height': 240}, {
            'file_id': 'AgACAgIAAxkDAAIBh166ZAABvF-KMjOpCwYBNIY_0NqhYgACZq0xGzGz2EmQfA0e8Se2OhgS6JEuAAMBAAMCAAN4AAO2zQEAARkE',
            'file_unique_id': 'AQADGBLokS4AA7bNAQAB', 'file_size': 64813, 'width': 600, 'height': 450}],
                                   'caption': 'Вот так выглядит Калуга'}}


def get_image(toponym_to_find, map_type):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
        "geocode": toponym_to_find,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    json_response = response.json()
    if json_response["response"]["GeoObjectCollection"]["featureMember"]:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    else:
        return None
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    delta = "0.02"
    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([delta, delta]),
        "l": map_type,
        "pt": f"{toponym_longitude},{toponym_lattitude},pm2dgl"
    }

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)

    return BytesIO(response.content)


def start(update, context):
    update.message.reply_text(
        "Я бот-геокодер. Введи название местности которую хочешь увидеть. Например Калуга")
    return 1


def geocoder_image(update, context):
    chat_id = update.message.chat.id
    toponim = update.message.text
    map = get_image(toponim, 'map')
    if not map:
        update.message.reply_text("Объект не найден")
        return ConversationHandler.END

    url = "https://api.telegram.org/bot1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U/sendPhoto";
    files = {'photo': map}
    data = {'chat_id': chat_id, 'caption': f'Вот так выглядит {toponim}'}
    r = requests.post(url, files=files, data=data)
    print(r.json())
    if r.json()['ok'] != True:
        update.message.reply_text(
            "Произошла ошибка при отправке данных\n" + r.json()['description']
        )

    return ConversationHandler.END


def stop(update, context):
    return ConversationHandler.END


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    update.message.reply_text("Произошла ошибка при отправке данных\n" + context.error)


updater = Updater(TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)
dp = updater.dispatcher

dp.add_error_handler(error)

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [MessageHandler(Filters.text, geocoder_image)]
    },
    fallbacks=[CommandHandler('stop', stop)]
)
dp.add_handler(conv_handler)

updater.start_polling()
updater.idle()
