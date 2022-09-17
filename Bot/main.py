from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, ContextTypes, MessageHandler, CallbackQueryHandler, ConversationHandler, Filters
# from bot_commands import *
# updater = Updater('5498101437:AAHNMtqhJB7DQ6IUaSQuGslg0_fxJ-yI6Xc')
# dispatcher = updater.dispatcher

# updater.dispatcher.add_handler(CommandHandler('start', start))
# updater.dispatcher.add_handler(CommandHandler('names', names_command))
# updater.dispatcher.add_handler(CommandHandler('n', numberSecond))
# updater.dispatcher.add_handler(CommandHandler('op', operation))
# updater.dispatcher.add_handler(CommandHandler('res', result))
# updater.dispatcher.add_handler(CommandHandler('play', play_game))
# updater.dispatcher.add_handler(CommandHandler('second_name', second_name_command))


# updater.dispatcher.add_handler(CommandHandler("hello", hello_command))
# updater.dispatcher.add_handler(CommandHandler("name", first_name_command))
# updater.dispatcher.add_handler(CommandHandler("name", second_name_command))



# updater.dispatcher.add_handler(CommandHandler("human", human))

# updater.dispatcher.add_handler(CommandHandler("kakdela", kakdela))
# updater.dispatcher.add_handler(CommandHandler("help", help_command))
# updater.dispatcher.add_handler(CommandHandler("time", time_command))
# updater.dispatcher.add_handler(CommandHandler("sum", sum_command))




# start_handler = CommandHandler('start', start)
# cancel_handler = CommandHandler('cancel', cancel)
# nameone_handler = MessageHandler(Filters.text, first_name_command)
# nametwo_handler = MessageHandler(Filters.text, second_name_command)
# oper_handler = CallbackQueryHandler(operation)
# conv_handler = ConversationHandler(entry_points=[start_handler],
#                                    states={
#                                        FIRSTNAME: [nameone_handler],
#                                        SECONDNAME: [nametwo_handler],
#                                     #    OPERATION: [oper_handler],
#                                    },
#                                    fallbacks=[cancel_handler])



print('server start')
# dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle()