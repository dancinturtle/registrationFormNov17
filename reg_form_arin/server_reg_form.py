from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "00gieB00g!e"


def has_upper_num(password):
    #checks if the entered password meets our requirements
    has_upper = False
    has_num = False
    check = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_num = True

    if has_num and has_upper:
        check = True

    return check


@app.route('/')
def index():
  return render_template("reg_form.html")


@app.route('/result', methods=['POST'])
def create_user():
    import time
    import datetime
    print "Got Post Info"
    print request.form

    datetime.datetime.now().strftime("%Y-%m-%d")

    f_name = str(request.form['f_name'])
    l_name = str(request.form['l_name'])
    email = str(request.form['email'])
    pwd = str(request.form['pwd'])
    pwd_c = str(request.form['pwd_c'])
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    bday = request.form['bday']

    for thing in request.form:
        if len(request.form[thing]) < 1:
            flash('All fields required')
            return redirect('/')

    if not NAME_REGEX.match(request.form['f_name']) or not NAME_REGEX.match(request.form['l_name']):
        flash("Names must only contain letters")
        return redirect('/')

    if bday >= today:
        flash("Birthdate invalid, must be before today.")
        return redirect('/')

    if not EMAIL_REGEX.match(request.form['email']):
        flash("Not a valid email address")
        return redirect('/')

    if len(pwd) < 8:
        flash("Password must be at least 8 characters.")
        return redirect('/')

    if not has_upper_num(pwd):
        flash('Password must contain at least one uppercase letter and one number')
        return redirect('/')

    if pwd != pwd_c:
        flash("Passwords must match")
        return redirect('/')

    return render_template('reg_results.html')

app.run(debug=True)
