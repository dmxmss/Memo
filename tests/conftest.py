from src.lib import Entry
import pytest
import datetime

@pytest.fixture
def basic_time():
    return datetime.datetime(2008, 9, 10, 4)

@pytest.fixture
def basic_entry(basic_time):
    return Entry(name="test no repeat", date_created=basic_time)

@pytest.fixture
def entry_with_one_repeat(basic_time):
    return Entry(name="test one repeat", date_created=basic_time, amount_of_repetitions=1)

@pytest.fixture
def entry_with_two_repeat(basic_time):
    return Entry(name="test two repeats", date_created=basic_time, amount_of_repetitions=2)

@pytest.fixture
def in_one_hour(basic_time):
    return basic_time + datetime.timedelta(hours=1)

@pytest.fixture
def in_three_hours(basic_time):
    return basic_time + datetime.timedelta(hours=3)

@pytest.fixture
def in_one_day(basic_time):
    return basic_time + datetime.timedelta(days=1)
