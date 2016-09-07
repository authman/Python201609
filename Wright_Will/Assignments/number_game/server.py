from flask import Flask, render_template, session, redirect,request
from random import randint
import re
app = Flask(__name__)
app.secret_key = 'freddy'

@app.route('/',methods=['POST','GET'])
def home():
    isCorrect = ""
    message = ""
    color = 'red'
    if not session.has_key('num'):
        session['num'] = randint(0,100)
    if request.form.has_key('guess'):
        guess = int(request.form['guess'])
        num = session['num']
        print guess
        print num
        if guess > num:
            color = 'red'
            message = 'Too High!'
            isCorrect = False

        elif guess < num:
            color = 'red'
            message = 'Too Low!'
            isCorrect = False
        else:
            color = 'green'
            message = str(guess) + ' was the Number!'
            isCorrect = True
    return render_template("index.html",message=message,color=color,isCorrect=isCorrect)

@app.route('/reset', methods=['POST','GET'])
def reset():
    print "reset"
    session.pop('num')
    return redirect("/")

app.run(debug=True)
