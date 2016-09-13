from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "TopSecret"

@app.route('/')
def index():
  return render_template("index.html", count=session['count'])

@app.route('/process_money', methods=['POST'])
def process_money():
   if not session.has_key('count'):
      session['count'] = 0
   if request.form['building'] == 'farm':
      session['count'] += random.randrange(10, 21)
   elif request.form['building'] == 'cave':
      session['count'] += random.randrange(5, 11)
   elif request.form['building'] == 'house':
      session['count'] += random.randrange(2, 6)
   elif request.form['building'] == 'casino':
      session['count'] -= random.randrange(-50, 51)
   
   return redirect('/')

app.run(debug=True) 