from system.core.controller import *

class posts(Controller):
    def __init__(self, action):
        super(posts, self).__init__(action)
        self.load_model('post')
        self.db = self._app.db

    def index(self):

        return self.load_view('index.html')

    def create(self):

        return redirect("/")
