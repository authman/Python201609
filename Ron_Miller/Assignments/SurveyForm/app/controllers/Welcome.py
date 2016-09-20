"""
	Sample Controller File
	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.
	Create a controller using this template
"""
from system.core.controller import *


class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)


	def index(self):
		if not 'count' in session:
			session['count']=0


		return self.load_view('index.html')

	def process(self):

		session['userName']=request.form['name']
		session['lang']=request.form['favLang']
		session['loc']=request.form['location']
		session['com']=request.form['comment']


		return redirect('/results')

	def result(self):
		session['count']+=1

		return self.load_view('results.html')



