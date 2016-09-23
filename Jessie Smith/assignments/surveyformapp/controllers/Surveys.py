
from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

    def index(self):
        if not session.has_key('count'):
            session['count'] = 0

        return self.load_view('index.html')

    def process(self):
        session['count'] += 1
        session['name']=request.form['name']
        session['location']=request.form['location']
        session['language']=request.form['language']
        session['comment']=request.form['comment']
      
        return redirect('/result')

    def result(self):

        return self.load_view('result.html')







