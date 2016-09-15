from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process/<_id>', methods = ['POST'])
def process(_id):
    print ("I love flask! And {}".format(_id))# id is a built in function changed to _id
    return redirect('/')


if __name__ == '__main__':
  app.run(debug = True)


"""
Will this work?  What
What will this print???
"""
