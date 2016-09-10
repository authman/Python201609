from flask import Flask, session, redirect, render_template, flash, request
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = 'fred'
mysql = MySQLConnector(app,'login_reg')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def process():
    email = request.form['email']
    fname = request.form['fname']
    lname = request.form['lname']
    password = request.form['password']
    confirm_pass = request.form['confirm_pass']
    error = False

    if not re.match(r"\b[a-z]+[a-z0-9_]*@.+\..+\b",email,):
        flash("not a valid email")
        error = True

    if not re.match(r"\b[a-zA-Z]+\b",fname,):
        flash("First Name can only contain letters and must be at least 2 charachters")
        error = True

    if error:
        return redirect('/')
    return redirect('/success')
@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
