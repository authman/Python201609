from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector
import re
from flask.ext.bcrypt import Bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

bcrypt = Bcrypt(app)

mysql = MySQLConnector(app, 'kenbook')



@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():




    if request.form['action'] == 'register' :
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password1']
        password_confirm = request.form['password2']
        

        
        if len(first_name) < 2:
            flash('Your first name must be at least 2 characters', 'error')
        elif len(last_name) < 2:
            flash('Your last name must be at least 2 characters', 'error')
        elif not EMAIL_REGEX.match(email):
            flash('Please use a valid email address', 'error')
        elif len(password) < 8:
            flash('Your password must be at least 8 characters', 'error')
        elif not password_confirm == password:
            flash('Your passwords do not match', 'error')
        else:

            register_query = 'INSERT INTO user (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'

            pw_hasher = bcrypt.generate_password_hash(password)

            data = {
                'first_name' : first_name,
                'last_name' : last_name,
                'email' : email,
                'password' : password,
                'pw_hash' : pw_hasher
            }

            mysql.query_db(register_query, data) ###ADD TO DATABASE

            select_query = 'SELECT * FROM user WHERE email = :email LIMIT 1'

            user = mysql.query_db(select_query, data) ###QUERY USER TO POST ON SUCCESS PAGE

            return render_template('success.html', user = user)
        

    elif request.form['action'] == 'login' :
        
        email = request.form['email']
        password = request.form['password1']
        data = {
            'email' : email,
            'password' : password
        }

        if not EMAIL_REGEX.match(email):
            flash('Please enter a valid email', 'error')        ###validations
        elif len(password) < 8:
            flash('Your password must be at least 8 characters', 'error')
        else:
            select_query = 'SELECT * FROM user WHERE email = :email LIMIT 1'

            user = mysql.query_db(select_query, data)

            if user:   ###if user email exists in database, proceed to check hashed pw
            
                if bcrypt.check_password_hash(user[0]['pw_hash'], password):
                    return render_template('success.html', user = user)          ###successful
                else:
                    flash('Wrong password!', 'error')
                    

            else:           ###wrong email!
                flash('Wrong email!', 'error')
                
        
        

    return redirect('/')


@app.route('/success', methods=['GET'])
def success():
    


    return render_template('success.html')


app.run(debug=True)
