from random import randint

headct = 0
tailct = 0

for i in range(5000):

	coin = randint(1,2)

	if coin == 1:
		headct += 1
		attempt = headct + tailct
		print("Attempt # "+ str(attempt) +" : Throwing a coin...It's a head!...Got " + str(headct) +" head(s) so far and "+str(tailct) + " tail(s) so far")
		
	elif coin  != 1:
		tailct += 1
		attempt = headct + tailct
		print("Attempt # "+ str(attempt) +" : Throwing a coin...It's a tail!...Got " + str(headct) +" head(s) so far and "+str(tailct) + " tail(s) so far")
		

#coin toss
#simulate tossing a coin 5000 times
#display result of current toss and display running tally of heads and tails	
#Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far 
#Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far 
#Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far 
#Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far