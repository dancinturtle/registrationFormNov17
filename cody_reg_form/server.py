from flask import Flask, request, flash, redirect, url_for, render_template
from datetime import datetime
import re

app = Flask(__name__)
app.secret_key = "RUBYISBETTER<3"

# Valid email constant/regex
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Root
@app.route('/')
def index():
  return render_template('index.html')

# Success page after submit
@app.route('/welcome')
def welcome():
  return render_template('welcome.html')

# Form submit
@app.route('/process', methods=['POST'])
def process():
  # Initialize variables for easy comparisons
  reg_form = request.form
  email_address = reg_form['email_address']
  first_name = reg_form['first_name']
  last_name = reg_form['last_name']
  password = reg_form['password']
  password_confirmation = reg_form['password_confirmation']

  # Push all errors into list to display after end of validations.
  errors = []

  # Can't be blank.
  # Loop through all attributes and capitalize/format name.
  for key in reg_form:
    if len(reg_form[key]) < 1:
      errors.append("{} can't be blank.".format(key.replace("_", " ")).capitalize())

  # Valid email
  if not EMAIL_REGEX.match(email_address):
    errors.append("Email address is invalid.")

  # Validate password
  # Must be at least 8 characters.
  if len(password) <= 8:
    errors.append("Passwords must be at least 8 characters long.")

  # Must match confirmation.
  if password != password_confirmation:
    errors.append("Passwords don't match.")

  # Must contain one upper case and one numberical character.
  if not any(char.isupper() for char in password) or not any(char.isdigit() for char in password):
    errors.append("Password must contain at least one upper case letter and one number.")

  # First/last name must not include any numbers.
  if not first_name.isalpha():
    errors.append("First name can't contain numbers.")

  if not last_name.isalpha():
    errors.append("Last name can't contain numbers.")

  # Ensure validate date format.
  try:
    birthday = datetime.strptime(reg_form['birthday'], "%m/%d/%Y").date()
    if birthday > datetime.date(datetime.now()):
      errors.append("Birthday can't be in the future.")
  except ValueError:
    errors.append("Birthday format is invalid.")

  # If there are any errors in the list, then redirect back to the index and display flash messages.
  # If there are no errors then redirect to the welcome/success page.
  if len(errors) > 0:
    # Sort errors alphabeticaly.
    errors.sort()
    # Create a new flash message for each error in the list.
    # In the view we loop through all flash messages to display.
    for message in errors:
      flash(message, 'error')
    return redirect(url_for('index'))
  else:
    flash("Success! Thanks for completing the survey!", 'success')
    return redirect(url_for('welcome'))

app.run(debug=True)
