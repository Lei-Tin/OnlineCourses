# TODO

from sys import argv
import cs50

if len(argv) != 2:
    print("Usage: python roster.py {house}")
    exit(1)


open("students.db", "r")
db = cs50.SQL("sqlite:///students.db")

rows = db.execute("SELECT * FROM students WHERE house = ? ORDER BY LAST, FIRST", argv[1])

for row in rows:

    if row['middle'] == None:
        print(f"{row['first']} {row['last']}, born in {row['birth']}")
    else:
        print(f"{row['first']} {row['middle']} {row['last']}, born in {row['birth']}")