"""
	Sample Controller File
	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.
	Create a controller using this template
"""
from system.core.controller import *
import string
import random

class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)

		session['word']=''
		for i in range (10):
			session['word']+=random.choice(string.letters+string.digits)
		"""
			This is an example of loading a model.
			Every controller has access to the load_model method.
			self.load_model('WelcomeModel')
		"""
	""" This is an example of a controller method that will load a view for the client """
	def index(self):
		if not session['count']:
			session['count'] =0		
		""" 
		A loaded model is accessible through the models attribute 
		self.models['WelcomeModel'].get_all_users()
		"""
		return self.load_view('index.html')

	def process(self):

		session['count']+=1

		return redirect('/landing')



