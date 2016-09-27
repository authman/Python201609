""" 
	Sample Model File

	A Model should be in charge of communicating with the Database. 
	Define specific model method that query the database for information.
	Then call upon these model method in your controller.

	Create a model using this template.
"""
from system.core.model import Model
import re
class Reg(Model):
	def __init__(self):
		super(Reg, self).__init__()


	def register(self, info):
		# We write our validations in model functions.
		# They will look similar to those we wrote in Flask
		EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
		errors = []
		# Some basic validation
		if not info['fName']:
			errors.append('Name cannot be blank')
		elif len(info['fName']) < 2:
			errors.append('Name must be at least 2 characters long')
		if not info['lName']:
			errors.append('Name cannot be blank')
		elif len(info['lName']) < 2:
			errors.append('Name must be at least 2 characters long')
		if not info['email']:
			errors.append('Email cannot be blank')
		elif not EMAIL_REGEX.match(info['email']):
			errors.append('Email format must be valid!')
		if not info['password']:
			errors.append('Password cannot be blank')
		elif len(info['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		elif info['password'] != info['pw_confirmation']:
			errors.append('Password and confirmation must match!')
		# If we hit errors, return them, else return True.
		if errors:
			return {"status": False, "errors": errors}
		else:
			password = info['password']
			hashed_pw = self.bcrypt.generate_password_hash(password)
			createQuery = "INSERT INTO user (fName, lName, email, password, created_at) VALUES (:fName, :lName, :email, :password, NOW())"
			createData = {'fName': info['fName'], 'lName': info['lName'], 'email':info['email'], 'password': hashed_pw}
			self.db.query_db(createQuery, createData)

			getUserQuery = "SELECT * FROM user ORDER BY id DESC LIMIT 1"
			users = self.db.query_db(getUserQuery)
			return { "status": True, "user": users[0] }

	def login(self, info):
		password = info['password']
		userQuery = "SELECT * FROM user WHERE email = :email LIMIT 1"
		userData = {'email': info['email']}
 
		user = self.db.get_one(userQuery, userData)
		if user:
		   # check_password_hash() compares encrypted password in DB to one provided by user logging in
			if self.bcrypt.check_password_hash(user.password, password):
				return user
		# Whether we did not find the email, or if the password did not match, either way return False
		return False







	"""
	Below is an example of a model method that queries the database for all users in a fictitious application
	
	Every model has access to the "self.db.query_db" method which allows you to interact with the database

	def get_users(self):
		query = "SELECT * from users"
		return self.db.query_db(query)

	def get_user(self):
		query = "SELECT * from users where id = :id"
		data = {'id': 1}
		return self.db.get_one(query, data)

	def add_message(self):
		sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
		data = {'message': 'awesome bro', 'users_id': 1}
		self.db.query_db(sql, data)
		return True
	
	def grab_messages(self):
		query = "SELECT * from messages where users_id = :user_id"
		data = {'user_id':1}
		return self.db.query_db(query, data)

	"""