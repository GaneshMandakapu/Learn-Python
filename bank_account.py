class Bank_Account:

	def __init__(self,name,type,balance):
		self.name = name
		self.type = type
		self.balance = balance

	def deposit(self,Amount):
		self.balance +=Amount

	def withdraw(self,Amount):
		self.balance -= Amount


	def __str__(self):
		return "{} {} accounts has balance {} ".format(self.name,self.type,self.balance)



preet = Bank_Account("Pritpal","Savings",1000)

print(preet)

preet.deposit(1000)
print(preet)

preet.withdraw(500)

print(preet)
