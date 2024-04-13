#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb


if name === '__main__':
    db = mysql.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states")
    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    db.close()
