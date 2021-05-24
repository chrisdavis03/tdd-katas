import sqlite3
from sqlite3 import Error


def list_users():
    db_file='./tests/qa.db'
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute('select * from user')
    users = cur.fetchall()
    conn.close()

    print (users)

    return users


if __name__ == '__main__':
    pass