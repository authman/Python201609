
from system.core.controller import *
import random, string

class Welcome(Controller):
	def __init__(self, action):
		super(Welcome, self).__init__(action)

	def index(self):

		if not session.has_key('count'):
			session['count'] = 0
		if not session.has_key('random'):
			session['random'] = "Click Me!"

		return self.load_view('index.html')

	def process(self):
		session['count'] += 1
		session['random'] = random.choice(string.ascii_letters)

		return redirect('/')


