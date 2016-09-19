from flask import Flask, session, redirect, render_template, flash, request
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = 'bob'
mysql = MySQLConnector(app,'login_reg')
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process',methods=['POST'])
def process():
    error = False
    formtype = request.form['formtype']
    password = request.form['password']
    session['email'] = request.form['email']
    # register specific session values
    if formtype == 'register':
        session['fname'] = request.form['fname']
        session['lname'] = request.form['lname']
        confirm_pass = request.form['confirm_pass']
        # validate first name
        if not re.match(r"\b[a-zA-Z]{3,}\b",session['fname'],):
            flash("First Name can only contain letters and must be at least 2 charachters")
            error = True
        #validate last name
        if not re.match(r"\b[a-zA-Z]{3,}\b",session['lname'],):
            flash("Last Name can only contain letters and must be at least 2 charachters")
            error = True

        if password != confirm_pass:
            flash("Password and Confirm Password must match")
            error = True
    # validate email
    if not re.match(r"\b[a-z]+[a-z0-9_]*@.+\..+\b",session['email'],):
        flash("not a valid email")
        error = True
    #validate password
    if not re.match(r"\b[a-zA-Z0-9_]{8,}\b",password,):
        flash("Password must be alpha-numeric and at least 8 charachters")
        error = True
    user_query = "SELECT * FROM user WHERE email = :email"
    pw_hash = bcrypt.generate_password_hash(password)
    query_data = { 'email': session['email'],'fname':session['fname'],'lname':session['lname'] }
    emails = mysql.query_db(user_query, query_data)
    print emails
    if formtype == 'register':
        if  len(emails) > 0:
            error = True
            flash("This email already has an account")
    else:
        if  len(emails) == 0:
            error = True
            flash("we couldn't find your email")
        else:
            if not bcrypt.check_password_hash(emails[0]["password"], password):
                print pw_hash
                print emails[0]["password"]
                flash("wrong password")
                error = True
    if error:
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(password)
    query_data['pw_hash']= pw_hash
    insert_query = "INSERT INTO user (email, first_name, last_name, password) VALUES (:email, :fname, :lname, :pw_hash)"
    session['_id'] = mysql.query_db(insert_query, query_data)
    return redirect('/success')
@app.route('/success')
def success():
    return render_template('success.html')
@app.route('/log_out')
def log_out():
    session.pop('_id')
    return redirect('/')

app.run(debug=True)
