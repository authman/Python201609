from system.core.controller import *
import random
from string import ascii_lowercase
class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        hello="hello"

        return self.load_view('index.html',hello=hello)
