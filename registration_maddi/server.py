from flask import Flask, render_template, request, redirect, flash
import re 
import md5 
import datetime

app = Flask(__name__)
app.secret_key = 'bigsecret'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# NAME_REGEX = re.compile(r'^[a-zA-Z\s]*')



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index', methods=['POST'])

def login():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest()
    date = request.form['date']
    confirm_password  =  request.form['confirm_password']
    print "hello inside route"
    print request.form['first_name'].isalpha()

    #first_name,last_name,email,password,dob validations
    
    if len(request.form['first_name'])< 0 or not request.form['first_name'].isalpha():
        flash("Invalid first_name!")
        
    
    if len(request.form['last_name']) < 0 or not request.form['last_name'].isalpha():
    #  NAME_REGEX.match(request.form['last_name']):
        flash("Inavalid last_name !")  
    
    
    if len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email']) :
        flash("Invalid email!!")
        
    
    if request.form['password'] != request.form['confirm_password'] :
        flash("passwords are not matching!") 
    
    if len(request.form['password'])  < 8 :
        flash("password must be atleast 8 characters")

    #date of birth 
    minyear = 1900
    maxyear = datetime.date.today().year
    print datetime.date.today().year
    mydate = '12/12/2000'
    dateparts = mydate.split('/')
    try:
        if len(date) != 3:
           flash("Invalid date format")
        if int(date[2]) > maxyear or int(date[2]) < minyear:
           flash("Year out of range")
        dateobj = datetime.date(int(date[2]),int(date[1]),int(date[0]))
    except:
       flash("")

    return redirect("/")
    return redirect("/welcome")


@app.route('/welcome')

def user():
    return render_template("welcome.html")


app.run(debug = True)
