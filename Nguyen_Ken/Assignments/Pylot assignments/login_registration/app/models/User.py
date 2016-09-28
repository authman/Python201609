#model for user
from system.core.model import Model
import re

class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def create_user(self, user):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\.\_-]+\.[a-zA-Z]+$')
        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        #time for validations
        errors = []

        if not user['first_name']:
            errors.append('Name cannot be blank')
        elif len(user['first_name']) < 2:
            errors.append('Name must be longer than 2 characters')
        elif not NAME_REGEX.match(user['first_name']):
            errors.append('Name cannot contain numbers or special characters')
        if not user['last_name']:
            errors.append('Last name cannot be blank')
        elif len(user['last_name']) < 2:
            errors.append('Last name must be longer than 2 characters')
        elif not NAME_REGEX.match(user['last_name']):
            errors.append('Last name cannot contain numbers or special characters')
        if not user['email']:
            errors.append('Email field cannot be blank')
        elif not EMAIL_REGEX.match(user['email']):
            errors.append('Email must be a valid email')
        if not user['password']:
            errors.append('Please enter your desired password')
        elif len(user['password']) < 8:
            errors.append('Password must be longer than 8 characters')
        elif user['password'] != user['password_confirmation']:
            errors.append('Password and confirmation must match!')

        if errors:
            return {'status' : False, 'errors' : errors}
        else:
            password = user['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)

            ######create user query
            create_data = {
                'first_name' : user['first_name'],
                'last_name' : user['last_name'],
                'email' : user['email'],
                'pw_hash' : hashed_pw
            }
            create_query = 'INSERT INTO user (first_name, last_name, email, pw_hash, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, NOW(), NOW())'
            user_id = self.db.query_db(create_query, create_data) #should return new user id

            ######get user query
            get_user_data = {
                'id' : user_id
            }
            get_user_query = 'SELECT * FROM user WHERE id = :id LIMIT 1'
            new_user = self.db.query_db(get_user_query, get_user_data)

            return {'status' : True, 'new_user' : new_user[0]}


    def login_user(self, info):
        password = info['password']
        get_user_data = {
            'email' : info['email'],
            'password' : info['password']
        }
        get_user_query = 'SELECT * FROM user WHERE email = :email LIMIT 1'

        user = self.db.query_db(get_user_query, get_user_data)

        if user:
            if self.bcrypt.check_password_hash(user[0]['pw_hash'], password):
                return user[0]

        return False
