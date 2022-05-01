import os
import lib

from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler,
)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm Memo, bot for memorization anything you want")

