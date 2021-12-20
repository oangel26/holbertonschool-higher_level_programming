#!/usr/bin/python3
"""
Script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    # Use de Python-DB API to connect to MySQL database server
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    # Cursor object which gives the ability to have multiple envirionments
    cur = db.cursor()

    # Obtaining query results with fetchall()
    cur.execute("SELECT * FROM states WHERE states.name  LIKE 'N%' \
    ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("({}, '{}')".format(row[0], row[1]))
