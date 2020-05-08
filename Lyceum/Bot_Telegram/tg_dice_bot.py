from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import random, time

TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'


def dice(update, context):
    update.message.reply_text("Какой кубик бросаем?", reply_markup=dice_markup)


def dice1(update, context):
    update.message.reply_text(random.randint(1, 6))


def dice2(update, context):
    update.message.reply_text(f'{random.randint(1, 6)} {random.randint(1, 6)}')


def dice3(update, context):
    update.message.reply_text(random.randint(1, 20))


def timer(update, context):
    update.message.reply_text("Утановим таймер", reply_markup=timer_markup)


def set_timer1(update, context):
    update.message.reply_text(
        f"засек 30 секунд")
    time.sleep(int(30))
    update.message.reply_text(
        f"Таймер сработал")

def set_timer2(update, context):
    update.message.reply_text(
        f"засек 1 минуту")
    time.sleep(int(60))
    update.message.reply_text(
        f"Таймер сработал")

def set_timer3(update, context):
    update.message.reply_text(
        f"засек 5 минут")
    time.sleep(int(300))
    update.message.reply_text(
        f"Таймер сработал")

def start(update, context):
    update.message.reply_text(
        "Я Бот-помощник для игр",
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


updater = Updater(TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)
dp = updater.dispatcher

reply_keyboard = [['Бросить кубик', 'Установить таймер'], ['/close']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dice_keyboard = [['кинуть один шестигранный кубик', 'кинуть 2 шестигранных кубика одновременно'],
                 ['кинуть 20-гранный кубик'], ['вернуться назад']]
dice_markup = ReplyKeyboardMarkup(dice_keyboard, one_time_keyboard=False, resize_keyboard=True)

timer_keyboard = [['30 секунд', '1 минута'],
                  ['5 минут', 'вернуться назад']]
timer_markup = ReplyKeyboardMarkup(timer_keyboard, one_time_keyboard=False, resize_keyboard=True)

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.regex('Бросить кубик'), dice))
dp.add_handler(MessageHandler(Filters.regex('Установить таймер'), timer))

dp.add_handler(MessageHandler(Filters.regex('кинуть один шестигранный кубик'), dice1))
dp.add_handler(MessageHandler(Filters.regex('кинуть 2 шестигранных кубика одновременно'), dice2))
dp.add_handler(MessageHandler(Filters.regex('кинуть 20-гранный кубик'), dice3))
dp.add_handler(MessageHandler(Filters.regex('вернуться назад'), start))

dp.add_handler(MessageHandler(Filters.regex('30 секунд'), set_timer1))
dp.add_handler(MessageHandler(Filters.regex('1 минута'), set_timer2))
dp.add_handler(MessageHandler(Filters.regex('5 минут'), set_timer3))

dp.add_handler(CommandHandler("close", close_keyboard))

# Запускаем цикл приема и обработки сообщений.
updater.start_polling()

# Ждём завершения приложения.
# (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
updater.idle()
