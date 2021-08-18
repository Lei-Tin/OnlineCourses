from cs50 import SQL

db = SQL("sqlite:///messages.db")

messages = db.execute("SELECT * FROM message ORDER BY date DESC")


for message in messages:
    print(message["name"])
    print(message["message"])
    print(message["date"])