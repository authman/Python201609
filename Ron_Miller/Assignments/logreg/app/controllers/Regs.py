"""
	Sample Controller File
	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.
	Create a controller using this template
"""
from system.core.controller import *
class Regs(Controller):
	def __init__(self, action):
		super(Regs, self).__init__(action)

		self.load_model('Reg')
	
	def index(self):
		if not 'user' in session:
			return self.load_view('index.html')
		else:
			return redirect('/success')

	def register(self):
		userInfo = {
			 "fName" : request.form['fName'],
			 "lName" : request.form['fName'],
			 "email" : request.form['email'],
			 "password" : request.form['password'],
			 "pw_confirmation" : request.form['pw_confirmation']
		}
		createStatus=self.models['Reg'].register(userInfo)
		if createStatus['status']== True:
			session['id']=createStatus['user']['id']
			session['fName']=createStatus['user']['fName']
			return redirect('/success')
		else:
			for message in createStatus['errors']:
				flash(message)
			return redirect('/')

	def login(self):
		userInfo = {
			 "email" : request.form['email'],
			 "password" : request.form['password']
		}
		user=self.models['Reg'].login(userInfo)
		session['fName']=user['fName']
		return redirect('/success')

	def success(self):
		print "Hello this is a test"
		return self.load_view('success.html')
