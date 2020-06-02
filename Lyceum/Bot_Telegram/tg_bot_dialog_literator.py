from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler


TOKEN = '1035631059:AAEX5dgL_rtFnF8wTDifUSg3ZqNXtsDcX2U'
STIH_STR = 'Строка 1/nСтрока 2/nСтрока 3/nСтрока 4'
stih = STIH_STR.split('/n')
print(stih)


def start(update, context):
    context.user_data['stroka'] = 0
    update.message.reply_text(stih[context.user_data['stroka']])
    context.user_data['stroka'] += 1
    return 1


def step_1(update, context):
    print(stih[context.user_data['stroka']], update.message.text)
    if stih[context.user_data['stroka']] == update.message.text:
        context.user_data['stroka'] += 1
        if context.user_data['stroka'] == len(stih):
            update.message.reply_text('Стихотворение закончилось')
            update.message.reply_text('/stop')
            return
        context.user_data['stroka'] += 1
        update.message.reply_text(context.user_data['stroka'])
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
