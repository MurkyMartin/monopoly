class Property():

	#ORANGE_COST = 12
	#RED_COST = 10

	def __init__(self, name, cost, colour=None, house_cost=0 ,house_num=0, transport=False, utility=False):
		#name is name of property
		#colour of card
		#cost of property
		#house_cost duh
		#house_num duh
		
		
		#attributes of object
		self.name = name
		self.cost = cost
		self.colour = colour
		self.house_num = house_num
		self.house_cost = house_cost
		self.transport = transport #inherite
		self.utility = utility #inherite

		#values based on cost
		self.mortgage_cost = cost//2
		self.rent = None #dispute!

		#state variables
		self.owned = False
		self.mortgaged = False
		pass

	def __str__(self):
		pass

	def cal_rent(self):
		#checks self.house_num
		#updates self.rent value as a new house is added or sold

	def new_house(self):
		if self.house_num < 5:
			self.house_num += 1
			self.cal_rent()
		return

	def sold_house(self):
		if self.house_num > 0:
			self.house_num -= 1
			self.cal_rent()
		return

	def bought(self, player):
		self.owned = True
		player.add_property(self) #adds the property to a list of objects in the player object
		return

	def sold(self, player):
		self.owned = False
		player.remove_property(self)
		self.reset()

	def reset(self):
		self.mortgaged = False
		self.house_num = 0
		self.rent = None #dispute!

	def change_mortgage(self, player):
		if self.is_mortgaged():
			player.take(self.mortgage_cost) #take(amount) removes amount from player fund
		else:
			player.add(self.mortgage_cost) #add(amount) adds amount to player fund
		self.mortgaged = not(self.mortgaged)

	def is_owned(self):
		return self.owned

	def is_mortgaged(self):
		return self.mortgaged



class Player():

	def __init__(self, name, funds=1500, location=None):
		self.cards = []
		pass

	def __str__(self):
		pass

	def add_property(self, prop):
		self.cards.append(prop)

	def take(self, amount):
		self.funds -= amount

	def add(self, amount):
		self.funds += amount


class MakeBoard():

	def __init__(self, players, starting_point):
		for player in players:
			player.location = self.starting_point

	def __str__(self):
		pass