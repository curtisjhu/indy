from ..helper import *
from alpaca.data.live import CryptoDataStream

async def handle_stream_data(data):
	# Handle the incoming data from the stream
	print(data)


if __name__ == "__main__":
	try:
		stream = StockDataStream(api_key, api_secret)
		
		# multiple streams
		stream.subscribe_trades(handle_stream_data, "DOGE/USD")
		stream.run()
	except Exception as e:
		print(f"Error: {e}")
		stream.stop()