from random import randint
for i in range(100):

	grade = randint(60,100)

	if grade >89:
		print("Score: "+ str(grade) + "; Your grade is A")
	elif grade > 79 and grade <90:
		print("Score: "+ str(grade) + "; Your grade is B")
	elif grade > 69 and grade <80:
		print("Score: "+ str(grade) + "; Your grade is C")
	else:
		print("Score: "+ str(grade) + "; Your grade is D")	
