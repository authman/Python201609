import random
random_num = random.random()

for count in range(5000):
	coin = round(random_num)
	head_count=1
	tail_count=0
	if coin == 1:
		head_count +=1
		print "Throwing a coin...It's a head! Got " + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
	elif coin == 0:
		tail_count +=1
		print "Throwing a coin...It's a tail! Got " + str(tail_count) + " tail(s) so far and " + str(head_count) + " head(s) so far"
