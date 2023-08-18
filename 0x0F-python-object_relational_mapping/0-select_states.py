#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

username: str = sys.argv[1]
password: str = sys.argv[2]
db_name: str = sys.argv[3]

db = MySQLdb.connect(user=username, password=password, database=db_name)
cursor = db.cursor()

cursor.execute(
    """
    SELECT * FROM states ORDER BY id
    """
)

rows = cursor.fetchall()

[print(row) for row in rows]
