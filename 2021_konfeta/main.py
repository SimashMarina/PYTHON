from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
import datetime
from bot_and_human import *
from human_and_human import *
from spy import *

updater = Updater('5498101437:AAHNMtqhJB7DQ6IUaSQuGslg0_fxJ-yI6Xc')
dispatcher = updater.dispatcher

# board = [[InlineKeyboardButton('Да', callback_data='0')]]
# update.message.reply_text('Попробуете?', reply_markup=InlineKeyboardMarkup(board))

# def numberSecond(update, context):
#     global numberTwo
#     numberTwo = numbers(update.message.text)
#     board = [[InlineKeyboardButton('+', callback_data='0'), InlineKeyboardButton('-', callback_data='1')],
#              [InlineKeyboardButton('*', callback_data='2'), InlineKeyboardButton(':', callback_data='3')]]
#     update.message.reply_text('Выбери:', reply_markup=InlineKeyboardMarkup(board))

#     return OPERATION


# def operation(update, context):
#     global res
#     # global oper
#     que = update.callback_query
#     var = que.data
#     que.answer()
#     res = result(numberOne, numberTwo, var)
#     que.edit_message_text(text=f'Результат: {res}')


def help(update, context):
    log(update, context)
    update.message.reply_text(f'В этом боте можно сыиграть в игру 2021 конфета со своим другом. '
                                'Для этого нажмите /start.'
                                '\nСпасибо, что используте наш бот!')

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END

help_handler = CommandHandler('help', help)
start_handler = CommandHandler('start', game_with_human)
cancel_handler = CommandHandler('cancel', cancel)
nameone_handler = MessageHandler(Filters.text, first_names)
nametwo_handler = MessageHandler(Filters.text, second_names)
oper_handler = MessageHandler(Filters.text, first_operation)
sec_operation = MessageHandler(Filters.text, second_operation)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                       FIRSTNAME: [nameone_handler],
                                       SECONDNAME: [nametwo_handler],
                                       OPERATION: [oper_handler],
                                       SECONDOPERATION: [sec_operation],
                                        },
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(help_handler)


def cancell(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END

cancell_handler = CommandHandler('cancel', cancell)
start_bot_handler = CommandHandler('startbot', game_with_bot)
name_handler = MessageHandler(Filters.text, names)
oper_bot_handler = MessageHandler(Filters.text, operation_player)
oper_human_handler = MessageHandler(Filters.text, operation_bot)
conver_handler = ConversationHandler(entry_points=[start_bot_handler],
                                   states={
                                       NAME: [name_handler],
                                       OPERATIONONE: [oper_bot_handler],
                                       OPERATIONTWO: [oper_human_handler],
                                        },
                                   fallbacks=[cancell_handler])

namesss = CommandHandler('name', namess)

dispatcher.add_handler(conver_handler)
dispatcher.add_handler(namesss)

print('\nСервер запущен')
updater.start_polling()
updater.idle()