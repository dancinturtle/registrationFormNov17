from flask import Flask, render_template, request, redirect, session, flash, url_for
import re
from flask_validator import ValidateInteger, ValidateString, ValidateEmail
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
#firstName = request.form['firstName']
#lastName = request.form['lastName']
#email = request.form['email']
#password = request.form['password']
#confirmPassword = request.form['confirmPassword']

def validation():
	error = False
	if len(request.form['firstName']) < 1:
		flash("First Name cannot be empty!") 
		error = True
	elif not request.form['firstName'].isalpha():
        flash('First name cannot have numbers!', 'wrong')
        error = True
	if len(request.form['lastName']) < 1:
		flash("Last Name cannot be empty!")
		error = True
	elif not request.form['lastName'].isalpha():
        flash('Last name cannot have numbers!', 'wrong')
        error = True
	if len(request.form['email']) < 1:
		flash("Email cannot be empty!")
		error = True
	elif not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email format!', 'wrong')
        error = True
	if len(request.form['password']) < 1:
		flash("Password cannot be empty!")
		error = True
	if len(request.form['password']) < 8:
        flash('Password must contain at least 6 characters!', 'wrong')
        error = True
	if len(request.form['confirmPassword']) < 1:
		flash("Confirm Password cannot be empty!")
		error = True
	if request.form['password'] != request.form['confirmPassword']:
        flash('Password does not match!', 'wrong')
        error = True

	if error == True:
		return redirect('/')

	if error = False:
		flash('Success!', 'success')
    	return render_template('result.html')

@app.route('/create', methods=['POST'])
def reset():
    return redirect('/')
  	
  	'''def __declare_last__(cls):
  	  	  	        	ValidateString(request.form['firstName'])
  	  	  	        	ValidateString(request.form['lastName'])               
  	  	  	        	ValidateEmail(request.form['email'])'''
		#flash("Success! Your name is {}".format(request.form['name']))
    		#session['firstName'] = request.form['firstName']
    		#session['lastName'] = request.form['lastName']
    		#return render_template('result.html')

app.run(debug=True)
  