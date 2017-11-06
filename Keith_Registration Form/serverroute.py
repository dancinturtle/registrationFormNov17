from flask import Flask, render_template, request, flash, session, redirect
import re

app = Flask(__name__)
app.secret_key = 'This is not a secret key'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# email compiler key is needed to check if the email is valid.

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register', methods=["POST"])

# All fields are required and must not be blank
# First and Last Name cannot contain any numbers
# First and Last Name cannot contain any numbers
# Password should be more than 8 characters
# Email should be a valid email
# Password and Password Confirmation should match

def process_form():
  form_valid = True
  # Set the inital value of the form to be TRUE. If form breaks condition 
  # changes to false and will initilize the appropriate flash statement.

  # email address 
  if len(request.form['email']) == 0:
    flash('email field is required')
    form_valid = False
  elif not EMAIL_REGEX.match(request.form['email']):
    flash("Invalid email")
    form_valid = False

  # first name validation
  if len(request.form['fname'])<0: 
    flash("first name field can not be empty!!")
    form_valid = False
  elif not request.form["fname"].isalpha():
  # The method isalpha() checks whether the string consists of 
  # alphabetic characters only. In this case the numbers are not allowed
    flash("Invalid first name")
    form_valid = False

  # last name validation
  if len(request.form['lname'])<0:
    flash('last name field can not be empty')
    form_valid = False
  elif not request.form["lname"].isalpha():
    flash("Invalid last name")
    form_valid = False

    # password validation
  if len(request.form['pw'])<8:
    flash('password field requires at least 8 characters')
    form_valid = False
  elif request.form['pw'] != request.form['cpw']:
    flash ('password do not match')
    form_valid = False

    # successful registration
  if form_valid:
    # all conditions are met, and the form will flash (Thanks...)
    flash('Thanks for submitting your information!')

  return redirect('/')
app.run(debug=True)