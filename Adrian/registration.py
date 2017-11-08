from flask import Flask, render_template, redirect, request, session, flash
import re

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key='ThisIsASecret'

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_user():
	print "Got Post Info"
	if request.method == 'POST':
		if len(request.form['email']) < 1:
			flash('Email can not be empty!','wrong')
			if not EMAIL_REGEX.match(request.form['email']):
				flash('Invalid email format!', 'wrong')
		if len(request.form['first_name']) < 1:
			flash('Last name must not be empty', 'wrong')

			if not request.form['first_name'].isalpha(): 
				flash('First name must consist of alphabetical characters','wrong')
			
		if len(request.form['last_name']) < 1:
			flash('Last name must not be empty', 'wrong')
		
			if not request.form['last_name'].isalpha():
				flash('Last name must be alphabetical characters only!','wrong')
		
		if len(request.form['password']) < 1:
			flash('Password must not be empty','wrong')
			if len(request.form['password']) < 8:
				flash('Password must be longer than 8 characters.')
		
		if len(request.form['confirm_password']) < 1:
			flash('Confirm password must not be empty','wrong')
			if len(request.form['confirm_password']) < 8:
				flash('Password must be longer than 8 characters', 'wrong')
		
		if request.form['password'] != request.form['confirm_password']:
			flash('Both password fields must match!', 'wrong')
		
		else:
			flash('Thank you!','right')
			session['email'] = request.form['email']
			session['first_name'] = request.form['first_name']
			session['last_name'] = request.form['last_name']
			session['password'] = request.form['password']
			session['confirm_password'] = request.form['confirm_password']
	return redirect('/')

app.run(debug=True)