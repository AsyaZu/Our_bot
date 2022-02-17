from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import matplotlib.pyplot as plt
import numpy as np

def pict(update: Update, context: CallbackContext):
    msg = update.message.text
    items = msg.split()# сплитим сообщение
    a = int(items[1])
    b = int(items[2])
    c = int(items[3])
    x = np.arange(a, b, c)
    y = np.sin(x)
    plt.plot(x, y)
    plt.savefig('saved_figure.png') #сохраняем график в файл
    update.message.reply_text(f'sin {a}, {b}, {c}')
    context.bot.sendPhoto(chat_id=update.message.chat_id, photo="saved_figure.png", caption="sin {a}, {b}, {c}")
    



