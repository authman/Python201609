import random

def coinFlip(flipTimes):
    heads=0;## heads rep by 0 flip
    tails=0;## heads repby 1 flip
    for i in range(0,flipTimes):
        randNum=round(random.random())
        if randNum==0:
            heads+=1
            print"Attempt #"+str(i+1)+" Throwing coin...It's a head!..Got "+str(heads)+" head(s) so far and "+ str(tails)+" tail(s) so far"
        elif randNum==1:
            tails+=1
            print"Attempt #"+str(i+1)+" Throwing coin...It's a tail!..Got "+str(tails)+" tail(s) so far and "+ str(heads)+" head(s) so far"
        else:
            print" OMG it landed on its side!"
    print "Ending the program, Thank you!"
coinFlip(5000)
