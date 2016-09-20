from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'emaildb')
app.secret_key = "ThisIsSecret!"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def submit():
    working=True
    if len(request.form['email']) < 1:
        flash('Email cannot be blank!', 'red')
        working=False

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", "red")
        working=False

    if not working:
        return redirect('/') 

    else:
        session['email_address'] = request.form['email']

        query = "INSERT INTO email_addresses (email_address, created_at, updated_at) VALUES (:email_address, NOW(), NOW())"
        
        data = {
                 'email_address': request.form['email']
               }

        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)
        return redirect('/success')

@app.route('/success')
def success():
    flash("The email address you entered ({}) is a valid email address! Thank You!".format(session['email_address']), 'green')

    query = "SELECT * FROM email_addresses"
    emails=mysql.query_db(query)

    return render_template('success.html', emails=emails)
app.run(debug=True)
















# @app.route('/friends', methods=['POST'])
# def create():
#     # Write query as a string. Notice how we have multiple values
#     # we want to insert into our query.
#     query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
#     # We'll then create a dictionary of data from the POST data received.
#     data = {
#              'first_name': request.form['first_name'], 
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation']
#            }
#     # Run query, with dictionary values injected into the query.
#     mysql.query_db(query, data)
#     return redirect('/')

# @app.route('/friends/<friend_id>')
# def show(friend_id):
#     # Write query to select specific user by id. At every point where
#     # we want to insert data, we write ":" and variable name.
#     query = "SELECT * FROM friends WHERE id = :specific_id"
#     # Then define a dictionary with key that matches :variable_name in query.
#     data = {'specific_id': friend_id}
#     # Run query with inserted data.
#     friends = mysql.query_db(query, data)
#     # Friends should be a list with a single object,
#     # so we pass the value at [0] to our template under alias one_friend.
#     return render_template('index.html', one_friend=friends[0])

# @app.route('/update_friend/<friend_id>', methods=['POST'])
# def update(friend_id):
#     query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
#     data = {
#              'first_name': request.form['first_name'], 
#              'last_name':  request.form['last_name'],
#              'occupation': request.form['occupation'],
#              'id': friend_id
#            }
#     mysql.query_db(query, data)
#     return redirect('/')

# @app.route('/remove_friend/<friend_id>', methods=['POST'])
# def delete(friend_id):
#     query = "DELETE FROM friends WHERE id = :id"
#     data = {'id': friend_id}
#     mysql.query_db(query, data)
#     return redirect('/')

app.run(debug=True)
