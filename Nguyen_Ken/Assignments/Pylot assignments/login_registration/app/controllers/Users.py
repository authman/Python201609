#controller for users
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)

        self.load_model('User')
        self.db = self._app.db

    def index(self):

        return self.load_view('index.html')

    def registration(self):
        user_info = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'password_confirmation' : request.form['password_confirmation']
        }

        create_user = self.models['User'].create_user(user_info)

        if create_user['status'] == False:
            if create_user['errors']:
                for error in create_user['errors']:
                    flash(error, 'error')
        elif create_user['status'] == True:
            flash ('Successfully registered!', 'success')
            return self.load_view('success.html', user = create_user['new_user'])

        return redirect('/')

    def login(self):
        user_info = {
            'email' : request.form['email'],
            'password' : request.form['password']
        }
        login_user = self.models['User'].login_user(user_info)

        if login_user:
            flash('Successfully logged in!', 'success')
            return self.load_view('success.html', user = login_user)
        flash('Wrong email or password!', 'error_login')
        return redirect('/')
