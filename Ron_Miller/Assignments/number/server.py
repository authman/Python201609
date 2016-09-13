from flask import Flask ,render_template, request, redirect, session
import random
app= Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if not 'guess' in session:
		session['guess']=random.randrange(0,101)
		session['state']=None
	
	
	return render_template('index.html',test=session['state'])

@app.route('/process', methods=['POST'] )
def addTwo():

	if session['state']=='nailed':
		again=request.form['again']
		if again == 'yes':
			del session['guess']
			return redirect('/')

	number = int(request.form['number'])
	

	if number > session['guess']:
		session['state']='high'
		

	elif number < session['guess']:
		session['state']='low'

	elif number == session['guess']:
		session['state']='nailed'
		

			
	
	return redirect('/')		

	


app.run(debug=True)