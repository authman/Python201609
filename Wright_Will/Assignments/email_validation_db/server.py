from flask import Flask, render_template,redirect
from mysqlconnection import MySQLconnector
app = Flask(__name__)
mysql = MySQLconnector(app,'email_validation')

@app.route('/')
def home():

    return render_template('index.html')
@app.route('/results')
def results():
    return render_template('results.html')
@app.route('/addUser'method='POST')
def addUser():
    return redirect('/results')
@app.route('/deleteUser'method='POST')
def deleteUser():

    return redirect('/results')

app.run(debug=True)
