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
    query = "SELECT user.id, user.password, user.first_name FROM user WHERE email = :email"
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
    session['fname'] = user['first_name']
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
    session['fname'] = fname
    return redirect('/wall')

@app.route('/wall')
def wall():
    if not '_id' in session:
        return redirect('/')

    msg_query = "SELECT user.first_name, user.last_name, message.id, message.message,date(message.created_at) AS _date  FROM thewall.message LEFT JOIN thewall.user ON message.user_id = user.id   ORDER BY message.created_at"
    messages = mysql.query_db(msg_query)
    comment_query = "SELECT *, date(comment.created_at) AS _date FROM thewall.comment LEFT JOIN thewall.user ON comment.user_id = user.id   ORDER BY comment.created_at"
    comments = mysql.query_db(comment_query)
    return render_template('wall.html',messages=messages,comments=comments)

@app.route('/logout', methods=['POST'])
def logout():
    for key in session.keys():
        session.pop(key)
    return redirect('/')
@app.route('/add_message', methods=['POST'])
def add_msg():
    msg = request.form['add_message']
    if msg != "":
        insert_query = "INSERT INTO thewall.message (user_id, message) VALUES (:_id, :message);"
        qdata = {'_id':session['_id'],'message':msg}
        mysql.query_db(insert_query,qdata)
    return redirect('/wall')

@app.route('/add_comment', methods=['POST'])
def add_comment():
    comment = request.form['add_comment']
    if comment != "":
        msg_id = request.form['add_to_msg_id']
        insert_query = "INSERT INTO thewall.comment (user_id, message_id, comment) VALUES (:_id, :message_id, :comment);"
        qdata = {'_id':session['_id'],'message_id':msg_id,'comment':comment}
        mysql.query_db(insert_query,qdata)
    return redirect('/wall')
app.run(debug=True)



# INSERT INTO thewall.user (first_name, last_name, email, password) VALUES ('will', 'wright', 'w@w.com', 'asdfghjkl');
