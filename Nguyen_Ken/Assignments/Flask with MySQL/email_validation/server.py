from flask import Flask, render_template, request, redirect, session, flash
import re
from datetime import datetime
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

REGEX_EMAIL = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
REGEX_PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$')

mysql = MySQLConnector(app, 'friendsdb')

@app.route('/')
def index():



    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    
    if not REGEX_EMAIL.match(request.form['email']):
        flash('Please enter a valid email b0$$', 'error')
        
    else:
        #add emails
        addUser = 'INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())'
        data = {
            'email' : request.form['email']
        }
        mysql.query_db(addUser, data)
        
        
        #show emails
        queryRecords = 'SELECT email, created_at FROM email'
        allRecords = mysql.query_db(queryRecords)

        
        flash('Awesome, your email address is {}'.format(request.form['email']), 'success')
        return render_template('success.html', allRecords = allRecords)
    
    
    return redirect('/')


app.run(debug=True)
