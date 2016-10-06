"""
    Sample Model File

    A Model should be in charge of communicating with the Database.
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class Courses(Model):
    def __init__(self):
        super(Courses, self).__init__()

    # Below is an example of a model method that queries the database for all users in a fictitious application
    #
    # Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM course ORDER BY created_at DESC")

    def get_course_by_id(self, course_id):
        # pass data to the query like so
        query = "SELECT * FROM course WHERE id = :course_id"
        data = { 'course_id': course_id}
        return self.db.query_db(query, data)

    def add_course(self, course):
      query = "INSERT INTO course (name, Desctription) VALUES (:name, :description)"
      data = { 'name': course['name'], 'description': course['description'] }
      return self.db.query_db(query, data)

    def update_course(self, course):
      # Building the query for the update
      query = "UPDATE course SET title=:title, description=:description WHERE id = :course_id"
      # we need to pass the necessary data
      data = { 'title': course['title'], 'description': course['description'], 'course_id': course['id']}
      # run the update
      return self.db.query_db(query, data)

    def delete_course(self, course_id):
      query = "DELETE FROM course WHERE id = :course_id"
      data = { "course_id": course_id }
      return self.db.query_db(query, data)
