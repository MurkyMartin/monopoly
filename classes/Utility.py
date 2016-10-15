from Card import Card

class Utility(Card):

	def __init__(self, name, cost):
		Card.__init__(name, cost)

		self.other_util_owned = False
		self.multiplier = 4 #change multiplier by checking if other util is owned
		pass

	def __str__(self):
		pass

	def change_multiplier(self):
		if self.other_util_owned:
			self.multiplier = 10
		else:
			self.multiplier = 4

	def other_util_bought(self):
		self.other_util_owned = True