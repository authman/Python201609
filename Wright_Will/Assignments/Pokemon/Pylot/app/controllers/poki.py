from system.core.controller import *
from random import randint
from time import strftime
class Poki(Controller):
    def __init__(self, action):
        super(gold, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db
    def index(self):
        return self.load_view('index.html')
