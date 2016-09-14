from system.core.controller import *
from random import randint
from time import strftime
class Login_Reg(Controller):
    def __init__(self, action):
        super(Login_Reg, self).__init__(action)
        self.load_model('Login_Reg')
        self.db = self._app.db

    def index(self):
        return self.load_view('index.html')

    def login(self):
        return redirect("/success")
    def register(self):
        session['fname'] = request.form['fname']
        session['lname'] = request.form['lname']
        session['email'] = request.form['email']
        user_info = {
         "fname" : request.form['fname'],
         "lname" : request.form['lname'],
         "email" : request.form['email'],
         "password" : request.form['password'],
         "conf_password" :  request.form['conf_password']
        }
        create_status = self.models['Login_Reg'].create_user(user_info)

        if create_status['status']:
            return redirect("/success")

        for error in create_status['errors']:
            flash(error,'register')
        return redirect("/")
    def login(self):
        session['email'] = request.form['email']
        info= {
          "email": request.form['email'],
          "password": request.form['password']
        }


        errors = self.models['Login_Reg'].login_valid(info)
        if not errors['status']:
            for error in errors['errors']:
                flash(error,"login")
            return redirect("/")
        return redirect("/success")
    def success(self):

        return self.load_view('success.html')
    def logout(self):
        session.clear()
        return redirect("/")
