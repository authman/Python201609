from flask import Flask, session, redirect, render_template, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,db)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process')
def process():
    pass
@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
