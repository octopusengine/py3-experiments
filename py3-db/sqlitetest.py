#!/usr/bin/env python
import sqlite3

conn=sqlite3.connect('iradio.db')
curs=conn.cursor()

print("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM iradio"):
    print(row)

print("\nDatabase entries for the jazz:\n")
for row in curs.execute("SELECT link FROM iradio WHERE notice='jazz'"):
    print(row)

conn.close()
