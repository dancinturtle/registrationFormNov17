from flask import Flask, render_template, request, session, redirect, flash#importing flask module so we can create our app.  all listed allow us to render, redirect, etc. html
import re #the re module perform some regular expression operations
app = Flask(__name__)#global variable name is used and tells Flask if we are running the file directly or importing as a module.

app.secret_key = "Secretkey"#for security purposes
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')# this is regex- sequence python to confirm a valid email. 

@app.route('/')#@is a decorater and attaches the function to the route '/'.  route communicates with the server what kind of info is needed. hence run this function. 
def index():# in this case, this function attaches to the render_template from index.html  this will render/get our form 
    return render_template('index.html')

#route to accept the submitted form and validate it
@app.route('/registration', methods=["POST"])# the app route now is in 'register' we use methods "POST" because we are sensitive info.  this route will handle the form submission.
def registration():
    
    if len(request.form["email"]) == 0:#'email' is the name attribute we added to our form inputs.  To access all data we use request.form[name_of_input].
        flash("Email cannot be blank")#if conditional to ensure that there is some letters.
       
    elif not EMAIL_REGEX.match(request.form['email']):# all request.form will return as a string.
        flash("Invalid email")#flash is expecting a correct string.
        

    if len(request.form["first_name"]) < 0:#again, we are checking to see if the field is empty.  no length.
        flash("First name is required")
       
    elif not request.form["first_name"].isalpha():# returns a boolean to confirm only alphabetic characters.
        flash("Invalid first name")

    if len(request.form["last_name"]) < 0:#making sure we have more than one letter
        flash("Last name is required")
      
    elif not request.form["last_name"].isalpha(): # returns a boolean to confirm only alphabetic characters.
        flash("Invalid last name")

    if len(request.form["pw"]) < 8:# this will ensure we have 8 characters
        flash("Password must be at least 8 characters")
        
    elif request.form["pw"] != request.form["confpw"]:
        flash("Passwords do not match")
       
    else:
        flash("Completed.")# if all is completed, note that in the return.
        
    return redirect('/') #this will redirect to the '/' route.  Always redirect after POST method to avoid data being handled more than once.

app.run(debug=True) #run app and run at debug mode to look for errors. 