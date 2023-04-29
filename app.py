from flask import Flask, render_template, request
from tarot_helper import answer
from horoscope_helper import horoscope_yay
import os
import json
from datetime import datetime

app = Flask(__name__, static_folder="assets")


@app.route("/")
def hello():
    return render_template("home.html")


@app.route("/love_reading/", methods=["GET"])
def love_get():
    try:
        love_result = answer("love")
        # print(love_result)
        return render_template("love_reading_result.html", love_result=love_result)
    except:
        return render_template("error.html")


@app.route("/career_reading/", methods=["GET"])
def career_get():
    try:
        career_result = answer("career")
        return render_template(
            "career_reading_result.html", career_result=career_result
        )
    except:
        return render_template("error.html")


@app.route("/general_reading/", methods=["GET"])
def general_get():
    try:
        general_result = answer("yearly forecast")
        return render_template(
            "general_reading_result.html", general_result=general_result
        )
    except:
        return render_template("error.html")


@app.route("/horoscope/", methods=["GET"])
def horoscope_get():
    try:
        return render_template("horoscope_landing.html")
    except:
        return render_template("error.html")


@app.route('/horoscope_reading', methods=['POST'])
def horoscope_reading():
    month = request.form['birth-month']
    day = request.form['birth-day']
    print(day)
    h = horoscope_yay(month, day)
    return render_template("horoscope_result.html", horoscope_result=h)


if __name__ == "__main__":
    app.run(debug=True)
