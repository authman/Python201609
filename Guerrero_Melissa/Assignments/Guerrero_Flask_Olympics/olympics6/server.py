from flask import Flask, render_template, session, request, redirect
import random
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    if not 'gold' in session:
        session['gold'] = 0
    if not 'activities' in session:
        session['activities'] = []
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    buildings = {
        'farm':random.randint(5,10),
        'casino':random.randint(-50,50),
        'cave':random.randint(0,30),
        'house':random.randint(0,5)
    }
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Will this work?
First you would need to import random from Python.
Also need to create a counter for the session 
or keep a total.
Would need to build out HTML to see buildings object.
Also would need to write and route forms accordingly.
"""
