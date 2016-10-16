from Card import Card

class Transport(Card):

	def __init__(self, name, cost=200):
		Card.__init__(name,cost)
		#perhaps this could declare the ownage of the transport cards and which ones???
		#maybe have a dictionary which contain transport names and value defaults to False so
		#more transports can be added and is more maintainable ??? {'Bus':False, 'Airport':False ...}
		self.other_trans_owned = [False]*4 
		#False in position 0 corresponds to first transport son the board and so on
		#True if transport owned
