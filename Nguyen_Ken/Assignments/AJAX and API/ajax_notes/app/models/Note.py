
from system.core.model import Model

class Note(Model):
    def __init__(self):
        super(Note, self).__init__()

    def get_all_notes(self):
        query = 'SELECT * FROM note'
        return self.db.query_db(query)

    def addTitle(self, info):
        data = {
            'title' : info['title']
            }

        insert_title_query = 'INSERT INTO note (title, created_at, updated_at) VALUES (:title, NOW(), NOW());'

        return self.db.query_db(insert_title_query, data)

    def addDescription(self, info):
        data = {
            'description' : info['description'],
            'id' : info['id']
            }

        update_description_query = 'UPDATE note SET description = :description, updated_at = NOW() WHERE id = :id;'
        return self.db.query_db(update_description_query, data)

    def delete_note(self, info):
        data = {
            'id' : info['id']
            }
        delete_query = 'DELETE FROM note WHERE id = :id;'
        return self.db.query_db(delete_query, data)
