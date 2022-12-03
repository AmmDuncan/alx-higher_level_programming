#!/usr/bin/python3
"""
    select all cities in the cities table where
    state matches provided argument
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
                SELECT c.id, c.name
                FROM cities c
                JOIN states s ON s.id = c.state_id
                WHERE CAST(s.name AS BINARY)
                LIKE CAST('{}' AS BINARY)
                ORDER BY c.id;
                '''.format(sys.argv[4]))
    rows = cur.fetchall()
    cities = [*map(lambda v: v[1], rows)]
    print(", ".join(cities))

    cur.close()
    db.close()
