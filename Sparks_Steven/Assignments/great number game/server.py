from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key='Sectrkey'

@app.route('/')
def main_page():
	if not session.has_key('number'):
		session['number'] = random.randrange(0, 101)
	
	if not session.has_key('msg'):
		session['msg'] = ''	

	if not session.has_key('color'):
		session['color'] = ''
	
	return render_template("index.html", msg = session['msg'], color = session['color'])

@app.route('/process', methods=['POST'])
def verify_guess():
	session ['guess'] = int(request.form['guess'])
			
	if(session ['guess'] == session['number']):
		session['msg'] = 'You\'re guess is correct the number was ' + str(session['number'])+'!'
		session['color']='green'

	elif(session ['guess'] < session['number']):
		session['msg'] = 'Too low.'
		session['color']='red'  

	else: 
		session['msg'] = 'Too high.' 
		session['color']='red'
		
	return redirect('/')

@app.route('/restart', methods=['POST'])
def restart():
	session.pop('number') 
	session.pop('guess')
	return redirect('/')

app.run(debug=True)

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