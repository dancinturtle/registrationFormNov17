#NOTE: please remember to refactor my code if it works

from flask import Flask, render_template, redirect, request, session, flash
import re, time, datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASS_REGEX = re.compile(r'^.(?=.[a-z])(?=.[A-Z])(?=.[\d\W]).*$')
DOB_REGEX = re.compile(r'^.(\b\d{1,2}[-/:]\d{1,2}[-/:]\d{4}\b)')
app=Flask(__name__)
app.secret_key='SeriouslySecret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/new', methods=['POST'])
def new():
	email_address = request.form['email']
	fname = request.form['first_name']
	lname = request.form['last_name']
	password = request.form['password']
	password_confirmation = request.form['confirmpass']

	# check for blanks
	if len(email_address) < 1 or len(fname) < 1 or len(lname) < 1 or len(password) < 1 or len(password_confirmation) < 1:
		flash('Please ensure you fill all the fields')
	elif len(password) < 8 or len(password_confirmation) < 8:
		# Ensure password length
		flash('provide a password with 8 characters or longer')
	elif not EMAIL_REGEX.match(email_address):
		# Email is valid
		flash('Ops ! Invalid email address!')
	elif not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
		# Alphanumeric password
		flash('Password must contain at least 1 uppercase letter and 1 number.')
	elif fname.isalpha() == False or lname.isalpha() == False:
		# Ensure name cant include digits
		flash('Name cannot contain numbers!')
	elif password_confirmation != password:
		# Confirm passwords match
		flash('Passwords do not match!')
	else:
		flash('Successfully registered!')
	return redirect('/')

app.run(debug=True)


