#coin toss
import random

print "~~~Welcome to Coin Toss~~~"
print "Heads it lives, tails it puts the lotion on its skin"


def coinFlip():
    headCount = 0
    tailCount = 0

    for i in range(1,5001):
        random_num = random.random()
        coin = round(random_num)
        if (coin==0):
            headCount = headCount + 1
            print "Attempt #" +str(i)+ ": Throwing it's fate(I mean coin)... It's a head! .. darn.. "
            print "Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " tail(s) so far.."
        elif (coin==1):
            tailCount += 1
            print "Attempt #" +str(i)+ ": Throwing it's fate(I mean coin)... It's a tail! .. it puts the lotion on it's skin! "
            print "Got " + str(headCount) + " head(s) so far and " + str(tailCount) + " tail(s) so far.. yay"

coinFlip()

print "End of program, it goes to sleep!!!"
