from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'frank'

@app.route('/')
def home():
    print session.has_key('count')
    if not session.has_key('count'):
            session['count'] = 1
    else:
        session['count'] += 1
    return render_template("index.html")
@app.route('/incre')
def incre():
    session['count'] += 1
    return redirect("/")
@app.route('/reset')
def reset():
    if session.has_key:
        del session['count']
    return redirect("/")

app.run(debug=True)
