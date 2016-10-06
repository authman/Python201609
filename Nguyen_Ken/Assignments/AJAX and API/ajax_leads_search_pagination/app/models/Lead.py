
from system.core.model import Model
import datetime

class Lead(Model):
    def __init__(self):
        super(Lead, self).__init__()

    def get_all_leads(self):
        query = 'SELECT * FROM leads'
        return self.db.query_db(query)

    def search_leads(self, info):
        print info['fromDate']
        print info['toDate']
        data = {
            'name' : info['name'],
            'fromDate' : None,
            'toDate' : None
        }
        if info['fromDate']:
            struct_from =  datetime.datetime.strptime(info['fromDate'],"%m/%d/%Y")
            fromD = struct_from.strftime("%Y-%m-%d")
            data['fromDate'] = fromD

        if info['toDate']:
            struct_to =  datetime.datetime.strptime(info['toDate'],"%m/%d/%Y")
            toD = struct_to.strftime("%Y-%m-%d") #idk why i was trying to convert both to y/m/d when the db was in y-m-d already!
            data['toDate'] = toD


        query = 'SELECT * FROM leads WHERE (first_name LIKE CONCAT("%",:name,"%") OR last_name LIKE CONCAT("%",:name,"%")) AND registered_datetime BETWEEN IFNULL(:fromDate,"2001-01-01 00:00:00") AND IFNULL(:toDate,NOW()); '
            #instructor magic..

        return self.db.query_db(query, data)
