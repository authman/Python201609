from flask import Flask, render_template, request, redirect,session,Markup
from random import randint
from datetime import datetime, date, time
app = Flask(__name__)
app.secret_key = "Dan"

@app.route('/',methods=['GET','POST'])
def index():
    if not session.has_key('log'):
        session['log'] = []
    if not session.has_key('gold'):
        session['gold'] = 0
    return render_template("index.html",gold=session['gold'],log=session['log'])
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

    html_string = "<h6 "
    if earnings < 0:
        html_string += "class = 'red'"
    html_string +=  ">"
    if earnings < 0:
        html_string += "Lost"
    else:
        html_string += "Earned"
    html_string +=  str(earnings) + " gold from the "
    html_string +=  request.form['place'] + "! "
    html_string +=  str(datetime.now().strftime("(%Y/%m/%d  %H:%M)"))
    html_string +=  "</h6>"
    print html_string
    if(len(session['log']) > 12):
        session['log'] = session['log'][1:len(session['log'])]
    session['log'].append(html_string)
    return redirect('/')
app.run(debug=True)
