from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def count_page_visits():
	if not session.has_key('count'):
		session['count'] = 0
	session['count'] += 1
	return render_template("index.html", count=session['count'])

app.run(debug=True)