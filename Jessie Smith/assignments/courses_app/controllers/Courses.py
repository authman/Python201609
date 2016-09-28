from system.core.controller import *
class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')

    def index(self):
        all_info=self.models['Course'].get_all_courses()
        return self.load_view('index.html', all_info=all_info)

    def show(self, id):
        course = self.models['Course'].get_course_by_id(id)
        return self.load_view('show.html', course=course)

    def add(self):
        course_details = {
            'title': request.form['coursename'],
            'description': request.form['description']
        }

        course_id=self.models['Course'].add_course(course_details)
        return redirect('/')

    def delete(self, course_id):
        course_id = self.models['Course'].delete_course(course_id)
        return redirect('/')

    def destroy(self, course_id):
        course = self.models['Course'].get_course_by_id(course_id) 
        return self.load_view('destroy.html', course=course)

    


    # def update(self, course_id):
    #     # in actuality, data for updating the course would come 
    #     # from a form on our client
    #     course_details = {
    #         'id': course_id,
    #         'title': 'Python 2.0',
    #         'description': 'This course is unreal!'
    #     }
    #     self.models['Course'].update_course(course_details)
    # 


