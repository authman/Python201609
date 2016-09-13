"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random
from string import ascii_lowercase
class Rand_Num(Controller):
    def __init__(self, action):
        super(Rand_Num, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        randword  = ""
        if not 'count' in session:
            session['count'] = 0
        session['count'] += 1
        random_word  = ""
        for x in range(14):
            random_word += random.choice(ascii_lowercase)

        return self.load_view('index.html',randword=random_word)
