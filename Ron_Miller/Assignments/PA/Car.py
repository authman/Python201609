class Car(object):
    def __init__(self, price, speed, fuel, mileage):

        self.price=price
        self.speed=speed
        self.fuel =fuel
        self.mileage=mileage

        if price>10000:
            self.tax=0.15
        elif price<10000 and price>0:
            self.tax=0.12

    def display_all(self):
        print "Car info:\nPrice: "+str(self.price)+"\nSpeed: "+ \
              str(self.speed)+"mph\nFuel: "+ self.fuel + \
              "\nMileage: "+ str(self.mileage)+"mpg\n" \
              "Tax: "+ str(self.tax)+"\n"

        
A=Car(2000,35,"Full",15)
B=Car(2000,5,"Not Full",105)
C=Car(2000,5,"Not Full",105)
D=Car(2000,15,"Kind of Full",95)
E=Car(2000,25,"Full",25)
F=Car(2000,45,"Empty",25)
G=Car(2000000,35,"Empty",15)

aList =[A,B,C,D,E,F,G]
for i in range(len(aList)):
    aList[i].display_all()
    

