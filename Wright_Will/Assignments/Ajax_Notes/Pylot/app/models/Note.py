
from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def notes(self):
        query = "SELECT * from note"
        return self.db.query_db(query)

    def note(self,_id):
        query = "SELECT * from note where id = :id"
        data = {'id': _id}
        return self.db.get_one(query, data)

    def add(self,new_post):
        sql = "INSERT INTO note (title, description) values(:title, :description)"
        return self.db.query_db(sql, new_post)

    def destroy(self,_id):
        query = "DELETE  FROM note WHERE id = :id"
        data = {'id':_id}
        return self.db.query_db(query, data)
