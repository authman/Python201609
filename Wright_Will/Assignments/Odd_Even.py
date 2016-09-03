
def Odd_Even():
    for n in range(1,2001):
        if n % 2 == 0:
            oddOrEven = "even"
        else:
            oddOrEven = "odd"
        print "Number is " + str(n) + ". This is  an " + oddOrEven + " number."

Odd_Even()
