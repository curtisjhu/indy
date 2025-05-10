import os
from dotenv import load_dotenv

load_dotenv()

from alpaca.trading.stream import TradingStream
from alpaca.trading.client import TradingClient

def handle_stream_data(data):
	# Handle the incoming data from the stream
	print(data)


if __name__ == "__main__":
	# Initialize the Alpaca trading client
	api_key = os.getenv("ALPACA_API_KEY")
	api_secret = os.getenv("ALPACA_SECRET_KEY")
	base_url = os.getenv("APCA_API_BASE_URL")

	stream = TradingStream(api_key, api_secret)

	# Subscribe to a specific symbol (e.g., AAPL)
	symbol = "AAPL"
	stream.subscribe_trades(handle_stream_data, symbol)

	# Start the stream
	stream.run()