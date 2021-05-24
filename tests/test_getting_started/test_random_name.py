import random
import pytest

## Here we are not calling out any application code. Just demonstrating the fixure decorator.
## As I read this, the test assertion is accepting any value.  So, when we manually send None data, the test fails.

@pytest.fixture
def random_name():
    names = ['Jphn', 'Jane', 'Marry']
    # return None
    return random.choice(names)

## Add the name of the fixture function to the test function.
def test_fixture_usage(random_name):
    assert random_name

