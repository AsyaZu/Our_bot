from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import matplotlib.pyplot as plt
import numpy as np

def pict(update: Update, context: CallbackContext):
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)

    plt.plot(x, y)
    plt.savefig('saved_figure.png') #сохраняем график в файл
    #plt.show()

    update.message.reply_text(f'Hello {update.effective_user.first_name}')



