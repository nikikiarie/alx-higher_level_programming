#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""


import sys
import MySQLdb as mysql


if __name__ == '__main__':
    db = mysql.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    db.close()
