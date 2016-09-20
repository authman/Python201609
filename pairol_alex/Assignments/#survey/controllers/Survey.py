from system.core.controller import *

class Survey(Controller):
    def __init__(self, action):
        super(Survey, self).__init__(action)
        self.load_model('SurveyModel')
        self.db = self._app.db
   
    def index(self):
        return self.load_view('index.html')

    def process(self):
        survey = {
                "name": request.form['name'],
                "location": request.form['location'],
                "language": request.form['language'],
                "comment": request.form['comment']
        }

        return self.load_view('result.html', survey = survey)