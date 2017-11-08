from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    
    return render_template('registration.html')

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
       
    return redirect('/')

@app.route('/login', methods=['get'])
def login():
    
    return render_template('loginpage.html')


@app.route('/success', methods=['POST'])
def success():
    email = request.form['email']
    password = request.form['password']

    if user:
        session['id'] = user[0]['id']
        
        return redirect('/newsfeed')
    
    else:
        flash("Unmatched password!")
        return redirect('/login')



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



app.run(debug=True)