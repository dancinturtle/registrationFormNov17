from flask import Flask, request, redirect, session, flash, render_template
import re


NAME_REGEX = re.compile(r'^[A-Z][-a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASS_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
app = Flask(__name__)
app.secret_key = "passwordisthis"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/results", methods=['POST'])
def process():
	if len(request.form['first_name']) < 1:
		flash("First name cannot be left blank")
	if len(request.form['last_name']) < 1:
		flash("Last name cannot be left blank")
	if len(request.form['email']) < 1:
		flash("Email cannot be left blank")
	if len(request.form['pass']) < 1:
		flash("Password cannot be left blank")
	if len(request.form['confirm']) < 1:
		flash("Confirm password please")
	if not NAME_REGEX.match(request.form['first_name']):
		flash("Invalid first name!")
	if not NAME_REGEX.match(request.form['last_name']):
		flash("Invalid last name!")
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address!")
	if not PASS_REGEX.match(request.form['pass']):
		flash("Password must be at least eight characters, contain at least one uppercase letter, contain at least one lowercase letter, contain at least one numeric value")
	if request.form['pass'] != request.form['confirm']:
		flash("Confirmation does not match password")

	return redirect("/")

app.run(debug=True)
