#server
from flask import Flask, render_template, request,redirect,flash
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/results',methods = ["post"])
def results():
    name =request.form['name']
    location = request.form['location']
    language = request.form['language']
    comment =request.form['comment']
    if len(name) < 1:
        flash('name must not be blank')
        #return redirect('/')
    if len(comment) < 1:
        flash('comment must not be blank')
        #return redirect('/')
    if len(comment) > 120:
        flash('comment can not be larger than 120 charachters')
        #return redirect('/')

    return render_template("results.html",name=name,location=location,language=language,comment=comment)
@app.route('/process', methods=['POST'])

app.run(debug=True)
