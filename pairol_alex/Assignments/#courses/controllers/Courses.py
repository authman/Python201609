from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')
        # self.db = self._app.db

    def index(self):
        # go to db and call index method
        courses = self.models['Course'].index();
        print courses
        return self.load_view('index.html', courses = courses)

    def destroy_confirm(self, id):
        print(id, "our id")
        course = self.models['Course'].show(int(id))
        # print course
        # go to db and call show
        return self.load_view('delete_confirm.html', course = course[0])

    def create(self):
        print request.form
        arguments = {"Title": request.form['Title'], "Description": request.form['Description']}
        self.models['Course'].create(arguments)
        return redirect('/return')



    def delete(self, id):
        # print (id, "duran duran")
        #call to db and delete
        self.models['Course'].delete(int(id))
        return redirect ('/return')
