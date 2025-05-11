from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from helpers import *
from abc import ABC, abstractmethod

class Engine(ABC):
	def __init__(self):
		self.trading_client = TradingClient(api_key, api_secret, paper=os.getenv("PAPER"))
		self.account = self.trading_client.get_account()
		self.positions = self.trading_client.get_all_positions()
		self.strategies = []
	
	@abstractmethod
	def add_strategy(self, strategy):
		"""
		Add a strategy to the engine.
		"""
		self.strategies.append(strategy)

	@abstractmethod
	def forward(self, data):
		for stragegy in self.strategies:
			strategy.execute(data)