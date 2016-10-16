from Card import Card

class Transport(Card):

	def __init__(self, name, cost=200, transports):
		Card.__init__(name,cost)
		#perhaps the the next assignment could declare the ownage of the transport cards and which ones???
		#initialise a new attribute called transports which holds a dictionary
		#maybe have a dictionary which contain transport names and value defaults to False so
		#more transports can be added and is more maintainable ??? 
		# transports = {'Bus':False, 'Airport':False ...}
		#***self.other_trans_owned = transports***
		
		#***self.other_trans_owned = [False]*4***
		#this is a second alternative
		#False in position 0 corresponds to first transport son the board and so on
		#True if transport owned
		
		##
		#Could do the checking in the board
		#If the board is a DDL, maintain a list of indexes of where the transports are
		#then check those indexes
		#could make this easier by having a 'owned_by' instance vairable that is a player object and check if a given
		#player owns tranport(s)
	
	"""def other_trans_bought(self):
		#if we are using a dictionary
		self.transports[self.name] = True
		return self.transports"""
		
