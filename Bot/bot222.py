from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
import datetime

updater = Updater('5498101437:AAHNMtqhJB7DQ6IUaSQuGslg0_fxJ-yI6Xc')
dispatcher = updater.dispatcher

n = 202
names = []
count = 1
START = 0
FIRSTNAME = 1
SECONDNAME = 2
OPERATION = 3
SECONDOPERATION = 4
RESULT = 5
first_name = ''
second_name = ''

# board = [[InlineKeyboardButton('Да', callback_data='0')]]
# update.message.reply_text('Попробуете?', reply_markup=InlineKeyboardMarkup(board))

def log(update: Update, context: ContextTypes):
    file = open(r'C:\Users\Начальник\Desktop\МАРИНА\PYTHON\Bot\ddb.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.datetime.now().time()}\n')
    file.close()

def start(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бота, в котором '
                                                       'можно попытаться сыграть в игру 2021 конфета\n'
                                                       'Правила игры: \n1) На столе лежит 2021 конфета.' 
                                                       'Играют два игрока, делая ход друг после друга. \n2) За один ход '
                                                       'можно забрать не более 28 конфет.' 
                                                       '\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. '
                                                       '\nУдачной игры!\n')
    context.bot.send_message(update.effective_chat.id, 'Введите имя первого человека: ')
    
    return FIRSTNAME

def first_names(update, context):
    log(update, context)
    global first_name
    first_name = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведите имя второго игрока: ')

    return SECONDNAME

def second_names(update, context):
    log(update, context)
    global second_name
    second_name = update.message.text
    update.message.reply_text(f'Ходит {first_name}: ')
    return SECONDOPERATION

def numbers(number):
        int(number)

def ostatok(update, n):
    if n != 0:
        return update.message.reply_text(f'Осталось конфет:  {n}')
    else:
        if count == 0:
            update.message.reply_text(f'Поздравляем! Побеждает {second_name}!\n{first_name}, '
                                        'не расстраивайтесь, в следующий раз у Вас обязательно получится выиграть :)')
            update.message.reply_text('Спасибо, что использовали нашего бота, ведь мы очень старались писать это чудо! Йоу!')
        else:
            update.message.reply_text(f'Поздравляем! Побеждает {first_name}!\n{second_name}, '
                                        'не расстраивайтесь, в следующий раз у Вас обязательно получится выиграть :)')
            update.message.reply_text('Спасибо, что использовали нашего бота, ведь мы очень старались писать это чудо! Йоу!')

def proverInt(update, size):
    try:
        return int(size)
    except:
        return update.message.reply_text(f'\nОшибка, введите число от 1 до 28: ')

def first_operation(update, context):
    log(update, context)
    global n
    global names
    global size
    global count
    count = 0
    size = proverInt(update, update.message.text)
    if 0 < size and size <= 28 and size <= n:
        n = n - size
        ostatok(update, n)
        if n >= 1: 
            update.message.reply_text(f'\n{first_name}, Ваш ход: ')
            return SECONDOPERATION
        else:
            return RESULT
    else:
        if n >= 28:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до 28: ')
        else:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до {n}: ')

def second_operation(update, context):
    log(update, context)
    global n
    global names
    global size
    global count
    count = 1
    size = proverInt(update, update.message.text)
    if 0 < size and size <= 28 and size <= n:
        n = n - size
        ostatok(update, n)
        if n >= 1: 
            update.message.reply_text(f'\n{second_name}, Ваш ход: ')
            return OPERATION
        else:
            return RESULT
    else: 
        if n >= 28:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до 28: ')
        else:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до {n}: ')
 
def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END

def help(update, context):
    log(update, context)
    update.message.reply_text(f'В этом боте можно сыиграть в игру 2021 конфета со своим другом. '
                                'Для этого нажмите /start.'
                                '\nСпасибо, что используте наш бот!')

help_handler = CommandHandler('help', help)
start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
nameone_handler = MessageHandler(Filters.text, first_names)
nametwo_handler = MessageHandler(Filters.text, second_names)
# result_handler = CommandHandler('res', result)
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

print('\nСервер запущен')
updater.start_polling()
updater.idle()










































































































































# from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
# from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
# import datetime

# updater = Updater('5498101437:AAHNMtqhJB7DQ6IUaSQuGslg0_fxJ-yI6Xc')
# dispatcher = updater.dispatcher

# global n 
# n = 20
# global m 
# m = 28
# names = []
# START = 0
# FIRSTNAME = 1
# SECONDNAME = 2
# OPERATION = 3
# RESULT = 4
# first_name = ''
# second_name = ''
# global msg
# msg = ''




# # board = [[InlineKeyboardButton('Да', callback_data='0')]]
# # update.message.reply_text('Попробуете?', reply_markup=InlineKeyboardMarkup(board))

# def log(update: Update, context: ContextTypes):
#     file = open(r'C:\Users\Начальник\Desktop\МАРИНА\PYTHON\Bot\ddb.csv', 'a', encoding='utf-8')
#     file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.datetime.now().time()}\n')
#     file.close()

# def numbers(number):
#         return int(number)

# def start(update, context):
#     log(update, context)
#     context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бота, в котором '
#                                                        'можно попытаться сыграть в игру 2021 конфета\n'
#                                                        'Правила игры: \n1) На столе лежит 2021 конфета.' 
#     'Играют два игрока, делая ход друг после друга. \n2) За один ход можно забрать не более 28 конфет.' 
#     '\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n')
#     context.bot.send_message(update.effective_chat.id, 'Введите имя первого человека: ')
    
#     return FIRSTNAME


# def first_names(update, context):
#     log(update, context)
#     global first_name
#     first_name = update.message.text
#     context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведите имя второго игрока: ')

#     return SECONDNAME


# def second_names(update, context):
#     log(update, context)
#     global second_name
#     second_name = update.message.text
#     update.message.reply_text(f'Ходи первым {first_name}: ')
#     return OPERATION

# def operation(update, context):
#     log(update, context)
#     global n
#     global names
#     names = [first_name, second_name]
#     count = 1
    
#     while n >= 1:
#         size = numbers(update.message.text)
#         count = count%2
#         names1 = names[count]
#         count = count + 1
#         n = n - size
#         update.message.reply_text(f'Осталось конфет: {n}, \n{names1}, Ваш ход: ')
#     return RESULT

# def result(update, context):
#     log(update, context)
#     pass

# def cancel(update, context):
#     context.bot.send_message(update.effective_chat.id, 'Прощай!')

#     return ConversationHandler.END



# start_handler = CommandHandler('start', start)
# cancel_handler = CommandHandler('cancel', cancel)
# nameone_handler = MessageHandler(Filters.text, first_names)
# nametwo_handler = MessageHandler(Filters.text, second_names)
# result_handler = CommandHandler('res', result)
# oper_handler = MessageHandler(Filters.text, operation)
# conv_handler = ConversationHandler(entry_points=[start_handler],
#                                    states={
#                                        FIRSTNAME: [nameone_handler],
#                                        SECONDNAME: [nametwo_handler],
#                                        OPERATION: [oper_handler],
#                                        RESULT: [result_handler]
#                                    },
#                                    fallbacks=[cancel_handler])


# dispatcher.add_handler(conv_handler)
# # dispatcher.add_handler(oper_handler)

# print('Server start')
# dispatcher.add_handler(conv_handler)
# updater.start_polling()
# updater.idle()