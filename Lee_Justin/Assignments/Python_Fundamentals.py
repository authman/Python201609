for x in range(1, 1000):
    if(x % 2 == 1):
        print x

for x in range(5, 1000001):
    if(x % 5 ==0):
        print x

a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

a = [1,2,5,10,255,3]
sum = 0

avg = sum/len(a)
for num in a:
    sum += num

print avg

for i in range(1,2001):
    if i % 2 == 0:
        print 'Number is ' + str(i) + '. This is an odd number.'
    else:
        print 'Number is ' + str(i) + '. This is an even number.'

a = [2,4,10,16]
def multiply(arr):
    for i in range(len(arr)):
        arr[i] = arr[i] * 5
    return arr

b = multiply(a)
print b


from random import randint

print "Scores and Grades"
for count in range(0, 10):
	score = randint(60, 100)

	if(score <= 70):
		grade = "D"
	elif(score <= 80):
		grade = "C"
	elif(score <= 90):
		grade = "B"
	else:
		grade = "A"

	print "Score: %d; Your grade is %s" %(score, grade)

print "End of program. Bye!"