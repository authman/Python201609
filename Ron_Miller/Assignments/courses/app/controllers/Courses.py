"""
	Sample Controller File
	A Controller should be in charge of responding to a request.
	Load models to interact with the database and load views to render them to the client.
	Create a controller using this template
"""
from system.core.controller import *
class Courses(Controller):
	def __init__(self, action):
		super(Courses, self).__init__(action)

		self.load_model('Course')

	
	def index(self):

		courseDict=self.models['Course'].get_courses()
		print courseDict
		return self.load_view('index.html',classList=courseDict)



	def process(self):
		if len(request.form['name'])<15:
			flash("Course Name must be longer than 15 characters")
		else:
			course={
				'name':request.form['name'],
				'description': request.form['comment'],
			}
			self.models['Course'].add_info(course)
		return redirect('/')


	def confirmation(self,_id):
		
		getCourse =self.models['Course'].get_course(_id)

		return self.load_view('destroy.html',getCourse = getCourse[0])

	
	def delCourse(self,_id):

		delCourse=self.models['Course'].del_course(_id)

		return redirect('/')