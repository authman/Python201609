from flask import Flask, render_template, request, redirect, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^\d')
app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def validation():
	broken = False

	if len(request.form['email'])<1:
		flash("Email cannot be blank")
		broken = True
	if not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid email address")
		broken = True

	if len(request.form['first_name'])<1:
		flash("You must enter your first name")
		broken = True

	if len(request.form['last_name'])<1:
		flash("You must enter your last name")
		broken = True

	if len(request.form['password'])<8:
		flash("Your password must be at least eight characters")
		broken = True

	if NAME_REGEX.match(request.form['first_name']):
		flash("Your name cannot contain numbers")
		broken = True

	if NAME_REGEX.match(request.form['last_name']):
		flash("Your name cannot contain numbers")
		broken = True

	if request.form['password'] != request.form['confirm_password']:
		flash("Your passwords do not match")
		broken = True
	
	if broken:
		return redirect('/')

	session['email'] = request.form['email']
	session['first_name'] = request.form['first_name']
	session['last_name'] = request.form['last_name']
	session['password'] = request.form['password']
	session['confirm_password'] = request.form['confirm_password']

	return redirect('/result')


@app.route('/result', methods=['GET'])
def working():
	return render_template("result.html")


app.run(debug=True)
