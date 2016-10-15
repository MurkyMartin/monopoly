from Card import Card

class Property(Card):

	def __init__(self, name, cost, colour, house_cost, rent):
		Card.__init__(name, cost)
		self.colour = colour
		self.house_cost = house_cost
		self.house_num = 0
		self.rent = rent

	def __str__(self):
		pass

	def cal_rent(self):
		pass

	def new_house(self):
		if self.house_num < 5:
			self.house_num += 1
			self.cal_rent()
		return

	def sell_house(self):
		if self.house_num > 0:
			self.house_num -= 1
			self.cal_rent()
		return

	"""We need to figure out how to tell peeps
	when they have a full set so they can start building
	and selling houses"""