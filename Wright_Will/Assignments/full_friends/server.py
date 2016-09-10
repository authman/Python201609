from flask import Flask, redirect, render_template,request
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():
    query = "SELECT * FROM users ORDER BY first_name,last_name"
    data = mysql.query_db(query)
    return render_template('index.html',friends=data)

@app.route('/friends',methods=["POST"])
def create():
    query ="INSERT INTO friends.users (first_name, last_name) VALUES (:fname, :lname);"
    fname = request.form["first_name"]
    lname = request.form["last_name"]
    data={"fname":fname,"lname":lname}
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<_id>/edit')
def edit(_id):
    print _id
    query ="SELECT first_name, last_name FROM users WHERE users.id = :id;"
    data={"id":_id}
    data = mysql.query_db(query, data)
    print data[0]
    return render_template("friend.html",data=data[0],_id=_id)

@app.route('/friends/<_id>',methods=["POST","GET"])
def update(_id):
    query ="UPDATE friends.users SET first_name=:fname, last_name=:lname, updated_at=NOW() WHERE id=:_id;"
    fname = request.form["first_name"]
    lname = request.form["last_name"]
    data={"fname":fname,"lname":lname,"_id":_id}
    mysql.query_db(query, data)
    return redirect("/")

@app.route('/friends/<_id>/delete',methods=["POST"])
def destroy(_id):
    query = "DELETE FROM friends.users WHERE id=:_id;"
    data ={"_id":_id}
    mysql.query_db(query,data)
    return redirect("/")

app.run(debug=True)
