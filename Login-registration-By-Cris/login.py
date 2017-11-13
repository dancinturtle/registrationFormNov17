from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'login')
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    
    return render_template('login.html')

@app.route('/process', methods=['POST'])
def process():
    

    if len(request.form['first_name']) < 2:
        flash("Name have to be more than 2 letters!")
    elif  len(request.form['last_name']) < 2:
        flash("Name have to be more than 2 letters!")
    elif  len(request.form['email']) < 2:
        flash("email is invalid!")
    elif  len(request.form['password']) < 8:
        flash("password should be at least 8 characters!")
    elif request.form['confirmation_password'] != request.form['password']:
        flash("Unmatched password!")
    else:
        flash("Success! Your registration is confirmed")
        
        query = "INSERT INTO registrations (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
        # hashed_password = sdlfkmasldkf(request.form['password'])

        data = {
        
             'first_name': request.form['first_name'],
             'last_name': request.form['last_name'],
             'email': request.form['email'],
             'password': request.form['password'],
             
        }
        mysql.query_db(query, data)

    return redirect('/')

@app.route('/login', methods=['get'])
def login():
    
    return render_template('loginpage.html')


@app.route('/success', methods=['POST'])
def success():
    email = request.form['email']
    password = request.form['password']

    query = "SELECT * FROM registrations WHERE email = :email AND password = :password"

    data = {
        'email': email,
        'password': password
    }
    user = mysql.query_db(query,data)
    
    if user:
        session['id'] = user[0]['id']
        
        return redirect('/newsfeed')
    
    else:
        flash("Unmatched password!")
        return redirect('/login')

    # query = "SELECT * FROM "                           
    # friends = mysql.query_db(query)

@app.route('/newsfeed')
def newsfeed():
    if 'id' in session:
        query = "SELECT * FROM registrations WHERE id = :id"
        data = {'id': session['id']}
        user = mysql.query_db(query,data)

        name = user[0]['first_name']
        return render_template('newsfeed.html', name=name)
    else:
        return redirect('/login')

    
app.run(debug=True)






# from flask import Flask, request, redirect, render_template, session, flash
# from mysqlconnection import MySQLConnector
# app = Flask(__name__)
# mysql = MySQLConnector(app,'emails')
# app.secret_key = 'KeepItSecretKeepItSafe'
# @app.route('/')
# def index():
#     query = "SELECT * FROM email_table"                           
#     friends = mysql.query_db(query)       
#     return render_template('emaildb.html',all_emails=friends)

# @app.route('/process', methods=['Post'])
# def process():

#     query = "INSERT INTO email_table (email_address, created_at) VALUES (:email_address,NOW())"

#     data = {
        
#              'email_address': request.form['email'],
             
#             }
    

#     if len(request.form['email']) < 3:     #!!!check this jellyfish!
#           flash("Email is not valid!")
#     else:
#           flash("Success! The email address you enterend {} is a VALID email address! Thank you!".format(request.form['email']))
#   #do some validations here!

#     mysql.query_db(query, data)
#     return redirect('/')
# app.run(debug=True)
