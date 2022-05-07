import pytest
from src.lib import Entry

class TestEntry:
    def test_just_created(self):
        import datetime

        date = datetime.datetime.today()
        entry = Entry(name="just created", date_created=date)

        assert entry.next_repetition == (date + entry.repetitions[0])

    def test_first_repeat(self):
        import datetime

        date = datetime.datetime.today()
        entry = Entry(name="first repetition", date_created=date, amount_of_repetitions=1)

        assert entry.next_repetition == (date + entry.repetitions[1])

    def test_second_repeat(self):
        import datetime

        date = datetime.datetime.today()
        entry = Entry(name="second repetition", date_created=date, amount_of_repetitions=2)

        assert entry.next_repetition == (date + entry.repetitions[2])
