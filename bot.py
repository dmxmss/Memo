import os
from lib import *
from typing import List

from telegram import Update
from telegram.ext import (
    CallbackContext,
    ConversationHandler,
)

TYPING_ENTRY_NAME, TYPING_ENTRY_DESCRIPTION = range(2)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm Memo, bot for memorization anything you want")

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
    /add - create entry
    """)

def add(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Please type entry name")
    return TYPING_ENTRY_NAME

def handle_typing_name(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    entry_name = update.message.text
    entries = user_data.get("entries", [])

    if entry_name in _names(entries):
        update.message.reply_text(
            "Entry with this name already exists"
            "Please type another entry name"
        )
        return TYPING_ENTRY_NAME

    user_data["entry_name"] = entry_name

    update.message.reply_text("Ok. Type description of the entry") 

    return TYPING_ENTRY_DESCRIPTION

def handle_typing_description(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    entry_description = update.message.text
    entry_name = user_data["entry_name"]
    entries = user_data.get("entries", [])

    entry = Entry(entry_name, entry_description)
    entries.append(entry)

    _clear_cache(context)
    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Cancelled"
    )
    _clear_cache(context)

    return ConversationHandler.END

def _names(entries: List[Entry]) -> List[str]:
    return list(map(lambda entry: entry.name, entries))

def _clear_cache(context: CallbackContext) -> None:
    user_data = context.user_data
    del user_data["entry_name"]
