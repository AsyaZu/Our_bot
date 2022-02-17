from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def calc(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()
    a = items[1]
    update.message.reply_text(f'{eval(a)}')

