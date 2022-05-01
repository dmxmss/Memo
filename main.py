import os

from bot import *
from telegram.ext import Updater

def main() -> None:
    updater = Updater(os.environ["BOT_API_TOKEN"])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
