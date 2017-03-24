
class Fighter(object):
	"""docstring for Fighter"""
	def __init__(self, name):
		self.name = name
		self.health = 100
		self.damage = 10


	def attack(self,other_guy):
		other_guy.health -= self.damage
		print("{} attacks {}".format(self.name,other_guy.name))
		print("{} losses {} points ".format(other_guy.name,self.damage))

	def __str__(self):
		return "{} : {}".format(self.name,self.health)



pritpal = Fighter("Preet")

qazi = Fighter("Qazi")

pritpal.attack(qazi)
print(pritpal.name)
print(qazi.name)

print(pritpal)
print(qazi)