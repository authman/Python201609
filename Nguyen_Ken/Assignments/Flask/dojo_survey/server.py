from flask import Flask, render_template, request, redirect, session
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

    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

app.run(debug=True)
