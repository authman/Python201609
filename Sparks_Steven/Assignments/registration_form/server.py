from flask import Flask, render_template, redirect, request, session, flash
import re

app = Flask(__name__)
app.secret_key = 'ThisIsSecret!'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
  
  return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():

    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirm_password = request.form['confirm_password']

    if len(email) < 1:
        flash("Email cannot be blank!")
    
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
    
    elif len(first_name) < 1:
        flash("First name cannot be blank!")

    elif not first_name.isalpha():
        flash("Your name cannot contain numbers nor special characters")
    
    elif len(last_name) < 1:
        flash("Last name cannot be blank!")

    elif not last_name.isalpha():
        flash("Your name cannot contain numbers nor special characters")
    
    elif len(password) < 1:
        flash("Password cannot be blank!")

    elif len(password) < 8:
        flash("Password must contain 8 characters or more")

    elif not confirm_password==password:
        flash("Passwords do not match")

    else:
        flash("Success!")

    return redirect('/')

app.run(debug=True)