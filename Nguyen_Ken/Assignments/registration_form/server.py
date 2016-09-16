from flask import Flask, render_template, request, redirect, session, flash
import re

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():

    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():

    session['email'] = request.form['email']
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['password'] = request.form['password1']
    session['confirm_password'] = request.form['password2']
    
    if len(session['email']) < 1:
        flash('Please enter your email', 'error')

    elif not EMAIL_REGEX.match(session['email']):
        flash('That is not a valid email address', 'error')

    elif len(session['first_name']) < 1:
        flash('Please enter your first name', 'error')

    elif not session['first_name'].isalpha():
        flash('Your name cannot contain numbers or special characters', 'error')

    elif len(session['last_name']) < 1:
        flash('Please enter your last name', 'error')

    elif not session['last_name'].isalpha():
        flash('Your name cannot contain numbers or special characters', 'error')

    elif len(session['password']) < 1:
        flash('Please enter a password', 'error')

    elif len(session['password']) < 8:
        flash('Your password must be greater than 8 characters', 'error')

    elif not session['confirm_password'] == session['password']:
        flash('Your password does not match!', 'error')

    else:
        flash('Thanks for submitting your information', 'success')



    
    return redirect('/')


app.run(debug=True)
