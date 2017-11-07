from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
  return render_template('index.html')
@app.route('/process', methods=['POST'])
def register():
    is_valid = True
    #email validations
    if len(request.form["email"]) == 0:
        flash("Email field cannot be empty")
        is_valid = False
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email format")
        is_valid = False

    #first name validations
    if len(request.form["fname"]) < 0:
        flash("First name cannot be empty")
        is_valid = False
    elif not request.form["fname"].isalpha():
        flash("Invalid first name format")
        is_valid = False
    
    #last name validations
    if len(request.form["lname"]) < 0:
        flash("Last name cannot be empty")
        is_valid = False
    elif not request.form["lname"].isalpha():
        flash("Invalid last name format")
        is_valid = False

    #password validations
    if len(request.form["pword"]) < 8:
        flash("Password must be at least 8 characters long")
        is_valid = False
    elif request.form["pword"] != request.form["confirm"]:
        flash("Passwords do not match")
        is_valid = False

    if is_valid:
        flash("Thanks for submitting your information.")

    return redirect('/')
app.run(debug=True)