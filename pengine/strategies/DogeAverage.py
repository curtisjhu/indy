

class DogeAverage(AbstractStrategy):
	"""
	DogeAverage strategy for trading.
	"""

	def __init__(self, symbol, exchange):
		self.symbol = symbol
		self.exchange = exchange
	
	def get_symbol(self):
		return self.symbol

	def execute(self, data):
		if stream_data < 0.5:
			