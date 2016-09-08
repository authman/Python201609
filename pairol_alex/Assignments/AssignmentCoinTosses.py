import random
import math

print 'Starting the program'

tcount = 0
hcount = 0

for i in range(1,10):
    r = round(random.random())  
    if r == 0:
        side = 'tail'
        tcount +=1
    else:
        side = 'head'
        hcount +=1
    print "Attempt #"+str(i)+": Throwing a coin...It's a "+side+"!...Got "+str(hcount)+" head(s) and "+str(tcount)+" tail(s) so far"

print 'Ending the program, thank you!'

# Assignment: Coin Tosses
# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
# Sample output should be like the following:
#           Starting the program...
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far 

# Ending the program, thank you!
# Here are some hints that might help:
# 1. Use the python random module to generate a random number
# import random
# random_num = random.random()
# # the random function will return a floating point number,
# # that is 0.0 <= random_num < 1.0
# 2. Use the python built-in round function to convert that floating point number into an integer
# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up to 1









