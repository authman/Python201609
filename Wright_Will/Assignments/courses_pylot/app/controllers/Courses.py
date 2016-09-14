from system.core.controller import *
from random import randint
from time import strftime
class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Courses')
        self.db = self._app.db

    def index(self):
        data = self.models['Courses'].get_all_courses()
        return self.load_view('index.html',data=data)

    def add(self):
        course = {"name":request.form['course_name'],"description":request.form['course_description']}
        self.models['Courses'].add_course(course)
        return redirect("/")

    def destroy(self,_id):
        self.models['Courses'].delete_course(_id)
        return redirect("/")
    def destroy_course(self,_id):

        return self.load_view('destroy_course.html',_id=_id)
