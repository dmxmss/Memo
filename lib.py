import datetime

class Entry:
    def __init__(self, name: str, description: str):
        today = datetime.datetime.today()

        self._repetitions = [datetime.timedelta(hours=1)
                            ,datetime.timedelta(hours=3)
                            ,datetime.timedelta(days=1)
                            ,datetime.timedelta(weeks=1)
                            ,datetime.timedelta(days=30)]
        self._name = name
        self._description = description
        self._date_created = today
        self._amount_of_repetitions = 0
        self._next_repetition = today + self._repetitions[0] 

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

        return diff >= datetime.timedelta(0) & self._amount_of_repetitions < total_repetitions
