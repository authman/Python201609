from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'secretsquirrel'


@app.route('/')
def index():
    if 'counter' in session == False:
        session['counter'] = 0

    session['counter'] += 1
        
    return render_template('index.html')

@app.route('/addTwo')
def addTwo():

    session['counter'] += 1
    
    return redirect('/')

@app.route('/reset')
def reset():

    session['counter'] = -1
    
    return redirect('/')



app.run(debug=True)
