#bike assignment

class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Max speed: " + self.max_speed
        print "Mileage: " + str(self.miles)
        return self
    def ride(self, x=1):
        print "Riding! WHEEEEEEE"
        self.miles += x*10
        return self
    def reverse(self, y=1):
        print "Reversing.."
        self.miles -= y*5
        if self.miles < 0:
            self.miles = 0
        return self

#create the instances of Bike
firstBike = Bike(100,"15mph")

secondBike = Bike(200,"25mph")

thirdBike = Bike(400,"35mph")

#lets go for a ride
print "taking my first bike out for a spin"
firstBike.ride(3).reverse(1).displayInfo()
print " "

print "taking my second bike out for a spin"
secondBike.ride(2).reverse(2).displayInfo()
print " "

print "taking my third bike out for a spin"
thirdBike.reverse(3).displayInfo()
print " "

#end of ride
