class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()
	def display_all(self):
		print "Price: " + str(self.price)
		print "Speed: " + str(self.speed)
		print "Fuel: " + str(self.fuel)
		print "Mileage: " + str(self.mileage)
		if self.price >= 10000:
			print "Tax: 15%"
		elif self.price < 10000:
			print "Tax: 12%"

carOne = Car(1000, '11mph', '1 gallon', 1000)
carTwo = Car(2000, '22mph', '2 gallons', 2000)
carThree = Car(3000, '33mph', '3 gallons', 3000)
carFour = Car(4000, '44mph', '4 gallons', 4000)
carFive = Car(5000, '55mph', '5 gallons', 5000)
carSix = Car(6000, '66mph', '6 gallons', 6000)