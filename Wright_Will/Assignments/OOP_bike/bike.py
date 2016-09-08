#bike

class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "price: " + str(self.price)
        print "max_speed: " + str(self.max_speed)
        print "miles: " + str(self.miles)
    def ride(self):
        print 'riding'
        self.miles += 10
    def reverse(self):
        print 'reversing'
        if self.miles < 5:
            self.miles = 0
        else:
            self.miles -= 5


a = Bike(100,10)
b = Bike(10,1)
c = Bike(50,5)

print "bike a:"
a.ride()
a.ride()
a.ride()
a.reverse()
a.displayInfo()
print "bike b:"
b.ride()
b.ride()
b.reverse()
b.reverse()
b.displayInfo()
print "bike c:"
c.reverse()
c.reverse()
c.displayInfo()
