from system.core.controller import *
from random import randint
from time import strftime
class Login_Reg(Controller):
    def __init__(self, action):
        super(Login_Reg, self).__init__(action)
        self.load_model('Login_Ref')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def login(self):

        if error:
            return redirect("/")

        return redirect("/success")
    def register(self):

        if error:
            return redirect("/")

        return redirect("/success")
    def success(self):

        return self.load_view('success.html')
