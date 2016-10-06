from system.core.controller import *

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        self.load_model('WelcomeModel')
        
    def index(self):
        return self.load_view('index.html')

    def create_user(self):
        #errors = []
        if request.form['form_type'] == 'registration':
            user_info = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : request.form['password'],
            'confirmpw' : request.form['confirmpw']
            }
            create_status=self.models['WelcomeModel'].create_user(user_info)
            
            if create_status['status']==True:
                session['id']=create_status['user']['id']
                session['first_name']=create_status['user']['first_name']
                return redirect('/success')
            else:
                for message in create_status['errors']:
                    flash(message, 'regis_errors')
                    #errors.append('Try again.')
                return redirect ('/')
    
    def login_user(self):
        
            user = self.models['WelcomeModel'].get_user_by_email(request.form['email'], request.form['pwd'])


            if user['status']==True:
                session['user_id'] = user['user']['id'] 
                return redirect('/success')
            else:
                flash('Invalid credentials')
                return redirect ('/')
    
    def success(self):
        return self.load_view('success.html')

 

