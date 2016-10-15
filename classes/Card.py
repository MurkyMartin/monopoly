class Card():

	def __init__(self, name, cost):
		#name of card
		#cost of the card
		#mortgage_cost calculates mortgage value
		#owned states if card is owned
		#mortgaged states if card is mortgaged
		self.name = name
		self.cost = cost
		self.mortgage_cost = cost//2
		self.owned = False
		self.mortgaged = False
		pass

	def bought(self, player): #card has been bought, calls Player class to declare ownage and subtractio to money
		self.owned = True
		player.add_card(self, self.cost)

	def sold(self, player): #card has been sold, calls Player class to declare disownage and addition to money
		self.owned = False
		player.remove_card(self, self.cost)

	def mortgage_card(self, player): #mortgages the card and player object gains money
		self.mortgaged = True
		player.mortgage_card(self, self.mortgage_cost)

	def unmortgage_card(self, player): #unmortgages the card and player object loses money
		self.mortgaged = False
		player.unmortgage_card(self, self.mortgage_cost)

	def owned(self): #returns if card is owned
		return self.owned

	def mortgaged(self): #returns if card is mortgaged
		return self.mortgaged
