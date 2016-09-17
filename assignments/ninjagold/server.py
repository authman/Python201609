from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
import random
app.secret_key="ThisIsSecret"

@app.route('/')
def ninjamoney():
	
	if not session.has_key('count'):
		session['count'] = 0 

	if not session.has_key('message'):
		session['message'] = [] 

	if not session.has_key('num'):
		session['num'] = 0
	
	return render_template("index.html", num=session['num'], count=session['count'], message=reversed(session['message']))


@app.route('/process_money', methods=['POST'])
def process_money():


	if (request.form['building'] == 'farm'):
		session['num'] = random.randrange(10, 21)
		session['count'] += session['num']
		session['message'].append("You earned " + str(session['num']) + " golds from the farm!")
		
	elif (request.form['building'] == 'cave'):
		session['num'] = random.randrange(5, 11)
		session['count'] += session['num']
		session['message'].append("You earned " + str(session['num']) + " golds from the cave!")

	elif (request.form['building'] == 'house'):
		session['num'] = random.randrange(2, 6)
		session['count'] += session['num']
		session['message'].append("You earned " + str(session['num']) + " golds from the house!")

	elif (request.form['building'] == 'casino'):
		session['num'] = random.randrange(-51, 51)
		session['count'] += session['num']
		session['message'].append("You earned " + str(session['num']) + " golds from the casino!")

	return redirect('/')

app.run(debug=True)


