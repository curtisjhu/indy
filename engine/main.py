from confluent_kafka import Consumer
import json

class Order:
	def __init__(self, order_id, symbol, quantity, price, side):
		self.order_id = order_id
		self.symbol = symbol
		self.quantity = quantity
		self.price = price
		self.side = side  # "buy" or "sell"

class OrderBook:
	def __init__(self):
		self.buy_orders = []
		self.sell_orders = []

	def add_order(self, order):
		if order.side == "buy":
			self.buy_orders.append(order)
			self.buy_orders.sort(key=lambda x: x.price, reverse=True)  # Highest price first
		elif order.side == "sell":
			self.sell_orders.append(order)
			self.sell_orders.sort(key=lambda x: x.price)  # Lowest price first

	def match_orders(self):
		trades = []
		while self.buy_orders and self.sell_orders:
			highest_buy = self.buy_orders[0]
			lowest_sell = self.sell_orders[0]

			if highest_buy.price >= lowest_sell.price:
				trade_quantity = min(highest_buy.quantity, lowest_sell.quantity)
				trade_price = lowest_sell.price

				trades.append({
					"symbol": highest_buy.symbol,
					"quantity": trade_quantity,
					"price": trade_price,
					"buy_order_id": highest_buy.order_id,
					"sell_order_id": lowest_sell.order_id
				})

				highest_buy.quantity -= trade_quantity
				lowest_sell.quantity -= trade_quantity

				if highest_buy.quantity == 0:
					self.buy_orders.pop(0)
				if lowest_sell.quantity == 0:
					self.sell_orders.pop(0)
			else:
				break
		return trades

class TradingEngine:
	def __init__(self):
		self.order_book = OrderBook()

	def place_order(self, order):
		self.order_book.add_order(order)
		trades = self.order_book.match_orders()
		return trades

def consume_orders_from_kafka():
	consumer = Consumer({
		'bootstrap.servers': 'localhost:9092',
		'group.id': 'trading-engine-group',
		'auto.offset.reset': 'earliest'
	})

	consumer.subscribe(['orders'])

	engine = TradingEngine()

	try:
		while True:
			msg = consumer.poll(1.0)  # Poll for messages
			if msg is None:
				continue
			if msg.error():
				print(f"Consumer error: {msg.error()}")
				continue

			order_data = json.loads(msg.value().decode('utf-8'))
			order = Order(
				order_id=order_data['order_id'],
				symbol=order_data['symbol'],
				quantity=order_data['quantity'],
				price=order_data['price'],
				side=order_data['side']
			)

			trades = engine.place_order(order)
			print(f"Processed Order: {order_data}")
			print(f"Trades: {trades}")

	except KeyboardInterrupt:
		print("Shutting down consumer...")
	finally:
		consumer.close()

if __name__ == "__main__":
	consume_orders_from_kafka()