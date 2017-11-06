from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+[a-zA-Z-]*[a-zA-Z]+$')
Password_REGEX = re.compile(r'^[a-zA-Z-]+[A-Z\d]+[a-zA-Z-]+$')


@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/login', methods=['POST'])
def submit():
    isform_valid= True
    isGoodForm =1
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        isform_valid= False
    # else if email doesn't match regular expression display an "invalid email address" message
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        isform_valid= False
    # check if name has 3 or more char 
    elif len(request.form['fname']) < 3:
        flash(" Name should have more than two characters")
        isform_valid= False
    # check if name matches regex
    elif not NAME_REGEX.match(request.form['fname']):
        flash("First Name cannot contain numbers!")
        isform_valid= False
    # check if name has 3 or more char 
    elif len(request.form['lname']) < 3:
        flash(" Name should have more than two characters")
        isform_valid= FALSE
    # check if name matches regex
    elif not NAME_REGEX.match(request.form['lname']):
        flash("Last Name cannot contain numbers!")
        isform_valid = False
    #Check length of pwd is >=8 
    elif len (request.form['password']) < 8:
        flash("password should be atleast 8 characters")
        isform_valid = False
    # check if password has one capital letter and one no
    elif not Password_REGEX.match(request.form['password']):
        flash("Password should have at least one capital letter and one digit")
        isform_valid = False 
    #Confirm typed pwd matches 
    elif not (request.form['password']) == (request.form['password_confirmation']):
        flash("password should match")
        isform_valid= False
    #Form is sans errors 
    else:
        if isform_valid:
            flash("Thanks for sumitting the correct information user!")
    fullname = request.form['fname'] + request.form['lname']
    # return render_template('success.html', name = fullname) 
    return redirect('/')

app.run(debug=True)

	
