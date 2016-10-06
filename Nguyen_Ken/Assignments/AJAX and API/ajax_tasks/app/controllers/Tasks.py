
from system.core.controller import *

class Tasks(Controller):
    def __init__(self, action):
        super(Tasks, self).__init__(action)

        self.load_model('Task')



    def index(self):
        tasks = self.models['Task'].get_all_tasks()
        return self.load_view('index.html', tasks = tasks)

    def add(self):
        data = {
            'name' : request.form['name']
        }

        self.models['Task'].add_task(data)
        tasks = self.models['Task'].get_all_tasks()
        return self.load_view('/partial/task.html', tasks = tasks)

    def edit(self):
        data = {
            'id' : request.form['id'],
            'name' : request.form['name']
            }

        self.models['Task'].edit_task(data)
        tasks = self.models['Task'].get_all_tasks()
        return self.load_view('/partial/task.html', tasks = tasks)
