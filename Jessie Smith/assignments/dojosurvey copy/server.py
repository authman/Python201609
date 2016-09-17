from flask import Flask, render_template, request, redirect, session, flash 
app = Flask(__name__)
app.secret_key = 'secret'


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/process', methods=['POST'])
def validation():



   if len(request.form['name'])<1:
      flash("Please enter your name.")
   elif len(request.form['comments'])>120:
      flash("Too long!")
   else:
      session['name'] = request.form['name']
      session['location'] = request.form['location']
      session['language'] = request.form['language']
      session['comments'] = request.form['comments']

      return redirect('/result')

   return redirect('/')


@app.route('/result', methods=['GET'])
def create_user():
   
   

   return render_template("result.html")

   
app.run(debug=True) 



