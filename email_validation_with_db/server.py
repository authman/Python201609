from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'IAlwaysForgetThis'

# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'myemaildb')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address!")
	else:
		flash("Success! Your email is {}".format(request.form['email']))
		query = "INSERT INTO user (email, created_at, updated_at) VALUES (:email, NOW(),NOW())"
		return redirect('/success')
	return redirect('/')

@app.route('/success', methods=['GET'])
def create():
	query = "SELECT email, created_at FROM user"
	user = mysql.query_db(query)
	print user
	return render_template ('success.html', emails=user)#is this right?








# an example of running a query
print mysql.query_db("SELECT * FROM user")
app.run(debug=True)