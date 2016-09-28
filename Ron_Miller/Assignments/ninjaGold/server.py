from flask import Flask ,render_template, request, redirect, session
import random
import datetime
app= Flask(__name__)
app.secret_key = 'ThisIsSecret'



@app.route('/')
def index():

	# session.pop('score')
	# session.pop('stringer')
	if not 'score' in session:
		session['score']=0
		session['stringer']=""

	return render_template('index.html')

@app.route('/process_money', methods=['POST'] )
def addTwo():
	invest =request.form["building"]

	if invest =="Farm":
		session['turn']=random.randint(10,20)
		session['score']+=session['turn']
		session['now']=datetime.datetime.now()
		session['stringer']="<h6 class='green'>Earned " +str(session['turn']) + " golds from the farm! "+str(session['now'])+"</h6>"+session['stringer']
		print session['stringer']




	elif invest == "Cave":
		session['turn']=random.randint(5,10)
		session["score"]+=session['turn']
		session['now']=datetime.datetime.now()
		session['stringer']="<h6 class='green'>Earned " + str(session['turn']) + " golds from the cave! "+str(session['now'])+"</h6>"+session['stringer']
		print session['stringer']

	elif invest == "House":
		session['turn']=random.randint(2,5)
		session["score"]+session['turn']
		session['now']=datetime.datetime.now()
		session['stringer']="<h6 class='green'>Earned " + str(session['turn']) + " golds from the house! "+str(session['now'])+"</h6>"+session['stringer']
		print session['stringer']

	elif invest == "Casino":
		session['turn']=random.randint(-50,50)
		session["score"]+=session['turn']
		session['now']=datetime.datetime.now()
		if session['turn']<0:
			session['stringer']="<h6 class='red'>YOU SUCK!" + str(session['turn']) + " golds! "+str(session['now'])+"</h6>"+session['stringer']
			print session['stringer']
		else:
			session['stringer']="<h6 class='green'>Lucky You!" + str(session['turn']) + " golds! "+str(session['now'])+"</h6>"+session['stringer']
			print session['stringer']

			
	session['strscore'] = str(session['score'])

	return redirect('/')		

	


app.run(debug=True)