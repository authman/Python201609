from system.core.controller import *
from time import strftime, gmtime
class Times(Controller):
    def __init__(self, action):
        super(Times, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        current_time = strftime("%b %d, %Y %H:%M:%S", gmtime())

        return self.load_view('index.html', current_time=current_time)
