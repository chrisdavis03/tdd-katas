import pytest
import sqlite3
from sqlite3 import Error
import os

# Another option is to perform a side effect, like creating a database or mocking a module.
# You can also run part of a fixture before and part after a test using yield instead of return. For example:

@pytest.fixture
def some_fixture():
    # do something before your test
    yield # test runs here
    # do something after your test
    pass


#@pytest.fixture(autouse=True)
## The Autouse flag is set to true in order to ensure that it gets used for each test.  This way, we do not need to add
# the fixure function to our test functions explicitly.  If a database is used for each test, then we can create a fixture
#to create and connect the database before the tests run and destroy it afterward.

## Lets try this with SQLite3.
@pytest.fixture(autouse=True)
def create_db():
    db_file = './tests/qa.db'
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE user
                       (user_id int, user_first text, user_last, text)''')

        cur.execute('''INSERT INTO user (user_id, user_first, user_last)
                               VALUES (1, 'Chris', 'Davis')''')

        conn.commit()
    except Error as e:
        print (e)
    finally:
        if conn:
            conn.close()

    yield
    ## cleanup db after testing.
    os.remove(db_file)

