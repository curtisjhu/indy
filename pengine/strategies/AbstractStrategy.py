from abc import ABC, abstractmethod

class AbstractStrategy(ABC):
	"""
	Abstract class for all strategies.
	"""

	def __init__(self, name: str):
		self.symbol = symbol
		
	def get_symbol(self):
		return self.symbol

	@abstractmethod
	def execute(self, data):
		raise NotImplementedError("Subclasses must implement this method")