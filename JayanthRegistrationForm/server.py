from flask import Flask, render_template, request, redirect, session, flash
import re
app = Flask(__name__)
app.secret_key="codingDojo"

NAME = re.compile(r'^[a-zA-z]+$')
EMAIL = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$')

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/submit', methods=['POST'])
def show_info():
    #check if all entries are good based on verification requirements above in re.compile
    status = formIsValid(request.form)
    print status
    # show if submits is accepted or needs to be resubmited. Show error through flash
    if (status['isValid']):
        print "success"
        return redirect('/success')
    
    else:
        print "error"
        for error in status['errors']:
            flash(error)
        return redirect('/')

@app.route('/success')
def success():
    return "Success"
    #check each form field is valid entry values
def formIsValid(client):
    errors=[]
    isValid=True
    if len(client['firstName'])<1:
        errors.append("Enter your first name")
        isValid = False

    if len(client['lastName'])<1:
        errors.append("Enter your last name")
        isValid = False

    if len(client['email'])<1:
        errors.append("Enter an email")
        isValid = False

    if len(client['pw'])<1:
        errors.append("Enter a password")
        isValid = False

    if len(client['confirm_pw'])<1:
        errors.append("Confirm your password")
        isValid = False

    if not re.match(NAME, client['firstName']) and not re.match(NAME, client['lastName']):
        errors.append("Names can only include letters")
        isValid=False

    if not re.match(EMAIL, client['email']):
        errors.append("You did not enter a valid Email address")
        isValid = False

    if client['pw'] != client['confirm_pw']:
        errors.append("Your passwords do not match")
        isValid = False

    if not re.match(PASSWORD, client['pw']):
        errors.append("Passwords must include one uppercase letter and one number")
        isValid = False

    return {"isValid":isValid, "errors":errors}

app.run(debug=True)