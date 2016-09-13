from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key="ThisIsSecret"

@app.route('/')
def guessAnyNumber():
	if not 'randomNumber' in session:
		session['randomNumber'] = random.randrange(0, 101)
	
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def badthings():
	guess=int(request.form['guess'])
	print guess
	print session['randomNumber']

	if guess>session['randomNumber']:
		session['response'] =  "TOO HIGH, TRY AGAIN"
	elif guess<session['randomNumber']:
		session['response'] = "TOO LOW, TRY AGAIN"
	else:
		session['response'] = "YOU GOT IT RIGHT"

	return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
	session.pop('randomNumber')
	# session.pop('response')
	return redirect('/')

app.run(debug=True)
