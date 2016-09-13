from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = "TopSecret"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_user():
   if len(request.form['name']) < 1:
   	flash('Name cannot be empty!')
   else:
   	flash('Success! Your name is {}'.format(request.form['name']))
   location = request.form['location']
   language = request.form['language']
   if len(request.form['comment']) > 120:
   	flash('Please leave comments of 120 characters or fewer.')
   else:
   	flash('Thank you for your comment.')
   return redirect('/')

app.run(debug=True) 