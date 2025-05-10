import os
from dotenv import load_dotenv
load_dotenv()

from alpaca.data.live import CryptoDataStream

async def handle_stream_data(data):
	# Handle the incoming data from the stream
	print(data)


if __name__ == "__main__":
	# Initialize the Alpaca trading client
	api_key = os.getenv("ALPACA_API_KEY")
	api_secret = os.getenv("ALPACA_SECRET_KEY")

	try:
		stream = CryptoDataStream(api_key, api_secret)

		stream.subscribe_trades(handle_stream_data, "DOGE/USD")
		stream.run()
	except Exception as e:
		print(f"Error: {e}")
		stream.stop()