from system.core.controller import *
import random
from string import ascii_lowercase
class Surveys(Controller):
    def __init__(self, action):
        super(Surveys, self).__init__(action)
        self.load_model('WelcomeModel')
        self.db = self._app.db

    def index(self):
        locations = ["Seattle","San Diego","Salt Lake","Dallas","New York","Charleston"]
        languages = ["python","Javascript","Java","SQL","C#","C++","PHP","Ruby","F#","Clojure","Haskell"]
        return self.load_view('index.html',locations=locations,languages=languages)
    def process(self):
        if not "count" in session:
            session["count"] = 0
        session["count"] += 1
        session["name"] = request.form["user_name"]
        session["location"] = request.form["location"]
        session["language"] = request.form["language"]
        session["comment"] = request.form["comment"]
        return redirect('/result')
    def process(self):
        hello="goodbye"

        return self.load_view('results.html',name=session['name'],location=session['location'],language=session["language"],comment=session["comment"],count=session["count"])
