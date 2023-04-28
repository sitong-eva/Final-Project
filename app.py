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


# Define route for serving static files


# @app.route("/love_reading/")
# def love_get():
#     return render_template("love_reading_result.html")


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
        # print(career_result)
        return render_template(
            "career_reading_result.html", career_result=career_result
        )
    except:
        return render_template("error.html")


@app.route("/general_reading/", methods=["GET"])
def general_get():
    try:
        general_result = answer("yearly forecast")
        # print(general_result)
        return render_template(
            "general_reading_result.html", general_result=general_result
        )
    except:
        return render_template("error.html")


@app.route("/horoscope/", methods=["GET"])
def horoscope_get():
    try:
        # general_result = answer("yearly forecast")
        # print(general_result)
        return render_template("horoscope_landing.html")
    except:
        return render_template("error.html")


@app.route('/horoscope_reading', methods=['POST'])
def horoscope_reading():
    month = request.form['birth-month']
    day = request.form['birth-day']
    print(month)
    h = horoscope_yay(month, day)
    return render_template("horoscope_result.html", horoscope_result=h)

# def horoscope():
#     if request.method == "POST":
#         dob_str=request.json['dob']
#         dob = datetime.strptime(dob_str, '%Y-%m-%d')
#         month = dob.month
#         day = dob.day
#         print(month)
#         print(day)
#         horoscope_return=horoscope_yay(month,day)
#         print(horoscope_return)
#         return render_template("horoscope_result.html",horoscope_result=horoscope_return)


if __name__ == "__main__":
    app.run(debug=True)
