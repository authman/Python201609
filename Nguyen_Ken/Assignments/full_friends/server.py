from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

mysql = MySQLConnector(app, 'friendsdb')





@app.route('/')
def index():
    showQuery = 'SELECT * FROM friends'

    friends = mysql.query_db(showQuery)


    return render_template('index.html', all_friends = friends)



@app.route('/friends/<friend_id>/edit')
def edit(friend_id):

    friend_id = friend_id 

    return render_template('edit.html', friend_id = friend_id)
    


@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):

    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'occupation' : request.form['occupation'],
        'id' : friend_id
    }

    updateQuery = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"

    mysql.query_db(updateQuery, data)

    return redirect('/')


@app.route('/friends', methods=['POST'])
def create():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'occupation' : request.form['occupation']
    }

    createQuery = 'INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())'

    mysql.query_db(createQuery, data)

    return redirect('/')

@app.route('/friends/<friend_id>/confirm')
def confirm(friend_id):
    data = {
        'id' : friend_id
    }

    friend_id = friend_id

    singleFriendQuery = 'SELECT * FROM friends WHERE id = :id'

    oneFriend = mysql.query_db(singleFriendQuery, data)

    return render_template('delete.html', friend_id = friend_id, oneFriend = oneFriend)

@app.route('/friends/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):
    data = {'id' : friend_id}
    
    deleteQuery = 'DELETE FROM friends WHERE id = :id'

    mysql.query_db(deleteQuery, data)

    return redirect('/')

    


app.run(debug=True)
