from flask import Flask, render_template, request
from tarot_helper import answer
import os

app = Flask(__name__, static_folder="assets")


@app.route("/")
def hello():
    return render_template("home.html")


# Define route for serving static files


# @app.route("/love_reading/")
# def love_get():
#     return render_template("love_reading_result.html")


@app.route("/love_reading/", methods =['GET'])
def love_get():
    try:
        love_result = answer("love")
        print(love_result)
        return render_template("love_reading_result.html", love_result=love_result)
    except:
        return render_template("error.html")


if __name__ == "__main__":
    app.run(debug=True)
