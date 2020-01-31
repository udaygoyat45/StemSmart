from flask import request, redirect, render_template, url_for, flash
from flaskapp import db, app
from flaskapp.forms import RegistrationForm
from flaskapp.models import Email

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/sign", methods=['POST', 'GET'])
def sign():
    form = RegistrationForm()
    if form.validate_on_submit():
        newEmail = Email(email=form.email.data)
        db.session.add(newEmail)
        db.session.commit()

        flash("Thanks for registering")
        return render_template("home.html")

    return render_template("sign.html", form=form)
