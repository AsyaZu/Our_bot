from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

def sum(update: Update, context: CallbackContext):
    msg = update.message.text
    update.message.reply_text(f'{eval(msg)}')

