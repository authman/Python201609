
from system.core.controller import *

class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db



    def index(self):

        return self.load_view('index.html')

    def process(self):
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']

        return redirect('/Surveys/result')

    def result(self):
        if not 'count' in session:
            session['count'] = 0
        session['count'] += 1


        return self.load_view('result.html')
