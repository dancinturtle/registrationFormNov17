from flask import Flask, render_template, request, redirect, flash, session
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^([^0-9]*)$')

app=Flask(__name__)
app.secret_key='secrlksj'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/confirm', methods=['POST'])
def pass_data():
    fname= request.form['fname']
    lname= request.form['lname']
    email= request.form['email']
    psw= request.form['psw']
    psw2= request.form['psw2']
    #firstname
    if len(request.form['fname']) < 1:
        flash("First Name cannot be empty!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['fname']):
        flash("No numbers accepted in First Name!")
        return redirect('/')
    #lastname
    elif len(request.form['lname']) < 1:
        flash("Last Name cannot be empty!")
        return redirect('/')
    elif not NAME_REGEX.match(request.form['lname']):
        flash("No numbers accepted in Last Name!")
        return redirect('/')
    #email
    elif len(request.form['email']) < 1:
        flash("Email cannot be empty!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    #password
    elif len(request.form['psw']) < 1:
        flash("Pwd cannot be empty!")
        return redirect('/')
    elif len(request.form['psw']) < 8:
        flash("Password should be more than 8 characters")
        return redirect('/')
    #password2
    elif len(request.form['psw2']) < 1:
        flash("Pwd cannot be empty!")
        return redirect('/')
    elif request.form['psw2']!=request.form['psw']:
        flash("Pwd should match!")
        return redirect('/')

    
    return render_template('confirm.html')
    


app.run(debug=True)
