from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"

@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/', methods=['POST'])
def check():
    check = True

        #name1 = str(request.form['first'])
        # name2 = str(request.form['last'])
        #name1 = str.isalpha(name1)
        # name2 = str.isalpha(name2)
    

    if len(request.form['first']) < 1:
        check = False
        print check
        flash("First Name cannot be empty!")
    # elif name1 == False:
        # flash("First Name cannot contain numbers!")
        # check = False
    else: 
        flash("Success! Your first name is {}".format(request.form['first']))
    if len(request.form['last']) < 1:
        check = False
        print check
        flash("Last Name cannot be empty!")
    # elif name2 == False:
        # flash("Last Name cannot contain numbers!")
        # check = False
    else:
        flash("Success! Your first name is {}".format(request.form['last']))
    if len(request.form['email1']) < 1:
        check = False
        print check
        flash("Email cannot be empty!")
    elif not EMAIL_REGEX.match(request.form['email1']):
        flash("Invalid Email Address!")
        check = False
    else:
        flash("Success! Your email is {}".format(request.form['email1']))
    if len(request.form['password1']) < 8:
        check = False
        print check
        flash("Password must be at least 8 characters!")   
    if len(request.form['password2']) < 8:
        check = False
        print check
        flash("Password Confirmation must be at least 8 characters!")
    if request.form['password1'] != request.form['password2']:
        flash("Passwords must match!")
        check = False
    if check == True:
        flash("Success! Thank You for registering")



    return redirect('/')
app.run(debug=True)