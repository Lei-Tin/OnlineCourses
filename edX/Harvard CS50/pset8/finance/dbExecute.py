from cs50 import SQL
from datetime import datetime

db = SQL("sqlite:///finance.db")

# user_id = db.execute("SELECT id FROM users WHERE username = 123")

# print(user_id[0]["id"])

# rows = db.execute("SELECT username FROM users")


# for row in rows:
#     if "123" in row["username"]:
#         print("Found")


# print(row)

# symbol = "GOOG"

# output = db.execute("SELECT * FROM stocks WHERE symbol = ? AND user_id = ?", symbol, 10)

# print(output)

# if output == []:
#     print("GOOD")

symbol = "AAPL"
name = "Apple Inc"
shares = 1
price = 131.97
now = datetime.now()

db.execute("INSERT INTO log (user_id, symbol, name, shares, price, total, transactionTime, transactionType) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            10, symbol, name, -shares, -price, -price * int(shares), now.strftime("%d/%m/%Y %H:%M:%S"), "sell")