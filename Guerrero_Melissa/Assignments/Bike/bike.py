class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price is: $', str(self.price)
        print 'Max speed: ', str(self.max_speed)
        print 'Total miles: ', str(self.miles)
	def ride(self):
		print "Riding!"
		self.miles += 10
	def reverse(self):
		print "Reversing!"
		self.miles -= 5
		if (self.miles == 0):
			print "You may not reverse into negative mileage!"
			
bikeone = Bike(1, "11mph")
bikeone.ride()
bikeone.ride()
bikeone.ride()
bikeone.reverse()
bikeone.displayinfo()

biketwo = Bike(2, "22mph")
biketwo.ride()
biketwo.ride()
biketwo.reverse()
biketwo.reverse()
biketwo.displayinfo()

bikethree = Bike(3, "33mph")
bikethree.reverse()
bikethree.reverse()
bikethree.reverse()
bikethree.displayinfo()