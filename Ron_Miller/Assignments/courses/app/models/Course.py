""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model

class Course(Model):
	def __init__(self):
		super(Course, self).__init__()
	

	def get_courses(self):
		query = "SELECT * from course ORDER BY created_on DESC"
		return self.db.query_db(query)

	def add_info(self,info):
		sql = "INSERT into course (name, description, created_on) values(:name,:description, now())"
		data = info
		self.db.query_db(sql, data)
		return True

	def get_course(self,_id):
		query = "SELECT * from course WHERE id = :id"
		data = {'id':_id} 
		return self.db.query_db(query,data)	

	def del_course(self,_id):
		sql = "DELETE FROM course WHERE id=:id"
		data={'id':_id}
		self.db.query_db(sql, data)
		return True