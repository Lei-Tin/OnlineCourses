# Wrong Approach, does the same work but doesn't fulfill the check, redo in version 2
from sys import argv
import csv
import cs50

if len(argv) != 2:
    print("Usage: python import.py {characters.csv}")
    exit(1)

open("students.db", "w").close()
db = cs50.SQL("sqlite:///students.db")

db.execute("CREATE TABLE house (person_id INTEGER, house TEXT, birth INTEGER)")
db.execute("CREATE TABLE name (id INTEGER, firstName TEXT, middleName TEXT, lastName TEXT)")

with open(argv[1], "r") as file:

    reader = csv.DictReader(file)

    for row in reader:

        key = hash(row["name"])

        db.execute("INSERT INTO house (person_id, house, birth) VALUES (?, ?, ?)", key, row["house"], row["birth"])

        row["name"] = row["name"].split(" ")

        if len(row["name"]) == 3:
            first_name = row["name"][0]
            middle_name = row["name"][1]
            last_name = row["name"][2]
        else:
            first_name = row["name"][0]
            middle_name = "NULL"
            last_name = row["name"][1]

        db.execute("INSERT INTO name (id, firstName, middleName, lastName) VALUES (?, ?, ?, ?)",
                   key, first_name, middle_name, last_name)

exit(0)