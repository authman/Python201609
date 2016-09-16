from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app, 'mydb')


@app.route('/')
def index():
    # Display all of the friends on the index.html page
    friends = mysql.query_db("SELECT * FROM friend")
    return render_template("index.html", friends = friends)


@app.route('/friends', methods=['POST'])
def create():
    # Handle the add friend form submit and create the friend in the DB
    if not 'first_name' in request.form or not 'last_name'  in request.form or not 'email'      in request.form:
       flash("Don't hack me, bro")
       return redirect('/')

    mysql.query_db("INSERT INTO friend (first_name, last_name, email) VALUES (:first_name, :last_name, :email);", request.form)

    return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
    # Display the edit friend page for the particular friend
    data = {
        'id' : id
    }
    friends = mysql.query_db("SELECT * FROM friend WHERE id = :id LIMIT 1;", data)

    if len(friends) == 0:
        flash("Don't hack me, bro")
        return redirect('/')

    friend = friends[0]
    return render_template('edit.html', friend=friend)


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    # Handle the edit friend form submit and update the friend in the DB
    data = {
        'first_name' : request.form['first_name'],
        'last_name' :  request.form['last_name'],
        'email' :      request.form['email'],
        'updated_at' : 'NOW()',
        'id' :         id
    }
    mysql.query_db("UPDATE friend SET first_name=:first_name, last_name=:last_name, email=:email WHERE id = :id LIMIT 1;", data)

    return redirect('/')


@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):
    # Delete the friend from the DB
    mysql.query_db("DELETE FROM friend WHERE id = :id LIMIT 1;", {'id' : id} )
    return redirect('/')



app.run(debug=True)
