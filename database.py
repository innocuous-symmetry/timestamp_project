import sqlite3
from user_input import *
from datetime import datetime

# establish a connection to a .db file and create a cursor object
con = sqlite3.connect('data.db')
cur = con.cursor()

# create initial tables
cur.execute("CREATE TABLE IF NOT EXISTS TIMESTAMPS (session_id INTEGER PRIMARY KEY, time_in STRING, time_out STRING, name STRING, purpose STRING);")
cur.execute("CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY, name STRING, cumulative_hours INTEGER);")

# declare and insert some initial values
timestamp_list = [
    ('Mikayla', 'work on project'),
    ('not Mikayla', 'work on project'),
    ('someone else', 'debugging')
]

cur.executemany("INSERT INTO TIMESTAMPS (name, purpose) VALUES (?, ?)", timestamp_list)
con.commit()

# Functions to define:
# 1) Select all timestamps
# 2) Find a timestamp by date range
# 3) Calculate total hours for the week
# 4) Calculate complete sum of hours

def create_new_stamp(timestamp, name, purpose):
    to_insert = (timestamp, name, purpose)
    cur.execute("INSERT INTO TIMESTAMPS (time_in, name, purpose) VALUES (?, ?, ?)", to_insert)
    con.commit()

def get_all_stamps():
    return cur.execute("SELECT * FROM TIMESTAMPS;")


def get_number_of_stamps(input):
    table_rows = []
    for row in cur.execute("SELECT * FROM TIMESTAMPS;"):
        table_rows.append(row)

    return table_rows[:input]


def get_table_length():
    table_rows = []
    for row in cur.execute("SELECT * FROM TIMESTAMPS;"):
        table_rows.append(row)
    return len(table_rows)


def get_stamp_by_date():
    pass

def get_weekly_hours():
    pass

def get_all_hours():
    pass


def delete_all_rows():
    cur.executemany("DELETE * FROM TIMESTAMPS;")