class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
		return self

	def displayInfo(self):
		print 'Price is: ' + str(self.price)
        print 'Max speed: ' + str(self.max_speed)
        print 'Total miles: ' + str(self.miles)
        return self
    	
	def ride(self):
		print "Riding!"
		self.miles += 10
		return self
		
	def reverse(self):
		print "Reversing!"
		self.miles -= 5
		if (self.miles == 0):
			print "You may not reverse into negative mileage!"
		return self
		

bikeone = Bike(1, "11mph")
bikeone.ride().ride().ride().reverse().displayinfo();

biketwo = Bike(2, "22mph")
biketwo.ride().ride().reverse().reverse().displayinfo();

bikethree = Bike(3, "33mph")
bikethree.reverse().reverse().reverse().displayinfo();

