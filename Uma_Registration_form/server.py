from flask import Flask, render_template, request, session, redirect, flash
import re
from datetime import datetime
app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = '123123'
@app.route('/')
def index():
  return render_template("form.html")

@app.route('/process', methods=['GET', 'POST'])
def process():
   email = request.form['email']
   fname = request.form['fname']
   lname = request.form['lname']
   bday = request.form['bday']
   password = request.form['password']
   cnrfmPassword = request.form['cnrfmPassword']
   flag = True
   EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
   if len(email) < 1:
   	flag = False
   	flash('Email cannot be empty', 'error') 
   elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")

   if len(fname) < 1:
   	flag = False
   	flash('First Name cannot be empty', 'error')
   elif any(char.isdigit() for char in fname) == True:
   	flag = False
   	flash('First Name cannot have numbers', 'error')

   if len(lname) < 1:
   	flag = False
   	flash('Last Name cannot be empty', 'error')
   elif any(char.isdigit() for char in lname) == True:
   	flag = False
   	flash('Last Name cannot have numbers', 'error')

   if len(bday) < 1:
      flag = False
      flash('Birthday cannot be empty', 'error')
   elif:
      bday = datetime.strptime(bday, '%Y-%m-%d')
      if(bday >= datetime.now()):
         flag = False
         flash('Birthday has to be less than today')
   
   if len(password) < 9 and len(cnrfmPassword) < 9 :
   	flag = False
   	flash('Password and Confirm Password should be more than 8 characters and match', 'error')
   elif len(password) < 9:
   	flag = False
   	flash('Password and Confirm Password should be more than 8 characters', 'error')
   elif len(cnrfmPassword) < 9:
   	flag = False
   	flash('Password and Confirm Password should be more than 8 characters', 'error')
   elif cnrfmPassword != password:
   	flag = False
   	flash('Password and Confirm Password should match', 'error')

   if flag:
   	flash('Thanks for submitting your information.', 'success')
   return redirect('/')
app.run(debug=True)


   