heads_count = 0
tails_count = 0
for count in range (0, 5001):
	import random
	random_num = random.random()
	x = random_num
	x_rounded = round(x)
	

	if (0 <= x_rounded <= 0.49):
		heads_count += 1
		print "Attempt #", count, "Tossing a coin...It's heads!", heads_count, "heads total"

	else:
		tails_count += 1
		print "Attempt #", count, "Tossing a coin...It's tails!", tails_count, "tails total"

	random.random()
print "End of program. Bye!"


