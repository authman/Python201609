from flask import Flask, render_template, request, redirect,session
from random import randint
app = Flask(__name__)
app.secret_key = "fred"

@app.route('/',methods=['GET','POST'])
def index():
    if not session.has_key('log'):
        session['log'] = ""
    if not session.has_key('gold'):
        session['gold'] = 0
    return render_template("index.html")
@app.route('/processgold',methods=['GET','POST'])
def processgold():
    earnings = 0
    if request.form['place'] == 'farm':
        earnings =  randint(10,21)
    elif  request.form['place'] == 'cave':
        earnings = randint(5,11)
    elif  request.form['place'] == 'house':
        earnings = randint(2,6)
    elif  request.form['place'] == 'casino':
        earnings = randint(-50,51)
    session['gold'] += earnings
    session['log'] += "\n" + "Earned " + str(earnings) + "gold from the " + request.form['place'] + "!"
    print session['log']
    return redirect('/')
app.run(debug=True)
