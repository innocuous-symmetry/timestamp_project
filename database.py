import sqlite3
from user_input import *
from datetime import datetime, timedelta

# establish a connection to a .db file and create a cursor object
con = sqlite3.connect('data.db')
cur = con.cursor()

# create initial tables
cur.execute("CREATE TABLE IF NOT EXISTS TIMESTAMPS (session_id INTEGER PRIMARY KEY, time_in STRING, time_out STRING, name STRING, purpose STRING);")
cur.execute("CREATE TABLE IF NOT EXISTS USERS (id INTEGER PRIMARY KEY, name STRING, cumulative_hours INTEGER);")

# Functions to define:
# 1) Select all timestamps
# 2) Find a timestamp by date range
# 3) Calculate total hours for the week
# 4) Calculate complete sum of hours

def get_created_id(timestamp):
    return cur.execute("SELECT * FROM TIMESTAMPS WHERE time_in=:stamp", {"stamp": timestamp})

def create_new_stamp(timestamp, name, purpose):
    to_insert = (timestamp, name, purpose)
    cur.execute("INSERT INTO TIMESTAMPS (time_in, name, purpose) VALUES (?, ?, ?)", to_insert)
    con.commit()

def punch_out(timestamp, id):
    data = (timestamp, id)
    cur.execute("""UPDATE TIMESTAMPS
                    SET time_out = ? 
                    WHERE session_id = ?
    """, data)
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

def get_weekly_hours():
    current_time = datetime.now()
    minus_week = current_time - timedelta(days = 7)
    
    return cur.execute("""
    SELECT time_in, time_out FROM TIMESTAMPS
    WHERE time_in>:minus_week
    """, {"minus_week": minus_week})

def get_all_hours():
    pass


def delete_all_rows():
    cur.execute("DELETE FROM TIMESTAMPS")
    con.commit()