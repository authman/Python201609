
from system.core.controller import *


class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)

        self.load_model('WelcomeModel')

   
    def index(self):
        session.clear()
        if 'first_name' in session:
            return redirect('/success') 
        return self.load_view('index.html')

    def process(self):
        if request.form['form_type'] == 'registration':
            user_info={
                'first_name' : request.form['first_name'],
                'last_name' : request.form['last_name'],
                'email' : request.form['email'],
                'password' : request.form['password'],
                'confirm_password' : request.form['confirm_password']
            }
            create_status = self.models['WelcomeModel'].create_user(user_info)
            
            if create_status['status'] == True:
                session['id'] = create_status['user']['id']
                session['first_name'] = create_status['user']['first_name']
                return redirect ('/success')
            else:
                for message in create_status['errors']:
                    flash(message)
                return redirect ('/')
        else:
            if len(request.form['email'])<1:
                flash("Email was too short")
                return redirect ('/') 
            
            if len(request.form['password']) <1:
                flash("Password was too short") 
                return redirect ('/')


            user = self.models['WelcomeModel'].get_user_by_email(request.form['email'])
            if len(user) == 0:
                flash("You don't exist")
                return redirect ('/')

            session['first_name'] = user[0]['first_name'] 
            return redirect('/success')



    def success(self):
        return self.load_view('/success.html')



