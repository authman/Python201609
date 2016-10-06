"""
	Sample Controller File
	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.
	Create a controller using this template
"""
from system.core.controller import *
import random
from time import strftime
class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)

	def index(self):

		if not 'gold' in session:
			session['gold']= 0
			session['output']=''

		return self.load_view('index.html')



	def process(self):

		

		build=request.form['building']
		
		if build=='Farm':
			turnScore = random.randint(10,20)
			curTime = strftime('%Y/%m/%d %I:%M %p')
			session['gold']+= turnScore
			session['output']='<p class="green"> Earned '+str(turnScore)+' golds from the farm! '+curTime+ '</p>' + session["output"]
		elif build=='Cave':
			turnScore = random.randint(5,10)
			curTime = strftime('%Y/%m/%d %I:%M %p')
			session['gold']+= turnScore
			session['output']='<p class="green"> Earned '+str(turnScore)+' golds from the cave! '+curTime+ '</p>' + session["output"]
		elif build=='House':
			turnScore = random.randint(2,5)
			curTime = strftime('%Y/%m/%d %I:%M %p')
			session['gold']+= turnScore
			session['output']='<p class="green"> Earned '+str(turnScore)+' golds from the house! '+curTime+ '</p>' + session["output"]
		elif build=='Casino':
			turnScore = random.randint(-50,50)
			curTime = strftime('%Y/%m/%d %I:%M %p')
			session['gold']+= turnScore
			if turnScore>=0:
				session['output']='<p class="green"> Nice you got '+str(turnScore)+' gold! Killed it at the Casino! '+curTime+ '</p>' + session["output"]
			else:
				session['output']='<p class="red"> Crap you lost '+str(turnScore)+' golds! Good luck explaining this to the wife '+curTime+ '</p>' + session["output"]

		return redirect('/index')
