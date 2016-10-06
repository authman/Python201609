from flask import Flask, render_template,session, request
app = Flask(__name__)
app.secret_key = 'my_secret_key'

@app.route('/')
def myfirstfunction():
    if not 'title' in session:
        session['title'] = 'hello world'
    if not 'name' in session:
        session['name'] = "Mike"
    return render_template('index.html', name=session['name'])

@app.route('/do_something')
def mysecondfunction():
    print request.form
    session['title'] = request.form['title']
    session['name'] = "Fred"
    return redirect('/') #should redirect to "/"

if __name__ == '__main__':
  app.run(debug = True)
