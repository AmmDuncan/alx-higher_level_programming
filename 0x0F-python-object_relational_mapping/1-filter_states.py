#!/usr/bin/python3
"""
    select all states in the states table where
    name starts with 'N'
"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    host = 'localhost'
    port = 3306
    [_, user, password, db_name] = sys.argv

    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute('''
                SELECT id, name
                FROM states
                WHERE name LIKE 'N%'
                ORDER BY id;
                ''')
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
