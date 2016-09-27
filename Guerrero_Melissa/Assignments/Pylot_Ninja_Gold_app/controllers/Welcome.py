
from system.core.controller import *
import random
from datetime import datetime

class Welcome(Controller):
    def __init__(self, action):
        super(Welcome, self).__init__(action)
        
   
    def index(self):
        if not 'gold' in session:
            session['gold'] = 0
        if not 'log' in session: 
            session['log'] = ''
        return self.load_view('index.html', gold = session['gold'], log = session['log'])
    
    def process_money(self):
        if not 'building' in request.form:
            return redirect('/')
        
        val = 0

        if request.form['building'] == 'farm':
            val += random.randrange(10, 21)
            
        elif request.form['building'] == 'cave':
            val += random.randrange(5, 11)
            
        elif request.form['building'] == 'house':
            val += random.randrange(2, 6)
            
        elif request.form['building'] == 'casino':
            val += random.randrange(-50, 51)
        
        session['gold'] += val   

        if val < 0:
            session['log'] = '<p style="color:red;">Lost '+str(val)+' golds from the '+request.form['building']+ '! '+datetime.now().strftime('%x %I:%M')+ '</p>' + session['log']
        else:
            session['log'] = '<p style="color:green;">Earned '+str(val)+' golds from the '+request.form['building']+ '! '+datetime.now().strftime('%x %I:%M')+ '</p>' + session['log']
        return redirect('/')

    def reset(self):
        session.clear()
        return redirect('/')
