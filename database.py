import sqlite3
from typing import ParamSpecArgs
from user_input import *

# establish a connection to a .db file and create a cursor object
con = sqlite3.connect('data.db')
cur = con.cursor()

# create initial tables
cur.execute("CREATE TABLE IF NOT EXISTS TIMESTAMPS (session_id INTEGER PRIMARY KEY, time_in STRING, time_out STRING, name STRING, purpose STRING);")
cur.execute("CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY, name STRING, cumulative_hours INTEGER);")

# declare and insert some initial values
timestamp_list = [
    (1, '1pm', 'null', 'Mikayla', 'work on project'),
    (2, '9pm', '11pm', 'not Mikayla', 'work on project'),
    (3, '8am', '5pm', 'someone else', 'debugging')
]

cur.executemany("INSERT INTO TIMESTAMPS VALUES (?, ?, ?, ?, ?)", timestamp_list)


"""

# The below logic for testing initial values are inserted,
# are able to be queried,
# and are accurately represented in the table.

# query table below:
table_rows = []
for row in cur.execute("SELECT * FROM TIMESTAMPS;"):
    # print each result
    print(row)
    # store each result individually in the list above
    table_rows.append(row)

# find COUNT(*) for the table
print(len(table_rows))

"""

# Functions to define:
# 1) Select all timestamps
# 2) Find a timestamp by date range
# 3) Calculate total hours for the week
# 4) Calculate complete sum of hours

def get_all_stamps():
    pass

def get_stamp_by_date():
    pass

def get_weekly_hours():
    pass

def get_all_hours():
    pass
