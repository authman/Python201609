
from system.core.model import Model
import re

class Login_Reg(Model):
    def __init__(self):
        super(Login_Reg, self).__init__()


    def create_user(self,info):

        errors = []
        all_users = self.get_users()
        if not re.match(r"[A-z]{2,}",info['fname']):
            errors.append("first name must be at least 2 charachters long")
        if not re.match(r"[A-z]{2,}",info['lname']):
            errors.append("last name must be at least 2 charachters long")
        if len(info['password']) < 8:
            errors.append("password must be at least 8 charachters long")
        if not re.match(r"[A-z]+[A-z_0-9]*\@[A-z]+\.[A-z]",info['email']):
            errors.append("Not a valid Email")
        elif [user['email'] for user in all_users if user['email'] == info['email']]:
            errors.append("Email already has an account")
        if info['password'] != info['conf_password']:
            errors.append("confirm password did not match password")
        if errors:
            return {"status": False, "errors": errors}
        info['pw_hash'] = self.bcrypt.generate_password_hash(info['password'])
        query = "INSERT into  user (first_name, last_name, email, password) VALUES (:fname, :lname, :email, :pw_hash) "
        _id = self.db.query_db(query,info)
        return {"status":True,"user_id":_id}

    def get_users(self):
        query = "SELECT * from user"
        return self.db.query_db(query)

    def login_valid(self,info):
        errors = []
        user_data = self.get_user_by_email(info['email'])
        # password length validation
        if len(info['password']) < 8:
            errors.append("password must be at least 8 charachters long")
        # email validation
        if not re.match(r"[A-z]+[A-z_0-9]*\@[A-z]+\.[A-z]",info['email']):
            errors.append("Not a valid Email")
        # email exist in db
        elif not user_data:
            errors.append("We couldn't find that email")
        # check password works
        if not self.bcrypt.check_password_hash(user_data['password'], info['password']):
            errors.append("wrong password")
        if errors:
            return {"status": False, "errors": errors}
        return {"status": True}

    def get_user_by_email(self,email):
        query = "SELECT * from user where email = :email"
        data = {'email': email}
        return self.db.get_one(query, data)
