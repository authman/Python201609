#animal OOP assignment

### animal parent class
class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self, x=1):
        self.health -= 1*x
        return self
    def run(self, y=1):
        self.health -= 5*y
        return self
    def displayHealth(self):
        print self.name
        print self.health
        return self

animal = Animal('Thunder')

print animal.walk(3).run(2).displayHealth()


### dog child class
class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self, x=1):
        self.health += 5*x
        return self

fido = Dog('Fido')

print fido.walk(3).run(2).pet(1).displayHealth()


### dragon child class
class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self, x=1):
        self.health -= 10*x
        return self
    def displayHealth(self):
        print 'This is a dragon!'
        super(Dragon, self).displayHealth()

drazo = Dragon('Drazo')

print drazo.walk(3).run(2).fly(2).displayHealth()
