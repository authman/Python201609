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
    return render_template('results.html')
@app.route('/addUser',methods=['POST'])
def addUser():
    session["name"] = request.form["name"]
    session["email"] = request.form["email"]
    #if not re.match(session["email"],r"[a-Z0-9_]@.*\..*"):
    if len(session["name"]) < 1 or len(session["email"]) < 1:
        return redirect("/")

    return redirect('/results')
@app.route('/deleteUser',methods=['POST'])
def deleteUser():

    return redirect('/results')

app.run(debug=True)
