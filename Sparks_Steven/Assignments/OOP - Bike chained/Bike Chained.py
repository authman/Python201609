class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0

	def display(self):
		print 'The price is: $' + str(self.price) +'.'
		print 'The max speed is: '+ str(self.max_speed) +'MPH.'
		print 'The milage is: '+ str(self.miles) +'miles.'
		return self

	def ride(self):
		print 'Riding'
		self.miles+=10
		return self

	def reverse(self):
		print 'Reversing'
		if self.miles>=5:
			self.miles-=5
		return self

	
bike1 = Bike(200, 25)
bike1.ride().ride().ride().reverse().display()

bike2 = Bike(175, 20)
bike2.ride().ride().reverse().reverse().display()

bike3 = Bike(100, 10)
bike3.reverse().reverse().reverse(). display()


		# create three instances of the bike class.
		# use the __init__() function to specify the price and max speed of each instance set miles to 0

		# add functions to class
		# Display info() - display bikes price, max speed,ttl miles
		# ride() - display riding on the screenand incr miles by 10
		# reverse() - display reversing and decr miles by 5

		# have the 1st instance 
		# 	ride x 3
		# 	reve x 1
		# 	display info

		# 	2nd instance
		# 	ride 2 x
		# 	rev 2 x
		# 	display info

		# 	3rd instance
		# 	rev 3x
		# 	display info
