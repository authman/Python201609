from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/ninja/')
def ninja():

    return render_template('ninjas.html')

@app.route('/ninja/<vararg>')
def secretNinjas(vararg):

    if vararg.lower() == 'blue':
        turtle = 'leonardo'
    elif vararg.lower() == 'orange':
       turtle = 'michelangelo'
    elif vararg.lower() == 'red':
        turtle = 'raphael'
    elif vararg.lower() == 'purple':
        turtle = 'donatello'
    else:
        turtle = 'other'
    
    return render_template('secretNinjas.html', ninja = turtle)


app.run(debug=True)
