
from system.core.controller import *

class Leads(Controller):
    def __init__(self, action):
        super(Leads, self).__init__(action)

        self.load_model('Lead')




    def index(self):


        return self.load_view('index.html')

    def loadLeads(self):
        all_leads = self.models['Lead'].get_all_leads()
        return self.load_view('/partial/leads.html', leads = all_leads)

    def search(self):
        data = {
            'name' : request.form['name'],
            'fromDate' : request.form['fromDate'],
            'toDate' : request.form['toDate']
        }

        leads = self.models['Lead'].search_leads(data)
        return self.load_view('/partial/leads.html', leads = leads)
