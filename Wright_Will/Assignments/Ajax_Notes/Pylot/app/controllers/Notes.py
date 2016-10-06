from system.core.controller import *

class Notes(Controller):
    def __init__(self, action):
        super(Notes, self).__init__(action)
        self.load_model('Note')
        self.db = self._app.db

    def index(self):
        notes = self.models['Note'].notes()
        return self.load_view('index.html',notes=notes)

    def create(self):
        new_post = {
            "title":request.form['title'],
            "description":request.form['description']
        }
        self.models['Note'].add(new_post)
        return redirect("/notes/html")
    def notes_html(self):
        notes = self.models['Note'].notes()
        return self.load_view('/partials/notes.html',notes=notes)

    def update(self):
        edit_post = {
            "title":request.form['titel'],
            "description":request.form['description']
        }
        return redirect("/")

    def destroy(self,_id):
        self.models['Note'].destroy(_id)
        return redirect("notes/html")
