from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'issasecret'

@app.route('/')

def about():
    return render_template('index.html')

@app.route('/process', methods=['POST'])

def process():
    if len(request.form['name']) < 1 or len(request.form['comments']) < 1:
        flash("Fields cannot be empty!") 
        return redirect('/')
    elif len(request.form['comments']) < 120:
        flash("Comments cannot be longer then 120 characters!")
        return redirect('/')
    else:
        name = request.form['name']
        dojo = request.form['dojo']
        language = request.form['language']
        comments = request.form['comments']

        return render_template('result.html', name = name, dojo = dojo, language = language, comments = comments)

app.run(debug=True)