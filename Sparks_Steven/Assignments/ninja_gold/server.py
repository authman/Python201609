from flask import Flask, render_template, request, redirect, session
import random
import datetime
import time
app = Flask(__name__)
app.secret_key='ThisIsSecret'


@app.route('/')
def main_page():
	
	if not session.has_key('count'):
		session['count'] = 0

	if not session.has_key('activity'):
		session['activity'] = ''

	
	# timex=time.strftime('%b %d %Y %H:%M:%S', time.localtime())

	return render_template("index.html", count=session['count'], activity=session['activity'], current_time=session['current_time'])

@app.route('/process_money', methods=['POST'])
def process_money():
	if(request.form['building'] == 'farm'):
		session['rand'] = random.randrange(10, 21)
		session['count'] += session['rand']	
		session['activity'] = '<p class="green">You earned ' + str(session['rand']) + ' golds from the farm. '+ time.strftime('%b %d %Y %I:%M:%S%p', time.localtime()) +'</p>' + session['activity']
	elif(request.form['building']== 'cave'):
		session['rand'] = random.randrange(5, 11)
		session['count'] += session['rand']	
		session['activity'] = '<p class="green">You earned ' + str(session['rand']) + ' golds from the cave. '+ time.strftime('%b %d %Y %I:%M:%S%p', time.localtime()) +'</p>'+ session['activity'] 
	elif(request.form['building']== 'house'):
		session['rand'] = random.randrange(2, 6)
		session['count'] += session['rand']	
		session['activity'] = '<p class="green">You earned ' + str(session['rand']) + ' golds from the house. '+ time.strftime('%b %d %Y %I:%M:%S%p', time.localtime()) +'</p>'+ session['activity']
	elif(request.form['building']== 'casino'):
		session['rand'] = random.randrange(-50, 51)
		session['count'] += session['rand']
		if session['rand'] >= 0:
			session['activity'] = '<p class="green">You earned ' + str(session['rand']) + ' golds from the casino.'  + time.strftime('%b %d %Y %I:%M:%S%p', time.localtime()) +'</p>'+ session['activity']
		elif session['rand'] < 0:
			session['activity'] = '<p class="red">You lost ' + str(-session['rand']) + ' golds at the casino.'  + time.strftime('%b %d %Y %I:%M:%S%p', time.localtime()) +'</p>'+ session['activity']
	return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
	session['count'] = 0
	session['activity'] = ''
	return redirect('/')

app.run(debug=True)

	# @app.route('/')
	# def page_visits():
		
	# 	if not session.has_key('count'):
	# 		session['count']=0 
	# 	else:
	# 		session['count']+=1

	
# @app.route('/')
# def index():
# 	return render_template("index.html")
# @app.route('/user', methods=['POST'])
# def create_user():
# 	print "Got Post Info"
#    # notice how the key we are using to access the info corresponds with the names
#    # of the inputs from our html form
# 	session['name'] = request.form['name']
# 	session['email'] = request.form['email']
# 	return redirect('/show') # redirects back to the '/' route
# @app.route('/show')
# def show_user():
# 	return render_template('user.html')