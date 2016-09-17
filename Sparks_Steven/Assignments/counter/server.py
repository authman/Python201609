from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='ThisIsSecret'

@app.route('/')
def page_visits():
	
	if not session.has_key('count'):
		session['count']=0 
	else:
		session['count']+=1

	return render_template("index.html", count=session['count'])


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