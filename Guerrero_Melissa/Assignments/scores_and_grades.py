for count in range (0, 10):
	score = input('Enter your score: ')

	if(60 <= score <= 69):
		print "Score: ", score, "Your grade is D"
	elif(70 <= score <= 79):
		print "Score: ", score, "Your grade is C"
	elif(80 <= score <= 89):
		print "Score: ", score, "Your grade is B"
	elif(90 <= score <= 100):
		print "Score: ", score, "Your grade is A"

print "End of program. Bye!"
