from flask import Flask, render_template, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[\d]') 
app = Flask(__name__)
app.secret_key = "TopSecret"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
   if len(request.form['email']) < 1:
      flash("Email cannot be blank!")
   if not EMAIL_REGEX.match(request.form['email']):
      flash("Invalid Email Address!")
   if len(request.form['first_name']) < 1:
   	flash('Name cannot be empty!')
   if len(request.form['last_name']) < 1:
      flash('Name cannot be empty!')
   if NAME_REGEX.match(request.form['first_name']):
   	flash('Please do not use numbers in your name!')
   if NAME_REGEX.match(request.form['last_name']):
      flash('Please do not use numbers in your name!')
   if len(request.form['password']) < 9:
      flash('Your password should be at least 8 characters long!')
   if not request.form['password'] == request.form['confirm_password']:
      flash('Passwords do not match. Please enter and confirm your passwords again.')
   else:
      flash('Thanks for submitting your information!')
   return redirect('/')

app.run(debug=True) 