class Animal(object):
    
    def __init__(self, name,health=100):
        self.name = name
        self.health=health

    def walk(self):
        self.health-=1
        return self

    def run(self):
        self.health-=5
        return self

    def displayHealth(self):
        print "Hey my name is "+ self.name +" and my health is " + str(self.health)



class Dog(Animal):
    
    def __init__(self, name,health=150):
        super(Dog,self).__init__(name, health)
        
        
    def pet(self):
        self.health+=5
        return self


class Dragon(Animal):

    def __init__(self, name,health=170):
        super(Dragon,self).__init__(name, health)

    def fly(self):
        self.health-=10
        return self

    def displayHealth(self):
        print "Its a Dragon!"
        super(Dragon,self).displayHealth()
        return self



A=Animal("Jim")
B=Dog("Tim")
C=Dragon("Ed")

A.walk().walk().walk().run().run().displayHealth()
B.walk().walk().walk().run().run().pet().displayHealth()    
C.walk().walk().walk().run().run().fly().fly().displayHealth()



    
        
