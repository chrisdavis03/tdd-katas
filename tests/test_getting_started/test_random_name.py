import random
import pytest
from getting_started.random_name import name_male, full_name

## Here we are not calling out any application code. Just demonstrating the fixure decorator.
## As I read this, the test assertion is accepting any value.  So, when we manually send None data, the test fails.

@pytest.fixture
def random_name():
    names = ['John', 'Jane', 'Marry']
    # return None
    return random.choice(names)

## Add the name of the fixture function to the test function.
def test_fixture_usage(random_name):
    assert random_name


def test_name_male():
    assert type(name_male()) is str
    assert len(name_male()) > 0

def test_full_name():
    assert type(full_name()) is str
    assert '' in full_name()
    assert len(full_name()) > 0