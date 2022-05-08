import pytest
from src.lib import Entry

class TestEntry:
    def test_just_created(self, basic_entry, in_one_hour):
        assert basic_entry.next_repetition == in_one_hour

    def test_first_repeat(self, entry_with_one_repeat, in_three_hours):
        assert entry_with_one_repeat.next_repetition == in_three_hours

    def test_second_repeat(self, entry_with_two_repeat, in_one_day):
        assert entry_with_two_repeat.next_repetition == in_one_day
