#car assignment

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        self.display_all()
    def display_all(self):
        print "\n" + "Price: " + str(self.price) + "\n" + "Speed: " + self.speed + "\n" + "Fuel: " + self.fuel + "\n" + "Mileage: " + self.mileage + "\n" + "Tax: " + str(self.tax) + "\n"


#making the cars
firstCar = Car(4000,"50mph","Half","20mpg")
secondCar = Car(30000,"80mph","Full","12mpg")
thirdCar = Car(90000,"120mph","Electric","200mpc")
fourthCar = Car(300000,"205mph","Full","14mpg")
fifthCar = Car(2000,"40mph","Quarter Full","19mpg")
sixthCar = Car(111585,"191mph","Half","16mpg")
