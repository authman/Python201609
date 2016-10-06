from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')
@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM friends")
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	if not 'first_name' in request.form or not 'last_name' in request.form or not 'email' in request.form:
		return redirect('/')

	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']

	mysql.query_db('INSERT INTO friends (first_name, last_name, email) VALUES (:first_name, :last_name, :email);', request.form) 
	return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
	data = {
		'id' : id
	}
	friends = mysql.query_db("SELECT * FROM friends WHERE id = :id", data)
	if len(friends)==0:
		return redirect('/')
	friend = friends[0]
	return render_template('edit.html', friend=friend)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
	data = {
		'first_name' : request.form['first_name'],
		'last_name' : request.form['last_name'],
		'email' : request.form['email'], 
		'id' : id,
		'updated_at' : 'NOW()'
	}
	mysql.query_db("UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :id;", data)
	return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
	data = {
		'id' : id,
	}
	mysql.query_db("DELETE FROM friends WHERE id = :id;", data)
	return redirect('/')


app.run(debug=True)