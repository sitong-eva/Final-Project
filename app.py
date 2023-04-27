from flask import Flask, render_template, request
from tarot_helper import answer
import os

app=Flask(__name__, static_folder='assets')

@app.route("/")
def hello():
    return render_template("home.html")

# Define route for serving static files

@app.route("/tarot/")
@app.get("/tarot/")
def tarot_get():
    return render_template("tarot_form.html")
@app.post("/tarot/")
def tarot_post():
    # try:
    # except:
    pass

if __name__=="__main__":
    app.run(debug=True)