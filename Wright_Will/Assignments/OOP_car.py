
class Car(object):
    def __init__(self,price,speed,fuel_mileage):
        self.price = price
        self.speed = speed
        self.fuel_mileage = fuel_mileage
        self.fuel = "full"
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
    def display_all(self):
        print "\n"
        print "price: " + str(self.price)
        print "speed: " + str(self.speed) +" mph"
        print "fuel: " + str(self.fuel)
        print "fuel_mileage: " + str(self.fuel_mileage) +" mpg"
        print "tax: " + str(self.tax)
    def drive(self):
        if self.fuel == "full":
            self.fuel = "kind of full"
        elif self.fuel == "kind of full":
            self.fuel = "Almost Empty"
        elif self.fuel == "Almost Empty":
            self.fuel = "Empty"
            print "UH OH.. You ran out of gass"
        elif self.fuel == "Empty":
            print "You car needs gas to run... genius."
car1 = Car(1000,50,30)
car2 = Car(2000,60,30)
car3 = Car(3000,70,25)
car4 = Car(4000,80,45)
car5 = Car(5000,90,12)
car6 = Car(6000,1000,9)

car1.display_all()
car2.display_all()
car3.display_all()
car4.display_all()
car5.display_all()
car6.display_all()
