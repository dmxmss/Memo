import os

from bot import *
from telegram.ext import (
    Updater,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters,
)

def main() -> None:
    updater = Updater(os.environ["BOT_API_TOKEN"])
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("remove", remove))
    dispatcher.add_handler(CommandHandler("check", check))
    dispatcher.add_handler(ConversationHandler(
        entry_points=[CommandHandler("add", add)],
        states={
            TYPING_ENTRY_NAME: [MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex("^cancel$")), handle_typing_name
            )],
            TYPING_ENTRY_DESCRIPTION: [MessageHandler(
                Filters.text & ~(Filters.command | Filters.regex("^cancel$")), handle_typing_description
            )],
        },
        fallbacks=[MessageHandler(
            Filters.regex("^cancel$") & ~Filters.command, cancel
        )],
    ))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
