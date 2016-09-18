
from system.core.model import Model

class post(Model):
    def __init__(self):
        super(post, self).__init__()

    def all(self):
        query = "SELECT * from post"
        return self.db.query_db(query)

    # def get_post(self):
    #     query = "SELECT * from post where id = :id"
    #     data = {'id': 1}
    #     return self.db.get_one(query, data)

    def add(self,post):
        sql = "INSERT INTO ajax_posts.post (text) VALUES (:post);"
        data = {'post': post}
        _id = self.db.query_db(sql, data)
        return _id

    def delete(self,_id):
        query = "DELETE * from post where id = :id"
        data = {'id': _id}
        return self.db.query_db(query, data)
