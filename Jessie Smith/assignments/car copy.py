class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if price > 10000:
			self.tax=.15
		else: 
			self.tax=.12 
		self.display_all()

	def display_all(self):
		print "Price" + str(self.price)
		print "Speed" + str(self.speed)
		print "Fuel" + str(self.fuel)
		print "Mileage" + str(self.mileage)
		print "Tax" + str(self.tax)

car1 = Car(1000, 70, "empty", 120000)
car2 = Car(2000, 75, "full", 180000)
car3 = Car(4500, 34, "full", 20483)
car4 = Car(9000, 45, "empty", 482028)
car5 = Car(67000, 34, "full", 45000)
car6 = Car(30000, 32, "empty", 2300)
