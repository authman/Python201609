from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
number=1
@app.route('/')
def index():
	session['number']+=1
	return render_template("index.html", number= number)
   
 

   return redirect('/')
   
app.run(debug=True) # run our server