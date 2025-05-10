from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from helpers import *

class Engine:
	def __init__(self):
		self.trading_client = TradingClient(api_key, api_secret, paper=True)
		self.account = self.trading_client.get_account()
		self.positions = self.trading_client.get_all_positions()

		self.strategies = []
	
	def forward(self, data):
		for stragegy in self.strategies:
			strategy.execute(data)