
from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)

        self.load_model('Note')



    def index(self):
        notes = self.models['Note'].get_all_notes()
        return self.load_view('index.html', notes = notes)

    def addTitle(self):
        data = {
            'title' : request.form['title']
            }
        self.models['Note'].addTitle(data)
        notes = self.models['Note'].get_all_notes()
        return self.load_view('/partial/notes.html', notes = notes)

    def addDescription(self):
        data = {
            'description' : request.form['description'],
            'id' : request.form['id']
            }
        self.models['Note'].addDescription(data)
        notes = self.models['Note'].get_all_notes()
        return self.load_view('/partial/notes.html', notes = notes)

    def delete(self):
        data = {
            'id' : request.form['id']
            }
        self.models['Note'].delete_note(data)
        notes = self.models['Note'].get_all_notes()
        return self.load_view('/partial/notes.html', notes = notes)
