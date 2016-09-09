from flask import Flask, render_template,redirect,request,session
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
app.secret_key = "fred"
mysql = MySQLConnector(app,'email_validation')

@app.route('/')
def home():
    if not 'email' in session:
        session['email'] = ""
    if not 'name' in session:
        session['name'] = ""
    return render_template('index.html',name=session['name'],email=session['email'])


@app.route('/results' )
def results():
    data = mysql.query_db("SELECT name,email,id FROM user")
    return render_template('results.html',data=data)


@app.route('/addUser',methods=['POST'])
def addUser():
    session["name"] = request.form["name"]
    session["email"] = request.form["email"]
    #if not re.match(session["email"],r"[a-Z0-9_]@.*\..*"):
    if len(session["name"]) < 1 or len(session["email"]) < 1:
        return redirect("/")
    query = "INSERT INTO email_validation.user (email, name) VALUES (:email,:name)";
    data = {
            'email':session['email'],
            'name':session['name']
            }
    mysql.query_db(query,data)
    return redirect('/results')


@app.route('/deleteUser',methods=['POST'])
def deleteUser():
    userid = request.form["userid"]
    query = "DELETE FROM email_validation.user WHERE id=:id";
    data={"id":userid}
    mysql.query_db(query,data)
    return redirect('/results')

app.run(debug=True)
