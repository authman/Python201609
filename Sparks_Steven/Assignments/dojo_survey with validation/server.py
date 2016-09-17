from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
   working = True
   if len(request.form['name'])<1:
      flash("Name cannot be empty")
      working = False

   if len(request.form['comment'])>120:
      flash("Comments limited to 120 characters")
      working = False

   if not working:
      return redirect('/')

   session['name'] = request.form['name']
   session['dojo_location'] = request.form['dojo_location']
   session['fave_lang'] = request.form['fave_lang']
   session['comment'] = request.form['comment']

   return redirect('/survey')

@app.route('/survey')
def create_survey():

   return render_template('survey.html', name=session['name'], dojo_location=session['dojo_location'], fave_lang=session['fave_lang'], comment=session['comment'])



app.run(debug=True)