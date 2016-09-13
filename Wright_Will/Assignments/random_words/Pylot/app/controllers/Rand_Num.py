"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from random import randint
import string
class Rand_Num(Controller):
    def __init__(self, action):
        super(Rand_Num, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db


    def index(self):
        randword  = ""
        print string.ascii_letters
        # for x in range(14):
        #     randword += randInt()
        return self.load_view('index.html')
