#!/usr/bin/python3
"""
    select all states in the states table where
    name matches provide argument
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute('''
                SELECT id, name
                FROM states
                WHERE CAST(name AS BINARY)
                LIKE CAST(%s AS BINARY)
                ORDER BY id;
                ''', (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
