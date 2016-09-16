from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

@app.route('/')
def index():
    session['random'] = int(random.randrange(0,101))

    #reset session
    if 'highDisplay' in session:
        session.pop('highDisplay')
    if 'lowDisplay' in session:
        session.pop('lowDisplay')
    if 'correctDisplay' in session:
        session.pop('correctDisplay')
    if 'formHide' in session:
        session.pop('formHide')
    if 'tooHigh' in session:
        session.pop('tooHigh')
    if 'tooLow' in session:
        session.pop('tooLow')
    if 'correct' in session:
        session.pop('correct')
    if 'guess' in session:
        session.pop('guess')

        

    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    
    return redirect('/1')


@app.route('/1')
def index2():
    #reset answer displays
    if 'highDisplay' in session:
        session.pop('highDisplay')
    if 'lowDisplay' in session:
        session.pop('lowDisplay')
    if 'correctDisplay' in session:
        session.pop('correctDisplay')
    if 'formHide' in session:
        session.pop('formHide')
    if 'tooHigh' in session:
        session.pop('tooHigh')
    if 'tooLow' in session:
        session.pop('tooLow')
    if 'correct' in session:
        session.pop('correct')

    if 'guess' in session:
        if session['guess']>session['random']:
            session['tooHigh'] = 'Too High!'
            session['highDisplay'] = 'block'
        elif session['guess']<session['random']:
            session['tooLow'] = 'Too Low!'
            session['lowDisplay'] = 'block'
        elif session['guess'] == session['random']:
            session['correct'] = session['random']
            session['correctDisplay'] = 'block'
            session['formHide'] = 'none'
        


    return render_template('index.html')

app.run(debug=True)
