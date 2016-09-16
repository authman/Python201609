from flask import Flask, render_template, request, redirect, session, flash
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def show_game():
	return render_template("index.html")

@app.route('/process', methods=['POST'])
def number_game():
	
	if not session.has_key('answer'):
		session['answer'] = random.randrange(0, 101)
		
	session['guess'] = int(request.form['guess'])
	if session['guess'] == session['answer']:
		flash('That is correct! Thank you for playing.')
	elif session['guess'] > session['answer']:
		flash('Try again. That guess is too high.')
	elif session['guess'] < session['answer']:
		flash('Try again. That guess is too low.')
	return redirect('/')

app.run(debug=True)