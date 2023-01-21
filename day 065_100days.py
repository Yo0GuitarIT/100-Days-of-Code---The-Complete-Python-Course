class character():
	name = None
	health = None
	magicPoint = None
	
	def __init__(self,name,health,magicPoint):
		self.name = name
		self.health = health
		self.magicPoint = magicPoint

	def print(self):
		print(f"Name: {self.name}")
		print(f"Health: {self.health}")
		print(f"Magic: {self.magicPoint}")

class david(character):
	lives = None
	alive = None

	def __init__(self,name,health,magicPoint,lives,alive):
		self.name = name
		self.health = health
		self.magicPoint = magicPoint
		self.lives = lives
		self.alive = alive

	def print(self):
		print(f"Name: {self.name}")
		print(f"Health: {self.health}")
		print(f"Magic: {self.magicPoint}")
		print(f"Lives: {self.lives}")
		print(f"Alive: {self.alive}")
		

david = david("David",100,50,3,"Yes")
david.print()
