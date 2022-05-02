import datetime

from lib import *
from typing import List

from telegram import Update
from telegram.ext import (
    CallbackContext,
    ConversationHandler,
)

TYPING_ENTRY_NAME, TYPING_ENTRY_DESCRIPTION = range(2)

def start(update: Update, context: CallbackContext) -> None:
    context.user_data["entries"] = []
    update.message.reply_text("Hello! I'm Memo, bot for memorization anything you want")

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("""
/add - create entry
/remove <name> - remove entry by <name>
/check - check all entries in this day
    """)

def add(update: Update, context: CallbackContext) -> int:
    update.message.reply_text("Please type entry name")
    return TYPING_ENTRY_NAME

def handle_typing_name(update: Update, context: CallbackContext) -> int:
    user_data = context.user_data
    entry_name = update.message.text
    entries = user_data["entries"]

    if entry_name in names(entries):
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
    entries = user_data["entries"]
    entry_name = user_data["entry_name"]
    entry_description = update.message.text

    entries.append(Entry(entry_name, entry_description))

    clear_cache(context)

    update.message.reply_text(
        f"Entry with name {entry_name} was successfully created"
    )

    return ConversationHandler.END

def cancel(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Cancelled"
    )

    clear_cache(context)

    return ConversationHandler.END

def remove(update: Update, context: CallbackContext) -> None:
    try:
        entry_name = context.args[0]
        entries = context.user_data["entries"]
        if entry_name not in names(entries):
            update.message.reply_text(
                "Entry with this name is absent"
            )
            return

        remove_entry_by_name(entry_name, context)

        update.message.reply_text(
            f"Entry with name {entry_name} was successfully removed"
        )
    except IndexError:
        update.message.reply_text(
            "Usage: /remove <name>"
        )


def check(update: Update, context: CallbackContext) -> None:
    entries = context.user_data["entries"]

    if not entries:
        update.message.reply_text(
            "You don't have any entries"
        )

    today_entries = filter(today_entry, entries)
    text = "" 

    for entry in today_entries:
        text += str(entry) + "\n"

    update.message.reply_text(text)

def names(entries: List[Entry]) -> List[str]:
    return list(map(lambda entry: entry.name, entries))

def today_entry(entry: Entry) -> bool:
    today = datetime.datetime.today()
    next_repetition = entry.next_repetition

    return today.year == next_repetition.year and today.month == next_repetition.month and today.day == next_repetition.day

def remove_entry_by_name(name: str, context: CallbackContext) -> None:
    entries = context.user_data["entries"]
    context.user_data["entries"] = list(filter(lambda entry: entry.name != name, entries))

def clear_cache(context: CallbackContext) -> None:
    user_data = context.user_data
    if "entry_name" in user_data:
        del user_data["entry_name"]
