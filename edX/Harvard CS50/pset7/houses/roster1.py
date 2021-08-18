# TODO
# Doesn't fulfill the check, redo in version 2
from sys import argv
import cs50

if len(argv) != 2:
    print("Usage: python roster.py {house}")
    exit(1)

open("students.db", "r")
db = cs50.SQL("sqlite:///students.db")

rows = db.execute(
    "SELECT name.firstName, name.middleName, name.lastName, house.house, house.birth FROM name JOIN house ON name.id = house.person_id WHERE house.house = ? ORDER BY name.lastName ASC, name.firstName ASC", argv[1])

for row in rows:
    if row["middleName"] == "NULL":
        print(row["firstName"], row["lastName"] + ", born in", row["birth"])
    else:
        print(row["firstName"], row["middleName"], row["lastName"] + ", born in", row["birth"])

exit(0)