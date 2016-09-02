#scores and grades
print "***Scores and Grades***"
print "Please enter your scores"

def letter(grade):
    if (60<=grade<=69):
        return "D"
    elif (70<=grade<=79):
        return "C"
    elif (80<=grade<=89):
        return "B"
    elif (90<=grade<=100):
        return "A"
    elif (grade>100):
        return "fabulous Glen-coco, you go Glen-coco!"
    else:
        return "unacceptable!"


for i in range(1,11):
    grade = input()
    print "Score:" + str(grade) + "; Your grade is " + letter(grade)

print "End of the program. Dueces!"
