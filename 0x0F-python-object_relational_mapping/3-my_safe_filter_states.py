#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""


import sys
import MySQLdb as mysql


if __name__ == '__main__':
    db = mysql.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE state.name=%s""", (sys.argv[4]))
    r = c.fetchall()
    temp = list(i[0] for i in rows)
    print(*temp, sep=", ")
    c.close()
    db.close()
