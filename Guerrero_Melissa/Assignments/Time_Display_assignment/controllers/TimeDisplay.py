from system.core.controller import *
from time import strftime
class TimeDisplay(Controller):
	def __init__(self, action):
		super(TimeDisplay, self).__init__(action)
	def timedate(self):
		time_date = strftime('%b %d, %Y %I %p')
	def index(self):
		time_date = strftime('%b %d, %Y %I %p')	
		return self.load_view('/time_display_index.html', message=time_date)