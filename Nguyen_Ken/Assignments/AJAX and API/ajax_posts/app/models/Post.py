
from system.core.model import Model

class Post(Model):
    def __init__(self):
        super(Post, self).__init__()

    def get_all(self):
        query = 'SELECT * FROM post'
        return self.db.query_db(query)

    def create_post(self, info):
        data = {
            'description' : info['description']
            }

        insert_query = 'INSERT INTO post (description, created_at, updated_at) VALUES (:description, NOW(), NOW())'

        return self.db.query_db(insert_query, data)
