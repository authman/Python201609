import random


heads = 0
tails = 0
for n in range( 1, 5001 ):
    rand = round(random.random())
    if rand == 1:
        flip = "head"
        heads += 1
    elif rand == 0:
        flip = "tail"
        tails += 1
    else:
        flip = "neither"
    print("Attempt#"+str(n)+": Throwing a coin... It's a "+ flip +"!... Got " + str(heads) +"head(s) so far and " + str(tails) +" tail(s) so far")
