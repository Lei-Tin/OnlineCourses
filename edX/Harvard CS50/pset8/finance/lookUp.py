from helpers import apology, login_required, lookup, usd
from cs50 import SQL

# rows = lookup("AAPL")

# for row in rows:
#     print(rows["name"])


# print((lookup("AAPL"))["price"])

# result = lookup("")

# print(result)

db = SQL("sqlite:///finance.db")

symbol = "AAPL"

name = lookup(symbol)["name"]
price = lookup(symbol)["price"]

cashRemaining = db.execute("SELECT cash FROM users WHERE id = ?", 10)


print(cashRemaining[0]['cash'])