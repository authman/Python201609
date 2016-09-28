from flask import Flask ,render_template, request, redirect, session

app= Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if not 'number' in session:    #if not session.has_key('number'):
		session['number'] = 0



	session['number']+=1
	##if request.form['value']== "Do Something":
		##session['number']+=2

	return render_template('index.html',num=session['number'])

@app.route('/process', methods=['POST'] )
def addTwo():

	submit = request.form['submit']
	if submit == 'add2':
		session['number']+=1


	elif submit=='reset':
		session['number']=-1

	
	return redirect('/')		

	


app.run(debug=True)