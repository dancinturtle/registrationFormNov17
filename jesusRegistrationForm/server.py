from flask import Flask,render_template, session,redirect,request,flash
import re
app = Flask(__name__)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = "ThisKeyIsSecretDoNotTOuchItORISwearIWillEatYourDOg"

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
def hasUpperAndNumber(inputString):
    hasNum = False
    hasUpper = False
    for char in inputString:
        if char.isupper():
            hasUpper=True
        elif char.isdigit():
            hasNum =True
    if hasNum and hasUpper:
        return True
    else:
        return False

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def registrationForm():
    errors = False
    eMail = request.form['email']
    firstName = request.form['fName']
    lastName = request.form['lName']
    passWord = request.form['pasw']
    confirmPassword = request.form['cPasw']
    #checking to make sure all fields are complete
    if len(eMail)<1 :
        flash("Please do Not Leave Your Email Blank")
        errors = True
    if len(firstName)<1:
        flash("Please do Not Leave Your First Name Blank")
        errors = True
    if len(lastName)<1 :
        flash("Please do Not Leave Your Last Name Blank")
        errors = True
    if len(passWord)<1:
        flash("A Password has not been written")
        errors = True
    if len(confirmPassword)<1:
        flash("You have not added written ANything inside of your confirm password field")
        errors =True
    #checking to makre sure firstname and last name have no integers
    if hasNumbers(firstName):
        flash("Your first name had numbers in it!")
        errors = True
    if hasNumbers(lastName):
        flash("Your Last name has numbers in it!")
        errors = True
    if len(passWord) < 8:
        flash("Your password is too small")
        errors = True
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        errors = True
    if passWord != confirmPassword:
        flash("Your password doesnt match to the confirm!")
        errors = True
    if not hasUpperAndNumber(passWord):
        flash("Your password Must containt at least 1 number and 1 Uppercase")
        errors = True
    if errors:
        return redirect('/')
    else:    
        return render_template("register.html",email=eMail,fName=firstName,lName=lastName)


app.run(debug=True)