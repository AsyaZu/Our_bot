from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from calc import*
from pict import*
from layoutswitch import*

updater = Updater('5231750444:AAFnNv0xzckgyU83M8fdU7qFgeBp5jqn8v0')

updater.dispatcher.add_handler(CommandHandler('calc', calc))
updater.dispatcher.add_handler(CommandHandler('pict', pict))
updater.dispatcher.add_handler(CommandHandler('lay', layout_switch))

print('start')

updater.start_polling()
updater.idle()