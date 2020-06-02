from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
import random

TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'

voprosi = {
    "test": [
        {
            "question": "В каком году была война 1812 года?",
            "response": "1812"
        },
        {
            "question": "В каком году была война 1813 года?",
            "response": "1813"
        },
        {
            "question": "В каком году была война 1814 года?",
            "response": "1814"
        },
        {
            "question": "В каком году была война 1815 года?",
            "response": "1815"
        },
        {
            "question": "В каком году была война 1816 года?",
            "response": "1816"
        },
        {
            "question": "В каком году была война 1817 года?",
            "response": "1817"
        },
        {
            "question": "В каком году была война 1818 года?",
            "response": "1818"
        },
        {
            "question": "В каком году была война 1819 года?",
            "response": "1819"
        },
        {
            "question": "В каком году была война 1820 года?",
            "response": "1820"
        },
        {
            "question": "В каком году была война 1821 года?",
            "response": "1821"
        },
        {
            "question": "В каком году была война 1822 года?",
            "response": "1822"
        },
        {
            "question": "В каком году была война 1823 года?",
            "response": "1823"
        }
    ]
}
vopr = []
for item in voprosi["test"]:
    vopr.append([item["question"], item["response"]])

print(vopr)
random.shuffle(vopr)
print(vopr)

prav_otvet = 0


def start(update, context):
    context.user_data['prav_otvet'] = 0
    context.user_data['vopros'] = 0
    update.message.reply_text(
        f"Будет предложено ответить на несколько вопросов\nВопрос номер {context.user_data['vopros'] + 1}\n{vopr[context.user_data['vopros']][0]}")
    return 1


def step_1(update, context):
    if vopr[context.user_data['vopros']][1] == update.message.text:
        context.user_data['prav_otvet'] += 1
    if context.user_data['vopros'] == 9:
        update.message.reply_text(f"Опрос закончился\nПравильных ответов {context.user_data['prav_otvet']}")
        return
    else:
        context.user_data['vopros'] += 1
        update.message.reply_text(
            f"Вопрос номер {context.user_data['vopros'] + 1}\n{vopr[context.user_data['vopros']][0]}")
        return 1


def stop(update, context):
    return ConversationHandler.END


updater = Updater(TOKEN, use_context=True)  # , request_kwargs=REQUEST_KWARGS)
dp = updater.dispatcher

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],

    states={
        1: [MessageHandler(Filters.text, step_1)]
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
