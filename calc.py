def sum(update: Update, context: CallbackContext):
    msg = update.message.text
    update.message.reply_text(f'{eval(msg)}')

