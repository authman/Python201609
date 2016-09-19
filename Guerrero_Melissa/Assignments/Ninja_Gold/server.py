from flask import Flask, render_template, request, redirect, session
import random, time
app = Flask(__name__)
app.secret_key = "TopSecret"
arr = []
mydatetime=time.localtime()
timevar= time.strftime('%b %d %Y %H:%M:%S', time.localtime())

@app.route('/')
def index():
  return render_template("index.html", messages=arr)

@app.route('/process_money', methods=['POST'])
def process_money():
   if not session.has_key('count'):
      session['count'] = 0
   if request.form['building'] == 'farm':
      num = random.randrange(10, 21)
      session['count'] += num
      message = 'Earned ' + str(num) + ' golds from the farm! ' + time.strftime('%b %d %Y %H:%M:%S', time.localtime())
   elif request.form['building'] == 'cave':
      num = random.randrange(5, 11)
      session['count'] += num
      message = 'Earned ' + str(num) + ' golds from the cave! ' + time.strftime('%b %d %Y %H:%M:%S', time.localtime())
   elif request.form['building'] == 'house':
      num = random.randrange(2, 6)
      session['count'] += num
      message = 'Earned ' + str(num) + ' golds from the house! ' + time.strftime('%b %d %Y %H:%M:%S', time.localtime())
   elif request.form['building'] == 'casino':
      num = random.randrange(-50, 51)
      session['count'] += num
      if num > 0:
         message = 'Earned ' + str(num) + ' golds from the casino! ' + time.strftime('%b %d %Y %H:%M:%S', time.localtime())
      elif num < 0:
         message = 'Lost ' + str(num) + ' golds from the casino! ' + time.strftime('%b %d %Y %H:%M:%S', time.localtime())
   
   arr.append(message)
   return redirect('/')

app.run(debug=True) 