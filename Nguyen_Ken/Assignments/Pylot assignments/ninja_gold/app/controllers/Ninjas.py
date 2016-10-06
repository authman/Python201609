
from system.core.controller import *
import random
import time

class Ninjas(Controller):
    def __init__(self, action):
        super(Ninjas, self).__init__(action)

        self.load_model('WelcomeModel')
        self.db = self._app.db



    def index(self):
        #session initializers
        if not 'gold' in session:
            session['gold'] = 0
            session['activities'] = []

        sessionActivities = session['activities']

        # session.pop('activities')
        # session.pop('gold')

        return self.load_view('index.html', sessionActivities = sessionActivities)

    def process_money(self):

        if request.form['building'] == 'farm':
            curTime = str(time.strftime('%Y/%m/%d %I:%M%p',time.localtime(time.time())))
            gold = random.randint(10,20)
            session['gold'] += gold
            earned = ['Earned '+str(gold)+' golds from the farm! '+curTime, 'green']
            session['activities'].append(earned) #+ session['activities']



        if request.form['building'] == 'cave':
            curTime = str(time.strftime('%Y/%m/%d %I:%M%p',time.localtime(time.time())))
            gold = random.randint(5,10)
            session['gold'] += gold
            earned = ['Earned '+str(gold)+' golds from the cave! '+curTime, 'green']
            session['activities'].append(earned) #+ session['activities']


        if request.form['building'] == 'house':
            curTime = str(time.strftime('%Y/%m/%d %I:%M%p',time.localtime(time.time())))
            gold = random.randint(2,5)
            session['gold'] += gold
            earned = ['Earned '+str(gold)+' golds from the House! Silly thieves.. '+curTime, 'green']
            session['activities'].append(earned) #+ session['activities']


        if request.form['building'] == 'casino':
            curTime = str(time.strftime('%Y/%m/%d %I:%M%p',time.localtime(time.time())))
            gold = random.randint(-50,50)
            session['gold'] += gold
            if gold >= 0:
                earned = ['Earned '+str(gold)+' golds from the casino! Dirty gambling hippies.. '+curTime, 'green']
                session['activities'].append(earned) #+ session['activities']
            elif gold < 0:
                lost = ['Lost '+str(gold)+' golds from the casino! Dirty gambling hippies.. '+curTime, 'red']
                session['activities'].append(lost) #+ session['activities']

        return redirect('/')
