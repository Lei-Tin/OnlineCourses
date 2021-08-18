import os
import pytz

from pytz import timezone
from datetime import datetime
from flask import Flask, render_template, request, redirect, session
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///messages.db")

asian = 'Asia/Chongqing'

@app.route("/")
def index():

    now = datetime.now(pytz.utc)

    date = now.astimezone(timezone(asian)).strftime("%m/%d/%Y")

    db.execute("DELETE FROM message WHERE date != ?", date)

    messages = db.execute("SELECT * FROM message ORDER BY time DESC")

    return render_template("index.html", messages = messages)

@app.route("/send", methods = ["POST"])
def send():
    if request.method == "POST":

        now = datetime.now(pytz.utc)

        name = request.form.get("name")
        message = request.form.get("message")
        time = now.astimezone(timezone(asian)).strftime("%H:%M:%S")
        date = now.astimezone(timezone(asian)).strftime("%m/%d/%Y")

        db.execute("INSERT INTO message (name, message, time, date) VALUES (?, ?, ?, ?)", name, message, time, date)

        return redirect("/")