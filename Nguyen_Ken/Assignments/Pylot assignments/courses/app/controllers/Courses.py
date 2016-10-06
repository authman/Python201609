
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)

        self.load_model('Course')
        self.db = self._app.db



    def index(self):
        allCourses = self.models['Course'].get_courses()
        return self.load_view('index.html', allCourses=allCourses)

    def add(self):
        if len(request.form['name']) < 15:
            flash('The course name must be at least 15 characters', 'error')
        else:
            name = request.form['name']
            description = request.form['description']

            add_course = {
                'name' : name,
                'description' : description
            }

            self.models['Course'].add_course(add_course)

        return redirect('/')

    def destroy(self, course_id):

        course = self.models['Course'].get_course(course_id)

        return self.load_view('destroy.html', course = course)

    def delete(self, course_id):

        self.models['Course'].delete_course(course_id)

        return redirect('/')
