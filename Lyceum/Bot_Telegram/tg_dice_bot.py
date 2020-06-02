from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup
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
    update.message.reply_text("Утановим таймер", reply_markup=reply_markup)


def set_timer1(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.message.chat_id
    try:
        # args[0] должен содержать значение аргумента (секунды таймера)
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text(
                'Извините, не умеем возвращаться в прошлое')
            return

        # Добавляем задачу в очередь
        # и останавливаем предыдущую (если она была)
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(task, due, context=chat_id)
        # Запоминаем созданную задачу в данных чата.
        context.chat_data['job'] = new_job
        # Присылаем сообщение о том, что всё получилось.
        update.message.reply_text(f'Вернусь через {due} секунд')

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Вернулся!')


def unset_timer(update, context):
    # Проверяем, что задача ставилась
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет активного таймера')
        return
    job = context.chat_data['job']
    # планируем удаление задачи (выполнится, когда будет возможность)
    job.schedule_removal()
    # и очищаем пользовательские данные
    del context.chat_data['job']
    update.message.reply_text('Хорошо, вернулся сейчас!')


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

timer_keyboard = [['/set 30', '/set 60'],
                  ['5 минут', 'вернуться назад']]
t_keyboard = [[InlineKeyboardButton("На 30 секунд", callback_data='/set 30'),
               InlineKeyboardButton("На 60 секунд", callback_data='/set 60')],
              [InlineKeyboardButton("На 5 минут", callback_data='/set 3'),
               InlineKeyboardButton("вернуться назад", callback_data='/set 60')]
              ]

reply_markup = InlineKeyboardMarkup(t_keyboard, one_time_keyboard=False, resize_keyboard=True)
# timer_markup = ReplyKeyboardMarkup(timer_keyboard, one_time_keyboard=False, resize_keyboard=True)

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.regex('Бросить кубик'), dice))
dp.add_handler(MessageHandler(Filters.regex('Установить таймер'), timer))

dp.add_handler(MessageHandler(Filters.regex('кинуть один шестигранный кубик'), dice1))
dp.add_handler(MessageHandler(Filters.regex('кинуть 2 шестигранных кубика одновременно'), dice2))
dp.add_handler(MessageHandler(Filters.regex('кинуть 20-гранный кубик'), dice3))
dp.add_handler(MessageHandler(Filters.regex('вернуться назад'), start))

# dp.add_handler(MessageHandler(Filters.regex('30 секунд'), set_timer1))
# dp.add_handler(MessageHandler(Filters.regex('1 минута'), set_timer2))
# dp.add_handler(MessageHandler(Filters.regex('5 минут'), set_timer3))

dp.add_handler(CommandHandler("set", set_timer1,
                              pass_args=True,
                              pass_job_queue=True,
                              pass_chat_data=True))
dp.add_handler(CommandHandler("unset", unset_timer,
                              pass_chat_data=True))

dp.add_handler(CommandHandler("close", close_keyboard))

# Запускаем цикл приема и обработки сообщений.
updater.start_polling()

# Ждём завершения приложения.
# (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
updater.idle()
