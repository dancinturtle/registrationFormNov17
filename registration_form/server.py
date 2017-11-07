from flask import Flask, render_template, redirect, request, session, flash
import re

regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
number = re.compile(r'^[0-9]+$')
app = Flask(__name__)
app.secret_key = 'snowfallen'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=['POST'])
def form():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    session['confirm_password'] = request.form['confirm_password']
    if len(session['first_name']) == 0:
        flash("first name is required")
    elif number.match(session['first_name']):
        flash("Oops! Your first name cannot contain numbers")
    elif len(session['last_name']) == 0:
        flash("last name is required")
    elif number.match(session['last_name']):
        flash("Oops! Your last name cannot contain numbers")
    elif not regex.match(session['email']):
        flash("valid email is required")
    elif len(session['password']) < 3:
        flash("password must be at least 3 characters long")
    elif session['password'] != session['confirm_password']:
        flash("passwords do not match!")
    else:
        flash("Thank you for submitting your information.")
    return redirect("/")

app.run(debug=True)