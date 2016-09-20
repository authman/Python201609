"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random, string  

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        
    def index(self):
        if not session.has_key('count'):
            session['count'] = 0
        if not session.has_key('randomized'):
            session['randomized'] = 'click the btn to start'
        
        return self.load_view('index.html')
    
    def process(self):
        session['count'] += 1
        session['randomized'] = ''.join(random.sample(string.ascii_letters, 14))
        return redirect('/')

