from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)

app.secret_key = 'secretsquirrel'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def create_user():
    print "$$$Creating User$$$"


    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if len(session['name']) < 1:
        flash('You must enter a name')
    elif len(session['comment']) < 1:
        flash('You must enter a comment')
    elif len(session['comment']) > 120:
        flash('Sorry, your comment is too long')
    else:
        return redirect('/success')

    print len(session['comment'])
    return redirect('/')

@app.route('/success')
def success():
    return render_template('success.html')

app.run(debug=True)
