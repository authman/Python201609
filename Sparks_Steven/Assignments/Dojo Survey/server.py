from flask import Flask, render_template, request, redirect
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
  return render_template("index.html")
# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
@app.route('/survey', methods=['POST'])
def create_survey():
   print "Got Post Info"
   # we'll talk about the following two lines after we learn a little more
   # about forms
   name = request.form['name']
   dojo_location = request.form['dojo_location']
   fave_lang = request.form['fave_lang']
   comment = request.form['comment']
   # redirects back to the '/' route
   return render_template('survey.html', name=name, dojo_location=dojo_location, fave_lang=fave_lang, comment=comment)
   #return redirect('/')
app.run(debug=True) # run our server