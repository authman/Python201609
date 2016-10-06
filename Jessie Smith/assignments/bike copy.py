class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	

	def displayInfo(self):
		print "Price: " + str(self.price)
		print "Max Speed: " + self.max_speed
		print "Miles" + str(self.miles)

	def drive(self):
		print "Driving"
		self.miles += 10

	def reverse(self):
		print "Reversing"
		if self.miles >= 5:
			self.miles -= 5

		
bike1 = Bike(200, "25 mph")
bike1.displayInfo()
bike1.drive()
bike1.drive()
bike1.drive()
bike1.reverse()

bike2=Bike(150, "30 mph")
bike2.displayInfo()
bike2.drive()
bike2.drive()
bike2.drive()
bike2.reverse()

bike3=Bike(300, "15 mph")
bike3.displayInfo()
bike3.drive()
bike3.drive()
bike3.drive()
bike3.reverse()




