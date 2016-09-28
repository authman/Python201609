
from system.core.model import Model

class Task(Model):
    def __init__(self):
        super(Task, self).__init__()

    def get_all_tasks(self):
        query = 'SELECT * FROM task;'
        return self.db.query_db(query)

    def add_task(self, info):
        data = {
            'name' : info['name']
        }

        insert_query = 'INSERT INTO task (name, created_at, updated_at) VALUES (:name, NOW(), NOW());'

        return self.db.query_db(insert_query, data)

    def edit_task(self, info):
        data = {
            'id' : info['id'],
            'name' : info['name']
        }

        edit_query = 'UPDATE task SET name=:name WHERE id=:id;'

        return self.db.query_db(edit_query, data)
