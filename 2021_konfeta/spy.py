from telegram import Update
from telegram.ext import Updater, CommandHandler, ContextTypes
import datetime

def log(update: Update, context: ContextTypes):
    file = open(r'C:\Users\Начальник\Desktop\МАРИНА\PYTHON\2021_konfeta\history.csv', 'a', encoding='utf-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, {datetime.datetime.now().time()}\n')
    file.close()