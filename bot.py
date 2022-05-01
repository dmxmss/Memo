import os

from telegram import Update
from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm Memo, bot for memorization anything you want")

def main() -> None:
    updater = Updater(os.environ["BOT_API_TOKEN"])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
