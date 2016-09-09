from flask import Flask, redirect, render_template,session
app = flask(__name__)
app.secret_key = "fred"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/friends')
def create():
    return redirect()
@app.route('/friends/<id>/edit')
def edit(id):
    return redirect()
@app.route('/friends/<id>')
def update(id):
    return redirect()
@app.route('/friends/<id>/delete')
def destroy(id):
    return redirect()

app.run(debug==True)
