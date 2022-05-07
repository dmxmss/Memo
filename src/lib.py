import datetime
from telegram.ext import CallbackContext
from typing import List

class Entry:
    def __init__(self, name: str, description="", date_created=datetime.datetime.today(), amount_of_repetitions=0):
        self._repetitions = [datetime.timedelta(hours=1)
                            ,datetime.timedelta(hours=3)
                            ,datetime.timedelta(days=1)
                            ,datetime.timedelta(weeks=1)
                            ,datetime.timedelta(days=30)]
        self._name = name
        self._description = description
        self._date_created = date_created
        self._amount_of_repetitions = amount_of_repetitions
        self._next_repetition = date_created + self._repetitions[amount_of_repetitions] 

    def __str__(self) -> str:
        text = f"Name: {self.name}, description: {self.description}, next repetition: {self.next_repetition}"
        return text

    def __repr__(self) -> str:
        text = f"Entry({self.name}, {self.description}, {self.date_created}, {self.amount_of_repetitions})"
        return text

    @property
    def repetitions(self):
        return self._repetitions

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def date_created(self):
        return self._date_created

    @property
    def amount_of_repetitions(self):
        return self._amount_of_repetitions

    @property
    def next_repetition(self):
        return self._next_repetition

    def repeat(self) -> bool:
        if self._time_to_repeat(): 
            today = datetime.datetime.today()
            diff = today - self._next_repetition

            self._amount_of_repetitions += 1
            self._next_repetition = self._date_created + self._repetitions[self._amount_of_repetitions] + diff
            return True

        return False

    def _time_to_repeat(self) -> bool:
        today = datetime.datetime.today()
        diff = today - self._next_repetition 
        total_repetitions = len(self._repetitions)

        return diff >= datetime.timedelta(0) and self._amount_of_repetitions < total_repetitions

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
