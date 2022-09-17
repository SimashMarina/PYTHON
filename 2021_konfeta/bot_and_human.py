from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
import datetime
from spy import *

from random import randint

STARTBOT = 0
NAME = 1
OPERATIONONE = 2
OPERATIONTWO = 3
RESULT_BOT = 4
name = ''

def proverInt(update, size):
    try:
        return int(size)
    except:
        return update.message.reply_text(f'\nОшибка, введите число от 1 до 28: ')

def game_with_bot(update: Update, context: ContextTypes):
    log(update, context)
    context.bot.send_message(update.effective_chat.id, 'Добро пожаловать в бота, в котором '
                                                       'можно попытаться сыграть в игру 2021 конфета\n'
                                                       'Правила игры: \n1) На столе лежит 2021 конфета.' 
                                                       'Играют два игрока, делая ход друг после друга. \n2) За один ход '
                                                       'можно забрать не более 28 конфет.' 
                                                       '\n3) Все конфеты оппонента достаются тому, кто сделал последний ход. '
                                                       '\nУдачной игры!\nИгра с ботом')
    context.bot.send_message(update.effective_chat.id, 'Введите своё имя: ')

    return NAME

def names(update, context):
    log(update, context)
    global name
    name = update.message.text
    context.bot.send_message(update.effective_chat.id, f'Ходит {name}: ')

    return OPERATIONONE

def namess(update, context):
    global name
    context.bot.send_message(update.effective_chat.id, f'Ходит {name}: ')


def ostatok_bot(update, n):
    if n != 0:
        return update.message.reply_text(f'Осталось конфет:  {n}')
    else:
        if count == 0:
            update.message.reply_text(f'Поздравляем! Побеждает бот!\n{name}, '
                                        'не расстраивайтесь, в следующий раз у Вас обязательно получится выиграть :)')
            update.message.reply_text('Спасибо, что использовали нашего бота, ведь мы очень старались писать это чудо! Йоу!')
        else:
            update.message.reply_text(f'Поздравляем! Побеждает {name}! Вы прекрасно справились :)')
            update.message.reply_text('Спасибо, что использовали нашего бота, ведь мы очень старались!')

def operation_player(update, context):
    log(update, context)
    global n
    global name
    global size
    global count
    count = 0
    size = proverInt(update, update.message.text)
    if 0 < size and size <= 28 and size <= n:
        n = n - size
        ostatok_bot(update, n)
        if n >= 1: 
            update.message.reply_text(f'\n{name}, Ваш ход: ')
            return OPERATIONTWO
        else:
            return RESULT_BOT
    else:
        if n >= 28:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до 28: ')
        else:
            update.message.reply_text(f'\nОшибка, введите число в диапозоне 1 до {n}: ')

def operation_bot(update, context):
    log(update, context)
    global n
    global size
    global count
    count = 1
    ostatok_bot(update, n)
    if n >= 1:
        if n >= 28:
            num = randint(1, 29)
            update.message.reply_text(f'\nХодит бот: {num}: ')
            n = n - num
            return OPERATIONONE
        else:
            num = randint(1, n)
            update.message.reply_text(f'\nХодит бот: {num}: ')
            n = n - num
            return OPERATIONONE
    else:
        return RESULT_BOT







# def bot():
#     print('Игра с ботом!')
#     player = input('Введите Ваше имя: ')
#     bot_player = 1 
#     def play_game_with_bot(n, player):
#         count = 0
#         while n > 0:
#             count = count % 2
#             if count == 1:
#                 num = randint(1, 29)
#                 print(f'\nХодит бот: {num}')
#                 n = n - num
#                 counting(n, count, player)
#             if count == 0:
#                 size = int(input(f'\n{player}, Ваш ход: '))
#                 if size > 28 or size <= 0:
#                     print('Ошибка!')
#                 n = n - size
#                 counting(n, count, player)
#             count += 1
#     play_game_with_bot(n, player)