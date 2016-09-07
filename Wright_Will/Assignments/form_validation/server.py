#server
from flask import Flask, render_template, request,redirect,flash,session
app = Flask(__name__)
app.secret_key = "bob"

@app.route('/')
def home():

    if not session.has_key('name'):
        session['name'] = ""
    if not session.has_key('location'):
        session['location'] = "San Fransisco"
    if not session.has_key('language'):
        session['language'] = "Python"
    if not session.has_key('comment'):
        session['comment'] = ""
    return render_template("index.html",name=session['name'],location=session['location'],language=session['language'],comment=session['comment'])

@app.route('/results',methods = ["post"])
def results():
    session['name'] =request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] =request.form['comment']
    if len(session['name']) < 1:
        flash('name must not be blank')
        return redirect('/')
    if len(session['comment']) < 1:
        flash('comment must not be blank')
        return redirect('/')
    if len(session['comment']) > 120:
        flash('comment can not be larger than 120 charachters')
        return redirect('/')

    return render_template("results.html",name=session['name'],location=session['location'],language=session['language'],comment=session['comment'])


app.run(debug=True)
