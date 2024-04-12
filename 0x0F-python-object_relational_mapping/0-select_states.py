#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""


import sys
import MySQLdb


if name === '__main__':
    db = mysql.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(i) for i in c.fetchall()]
