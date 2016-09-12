from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import MySQLConnector
from random import randint
import re
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = 'fred'
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'thewall')



def not_valid_email(email):
    if  re.match(r"[a-z]+[a-z0-9_]*@[a-z]+.[a-z]+",email):
        return False
    flash(email + " is not a valid email")
    return True

def not_valid_password(password):
    if re.match(r"[a-z0-9_]{8,}",password):
        return False
    flash(password + " is not a valid password")
    flash("password must be at least 8 alphanumric charachters")
    return True
def not_valid_name(name):
    if re.match(r"\b[a-z]{2,}\b",name):
        return False
    flash(name + " is not a valid name")
    return True


@app.route('/')
def index():
    if '_id' in session:
        return redirect('/wall')
    query = "SELECT * FROM user"
    print mysql.query_db(query)
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    #get form data
    email = request.form['email']
    password = request.form['password']
    error = False

    #validate email and password
    error = not_valid_email(email)
    error = not_valid_password(password)
    if error:
        return redirect('/')

    #get user data
    query = "SELECT user.id, user.password FROM user WHERE email = :email"
    qdata = {'email':email}
    user = mysql.query_db(query,qdata)

    # check email is in db
    if len(user) == 0:
        flash("We couldn't find the email you entered")
        return redirect('/')
    user = user[0]

    # validate password matches
    if not bcrypt.check_password_hash(user['password'], password):
        flash("wrong password")
        return redirect('/')

    session['_id'] = user['id']
    return redirect('/wall')

@app.route('/register', methods=['POST'])
def register():

    #get form data
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    # validate form
    error = False
    error = not_valid_name(fname)
    error = not_valid_name(lname)
    error = not_valid_email(email)
    error = not_valid_password(password)
    if not password == confirm_password:
        error = True
        flash('password does not match confirm password')
    if error:
        return redirect('/')

    #check if email already registered
    query = "SELECT email FROM user WHERE email = :email"
    qdata = {'email':email}
    emails = mysql.query_db(query,qdata)

    if len(emails) > 0:
        flash('you already have an account with this email')
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(password)
    insert_query = "INSERT INTO thewall.user (first_name, last_name, email, password) VALUES (:fname, :lname, :email, :password);"
    insert_data = {'fname':fname, 'lname':lname, 'email':email, 'password':pw_hash}
    session['_id'] = mysql.query_db(insert_query,insert_data)
    print session['_id']
    return redirect('/wall')

@app.route('/wall')
def wall():
    if not '_id' in session:
        return redirect('/')

    return render_template('wall.html')

@app.route('/logout', methods=['POST'])
def logout():
    # if '_id' in session:
    #     session.pop
    for key in session.keys():
        session.pop(key)
    return redirect('/')

app.run(debug=True)



# INSERT INTO thewall.user (first_name, last_name, email, password) VALUES ('will', 'wright', 'w@w.com', 'asdfghjkl');
