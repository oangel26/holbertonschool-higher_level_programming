#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
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
    cur.execute("SELECT cities.name \
    FROM cities \
    LEFT JOIN states \
    ON cities.state_id = states.id \
    WHERE cities.state_id=(SELECT DISTINCT states.id FROM states \
    WHERE states.name=%s) \
    ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row[0]), end="")
        if (row != rows[-1]):
            print(end=", ")
    print()
