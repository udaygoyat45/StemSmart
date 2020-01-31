from flask import request, redirect, render_template, url_for, flash
from flaskapp import db, app
from flaskapp.forms import RegistrationForm

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/sign")
def sign():
    return render_template("sign.html")
