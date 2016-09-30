
from system.core.controller import *

class Maps(Controller):
    def __init__(self, action):
        super(Maps, self).__init__(action)


    def index(self):

        return self.load_view('index.html')

    def get_directions(self):

        origin = request.form['from']
        destination = request.form['to']
        data = {
            'origin' : origin,
            'destination' : destination
            }

        url = "https://maps.googleapis.com/maps/api/directions/json?"+urlencode(data)+"&sensor=false&key=AIzaSyD1yZkrGqVRr9FPTOu8GFHzNEgO8kjBzZs"

        response = requests.get(url).content
            #request json from api thru our server, not the front end -- then we return the json object to the front end

        return response
