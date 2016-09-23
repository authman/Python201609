from system.core.controller import *
from time import strftime, time

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
   
    def index(self):
        time=strftime('%B %d, %Y, %I %p')
        return self.load_view('index.html', message=time)

