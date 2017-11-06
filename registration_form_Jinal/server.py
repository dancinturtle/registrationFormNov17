from flask import Flask, redirect, render_template, session, request,flash
import re
from datetime import datetime

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z][\sa-zA-Z]*$') #https://stackoverflow.com/questions/290449/how-do-i-disallow-numbers-in-a-regular-expression
PWD_REGEX = re.compile(r'^(?=.*?[A-Z]).*\d') #https://stackoverflow.com/questions/33588441/python-regex-password-must-contain-at-least-one-uppercase-letter-and-number
app = Flask(__name__)
app.secret_key = 'SecretKeepItSafe'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print request.form    
    error = False
    email_id = request.form['email']
    fname = request.form['fname']
    lname = request.form['lname']
    passwrd = request.form['password']
    confirm_pwd = request.form['confirm']
    bday = request.form['bday']
    
    bday = datetime.strptime(bday,"%Y-%m-%d")
    CurrentDate = datetime.now()
 
    if email_id == "" or fname =="" or lname=="" or passwrd =="" or confirm_pwd =="":
        error = True
        flash("All fields are required and must not be blank")
    else:
        if fname != "":
            if not NAME_REGEX.match(fname):
                error = True
                flash("Invalid first name ("+fname+") cannot have number ")
        if lname != "":
            if not NAME_REGEX.match(lname):
                error = True
                flash("Invalid last name ("+lname+") cannot have number ")
        if email_id != "":
            if not EMAIL_REGEX.match(email_id):
                error = True
                flash("Invalid Email Address! please follow abc@xyz.com")    
        if len(passwrd) < 8:
            error = True
            flash("Password should be more than 8 characters")
        elif not PWD_REGEX.match(passwrd):
            error = True
            flash("Invalid password! Password must contain atleast 1 Uppercase and 1 numeric value")    
        elif passwrd != confirm_pwd:
            error = True
            flash("Password and Password Confirmation are not matching")
        if bday > CurrentDate:
            error = True
            flash("Please enter valid date")
    
    if error:
        return redirect('/')
    else:
        return render_template('confirm.html',fname=fname, lname=lname, email_id=email_id, bday=bday)

@app.route('/reset')
def reset():
    return redirect('/')
app.run(debug='True')
