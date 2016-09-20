class Animal(object):
	def __init__(self, name):
		self.health=100
		self.name=name

	def walk(self):
		self.health-=1
		return self

	def run(self):
		self.health-=5
		return self

	def display(self):
		print 'Name:'+str(self.name)
		print 'Health:'+str(self.health)

animal=Animal('besse')
animal.walk().walk().walk().run().run().diplay()

class Dog(animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)
		self.health = 150
	
	def pet(self):
		self.health+=5
		return self

dog=Dog('snoopy')
dog.walk().walk().walk().run().run().pet().display()

class Dragon(animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name)
		self.health = 170
	
	def fly(self)
		self.health-=10

	def display(self):
		print 'This is a Dragon'
		super(Dragon, self).diplay()

dragon=Dragon('Puff')
dragon.fly().display()
