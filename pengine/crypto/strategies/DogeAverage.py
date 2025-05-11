from .AbstractStrategy import AbstractStrategy

class DogeAverage(AbstractStrategy):
	"""
	DogeAverage strategy for trading DOGE.
	This strategy calculates the average price of DOGE over a given period and makes buy/sell decisions based on the current price relative to the average.
	"""

	def __init__(self, symbol, exchange, period=10):
		super().__init__(symbol)
		self.exchange = exchange
		self.period = period
		self.prices = []

	def execute(self, data):
		"""
		Executes the strategy based on incoming data.
		:param data: A dictionary containing the latest price data for DOGE.
		"""
		current_price = data.get('price')
		if current_price is None:
			
			raise ValueError("Data must contain 'price' key")

		# Update the price history
		self.prices.append(current_price)
		if len(self.prices) > self.period:
			self.prices.pop(0)

		# Calculate the average price
		average_price = sum(self.prices) / len(self.prices)

		# Decision logic
		if current_price < 0.95 * average_price:

		elif current_price > 1.05 * average_price:
			print(f"Selling DOGE at {current_price}, above average price {average_price}")
		else:
			print(f"Holding DOGE at {current_price}, near average price {average_price}")
