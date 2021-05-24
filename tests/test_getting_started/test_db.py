import pytest
from getting_started.user_service import list_users

#does the create_db fixture run? Should create a database.
def test_list_users():
    db_file='./tests/qa.db'
    ## Initially this test fails because the DB has no users.

    assert len(list_users()) > 0

