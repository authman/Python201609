from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'secretsquirrel'

@app.route('/')
def index():
    #initialize gold count
    if not 'goldCount' in session:
        session['goldCount'] = 0
        session['activities'] = []

    
    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def money():

    
    
    formAction = request.form['action']
    
    if formAction == 'farm':
        farmGold = random.randrange(10,21)
        session['goldCount'] += int(farmGold)

        session['activities'].append('<p style="color: green">You earned '+str(farmGold)+ ' gold from the farm!</p>')
        
        print 'farm'
        print session['activities']
        
    elif formAction == 'cave':
        caveGold = random.randrange(5,11)
        session['goldCount'] += int(caveGold)

        session['activities'].append('<p style="color: green">You earned '+str(caveGold)+ ' gold from the cave!</p>')
        
        print 'cave'
        print session['activities']
        
    elif formAction == 'house':
        houseGold = random.randrange(2,6)
        session['goldCount'] += int(houseGold)

        session['activities'].append('<p style="color: green">You earned '+str(houseGold)+ ' gold from the house! Silly thieves</p>')
        
        print 'house'
        print session['activities']
        
    elif formAction == 'casino':
        casinoGold = random.randrange(-50,51)
        session['goldCount'] += int(casinoGold)

        if casinoGold >= 0:
            session['activities'].append('<p style="color: green">You earned '+str(casinoGold)+ ' gold from the casino!</p>')
        else:
            session['activities'].append('<p style="color: red">You lost '+str(casinoGold)+ ' gold from the casino! ha -- loser </p>')
        
        
        print 'casino'
        print session['activities']


    


    

    return redirect('/')

app.run(debug=True)
