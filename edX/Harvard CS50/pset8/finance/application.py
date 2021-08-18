import os
from datetime import datetime

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session, flash
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# https://stackoverflow.com/questions/37532286/flask-flash-not-working-after-redirect, solving flashes after redirect
class TestConfig:
    DEBUG = True
    SERVER_NAME = 'project-username.c9users.io'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

    cashRemaining = round(row[0]["cash"], 2)

    stocks = db.execute("SELECT * FROM stocks WHERE user_id = ?", session["user_id"])

    # Total Sum of everything in this quick for loop
    totalSum = cashRemaining
    for row in stocks:
        if row["shares"] != None and row["symbol"] != None:
            # Updating the row price whenever it's needed

            row["price"] = lookup(row["symbol"])["price"]

            totalSum += row["price"] * row["shares"]

    # Output to index.html with everything turned into USD
    return render_template("index.html", cashRemaining = usd(cashRemaining), totalSum = usd(totalSum), stocks = stocks)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cashRemaining = round(row[0]["cash"], 2)

    if request.method == "GET":
        return render_template("buy.html", cashRemaining = usd(cashRemaining))

    elif request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if symbol == None:
            flash('Please input symbol', 'error')
            return render_template("buy.html", cashRemaining = usd(cashRemaining))
        elif shares == "":
            flash('Please input shares!', 'error')
            return render_template("buy.html", cashRemaining = usd(cashRemaining))
        elif lookup(symbol) == None:
            flash('The symbol is invalid!', 'error')
            return render_template("buy.html", cashRemaining = usd(cashRemaining))

        name = lookup(symbol)["name"]
        price = lookup(symbol)["price"]

        cashRemaining = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        if (cashRemaining[0]['cash'] - (int(shares) * price)) > 0:
            if db.execute("SELECT * FROM stocks WHERE symbol = ? AND user_id = ?", symbol.upper(), session["user_id"]) == []:
                db.execute("INSERT INTO stocks (user_id, symbol, name, shares, price, total) VALUES (?, ?, ?, ?, ?, ?)", session["user_id"], symbol.upper(), name, shares, price, price * int(shares))

            else:
                db.execute("UPDATE stocks SET shares = shares + ? WHERE symbol = ? and user_id = ?", shares, symbol.upper(), session["user_id"])
        else:
            flash("You do not have enough money!", 'error')
            return render_template("buy.html", cashRemaining = usd(cashRemaining))

        # Getting time right now https://www.programiz.com/python-programming/datetime/current-datetime.
        # Logging the transaction into my log table, which records all of these, that will not be updated.
        now = datetime.now()
        db.execute("INSERT INTO log (user_id, symbol, name, shares, price, total, transactionTime, transactionType) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    session["user_id"], symbol.upper(), name, shares, price, price * int(shares), now.strftime("%d/%m/%Y %H:%M:%S"), "Buy")

        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", price * int(shares), session["user_id"])

        if shares == 1:
            flash(f"Bought {shares} share of {name}!", 'success')
            return redirect("/")
        else:
            flash(f"Bought {shares} shares of {name}!", 'success')
            return redirect("/")

@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():
    """Changes the amount of cash you have at the moment"""

    row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cashRemaining = round(row[0]["cash"], 2)

    if request.method == "POST":

        operation = request.form.get("operation")
        value = request.form.get("value")

        if operation == "Add":
            db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", value, session["user_id"])

        elif operation == "Subtract":
            if float(value) > db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]:
                flash("You do not have that much money to deduct!", 'error')
                return render_template("cash.html", cashRemaining = usd(cashRemaining))
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", value, session["user_id"])

        flash("Operation successful", 'success')

        row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        cashRemaining = round(row[0]["cash"], 2)

        return render_template("cash.html", cashRemaining = usd(cashRemaining))

    elif request.method == "GET":
        return render_template("cash.html", cashRemaining = usd(cashRemaining))


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cashRemaining = round(row[0]["cash"], 2)

    log = db.execute("SELECT * FROM log WHERE user_id = ? ORDER BY transactionTime DESC", session["user_id"])

    # Pass in log to log for the for loop inside the HTML file, where it loops through the whole database to display the action taken.
    return render_template("history.html", log = log, cashRemaining = usd(cashRemaining))

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id if logged in, https://cs50.stackexchange.com/questions/28742/pset7-flash-message-does-not-show-on-redirect
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash('Please input username!', 'error')
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash('Please input password!', 'error')
            return render_template("login.html")


        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash('Invalid username and/or password!', 'error')

            return render_template("login.html")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash('You were successfully logged in', 'success')
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    flash("Successfully logged out!", 'success')
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cashRemaining = round(row[0]["cash"], 2)

    if request.method == "GET":
        return render_template("quote.html", mode = "get", cashRemaining = usd(cashRemaining))

    elif request.method == "POST":

        checkSymbol = request.form.get("symbol")

        if not checkSymbol:
            flash("Please input a symbol!", 'error')
            return render_template("quote.html", mode = "get", cashRemaining = usd(cashRemaining))

        # Redirect to the quote page, because lookup the typed in symbol doesn't exist
        if lookup(checkSymbol) == None:
            flash("The stock you are looking for doesn't exist!", 'error')
            return render_template("quote.html", mode = "get", cashRemaining = usd(cashRemaining))

        name = lookup(checkSymbol)["name"]
        symbol = lookup(checkSymbol)["symbol"]
        price = lookup(checkSymbol)["price"]

        flash("Quoting successful!", 'success')
        return render_template("quote.html", mode = "post", name = name, symbol = symbol, price = price, cashRemaining = usd(cashRemaining))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        #Username check
        usernameCheck = db.execute("SELECT username FROM users")

        # Ensure username was submitted
        if not request.form.get("username"):
            flash('Please input username!', 'error')
            return render_template("register.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash('Please input password!', 'error')
            return render_template("register.html")

        elif request.form.get("password") != request.form.get("passwordConfirm"):
            flash('Passwords do not match!', 'error')
            return render_template("register.html")

        for row in usernameCheck:
            if request.form.get("username") == row["username"]:
                flash('Username taken!', 'error')
                return render_template("register.html")

        username = request.form.get("username")
        pwdHash = generate_password_hash(request.form.get("password"))
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, pwdHash)

        # user_id = db.execute("SELECT id FROM users WHERE username = ?", username)
        # db.execute("INSERT INTO stocks (user_id) VALUES (?)", user_id[0]["id"])



        # Redirect user to home page
        flash('Registration successful', 'success')
        return redirect("/login")


    elif request.method == "GET":
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    cashRemaining = round(row[0]["cash"], 2)

    stocks = db.execute("SELECT symbol FROM stocks WHERE user_id = ?", session["user_id"])

    if request.method == "GET":
        return render_template("sell.html", stocks = stocks, cashRemaining = usd(cashRemaining))

    elif request.method == "POST":

        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        if symbol == None:
            flash("You did not choose a share to sell", 'error')
            return render_template("sell.html", stocks = stocks, cashRemaining = usd(cashRemaining))
        elif shares == "":
            flash("Please input amount of shares!", 'error')
            return render_template("sell.html", stocks = stocks, cashRemaining = usd(cashRemaining))

        name = lookup(symbol)["name"]
        price = lookup(symbol)["price"]

        stockChosen = db.execute("SELECT * FROM stocks WHERE user_id = ? AND symbol = ?", session["user_id"], symbol.upper())

        if int(shares) > stockChosen[0]["shares"]:
            flash("You do not have enough shares to be sold!", 'error')
            return render_template("sell.html", stocks = stocks, cashRemaining = usd(cashRemaining))

        db.execute("UPDATE stocks SET shares = shares - ?, price = ? WHERE user_id = ? AND symbol = ?", shares, price, session["user_id"], symbol.upper())

        stockChosen = db.execute("SELECT * FROM stocks WHERE user_id = ? AND symbol = ?", session["user_id"], symbol.upper())

        if stockChosen[0]["shares"] == 0:
            db.execute("DELETE FROM stocks WHERE symbol = ?", symbol.upper())

        now = datetime.now()
        db.execute("INSERT INTO log (user_id, symbol, name, shares, price, total, transactionTime, transactionType) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    session["user_id"], symbol.upper(), name, int(shares), price, price * int(shares), now.strftime("%d/%m/%Y %H:%M:%S"), "Sell")

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", price * int(shares), session["user_id"])

        if shares == 1:
            flash(f"{shares} share sold!",'success')
        else:
            flash(f"{shares} shares sold!",'success')
        return redirect("/")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
