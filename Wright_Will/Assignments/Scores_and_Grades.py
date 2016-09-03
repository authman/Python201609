print "Scores and Grades"
for n in range(0,10):
    score = int(input("Score:"))
    if score <= 60:
        letter = "F"
    elif score <= 69:
        letter = "D"
    elif score <= 79:
        letter = "C"
    elif score <= 89:
        letter = "B"
    elif score >=90 and score <= 100 :
        letter = "A"
    else:
        letter ="???"
    print " Your grade is " + letter
print "End of the prgram. Bye!"
