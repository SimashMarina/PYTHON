import numbers
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
import datetime
from spy import *
from random import randint


n = 202
m = 28
names = []
START = 0
FIRSTNAME = 1
SECONDNAME = 2
OPERATION = 3
RESULT = 4
first_name = ''
second_name = ''


# def hello_command(update: Update, context: ContextTypes):
#     log(update, context)
#     update.message.reply_text(f'Привет, {update.effective_user.first_name}!')






def start(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, f'Добро пожаловать в бота, в котором '
                                                       'можно попытаться сыграть в игру 2021 конфета\n'
                                                       'Правила игры: \n1) На столе лежит {n} конфета.' 
    'Играют два игрока, делая ход друг после друга. \n2) За один ход можно забрать не более {m} конфет.' 
    '\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. \nУдачной игры!\n'
    'Введите свои имена: ')
    
    # return FIRSTNAME


def names_command(update: Update, context: ContextTypes):
    log(update, context)
    global first_name
    global second_name
    global names
    # context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведите свои имена: ')
    msg = update.message.text
    print(msg)
    # first_name = update.message.text
    # second_name = update.message.text
    names = msg.split()
    # second_name = update.message.text
    # first_name, second_name.split()
    first_name = names[1]
    second_name = names[2]
    update.message.reply_text(f'Привет, {first_name} и {second_name}')

    # return SECONDNAME

def numberSecond(update, context):
    log(update, context)
    board = [[InlineKeyboardButton('Приступим', callback_data='0'), InlineKeyboardButton('Выход', callback_data='1')]]
    update.message.reply_text('Выберите:', reply_markup=InlineKeyboardMarkup(board))
    return OPERATION
    # return START


def result(update: Update, context: ContextTypes, x):
    log(update, context)
    if x == '1':
        cancel()
    else:
        play_game()
        
    



def operation(update: Update, context: ContextTypes):
    log(update, context)
    global res
    que = update.callback_query
    var = que.data
    que.answer()
    res = result(var)
    que.edit_message_text(text=f'Результат: {winer}')



# def operation(update, context):
#     global res
#     # global oper
#     que = update.callback_query
#     var = que.data
#     que.answer()
#     res = result(numberOne, numberTwo, var)
#     que.edit_message_text(text=f'Результат: {res}')









def second_name_command(update: Update, context: ContextTypes):
    log(update, context)
    global second_name
    second_name = update.message.text
    update.message.reply_text(f'Привет, {first_name} и {second_name}')

    board = [[InlineKeyboardButton('Приступим', callback_data='0')]]
    update.message(InlineKeyboardMarkup(board))

    return OPERATION


def cancel(update, context):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

    return ConversationHandler.END



def play_game(update: Update, context: ContextTypes):
    log(update, context)
    global n
    global names
    count = 1
    while n > 0:
        update.message.reply_text(f'\n{names[count % 2]}, Ваш ход: ')
        msg = int(update.message.text)
        print(msg)
        size = msg
        update.message.reply_text(f'Осталось конфет: ')  
        # = {n - size}
        
        # if size > 28 or size <= 0:
        #     attempt = 3
        #     context.bot.send_message(update.effective_chat.id, 'Ошибка!')     
        #     while attempt > 0:
        #         update.message.reply_text(f'Осталось попыток {attempt}. Введите число от 1 до 28: ')
        #         size = update.message.text      
        #         if size > 28 or size <= 0:
        #             attempt -= 1
        #         else:
        #             break
        #     if attempt == 0:
        #         return 0
        # n = n - size
                  # context.bot.send_message(f'Осталось конфет = {n - size}')
                     # update.effective_chat.id, 
        # if n > 0:
        #     context.bot.send_message(update.effective_chat.id, f'Осталось конфет = {n}')
        # else: 
        #     context.bot.send_message(update.effective_chat.id, f'Больше нет конфет')
        # count += 1
    return names[not count % 2]

def winer(update: Update, context: ContextTypes):
    log(update, context)
    winer = play_game(n, names)
    if not winer:
        context.bot.send_message(update.effective_chat.id, 'Нет победителя.')
    else:
        context.bot.send_message(update.effective_chat.id, f'Поздравляю! Победил {winer}.')
    return




# def numberFirst(update, context):
#     global number
#     number = number(update.message.text)
#     context.bot.send_message(update.effective_chat.id, 'Отлично!\nВведи число: ')

#     return number




# def kakdela(update: Update, context: ContextTypes):
#     log(update, context)
#     update.message.reply_text(f'Как у тебя дела, {update.effective_user.first_name}?')

# def time_command(update: Update, context: ContextTypes):
#     log(update, context)
#     update.message.reply_text(f'{datetime.datetime.now().time()}!')

# def help_command(update: Update, context: ContextTypes):
#     log(update, context)
#     update.message.reply_text(f'/hello\n/kakdela\n/time\n/help\n/sum')

# def sum_command(update: Update, context: ContextTypes):
#     log(update, context)
#     msg = update.message.text
#     print(msg)
#     items = msg.split() 
#     x = int(items[1])
#     y = int(items[2])
#     update.message.reply_text(f'{x} + {y} = {x+y}')