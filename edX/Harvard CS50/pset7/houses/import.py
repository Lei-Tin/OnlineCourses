# TODO

from sys import argv
import csv
import cs50

if len(argv) != 2:
    print("Usage: python import.py {characters.csv}")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

# I ACTUALLY DON'T HAVE TO CREATE :C
# db.execute("CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, first VARCHAR(255), middle VARCHAR(255), last VARCHAR(255), house VARCHAR(10), birth INTEGER)")

with open(argv[1], "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        name = row['name'].split()

        first = name[0]
        if len(name) == 3:
            middle = name[1]
            last = name[2]
        else:
            middle = None
            last = name[1]

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                   first, middle, last, row['house'], row['birth'])

print("Import Successful")

exit(0)