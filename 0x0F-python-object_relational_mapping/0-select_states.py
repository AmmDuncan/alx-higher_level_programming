#!/usr/bin/python3
import MySQLdb
import sys

host = 'localhost'
port = 3306
user = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

db = MySQLdb.connect(host=host,
                     port=port,
                     user=user,
                     passwd=password,
                     db=db_name)
cur = db.cursor()

cur.execute('SELECT id, name FROM states')
rows = cur.fetchall()
for row in rows:
    print(row)
