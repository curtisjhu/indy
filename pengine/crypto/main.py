from ..helper import *
from alpaca.data.live import CryptoDataStream

# Initialize the CryptoDataStream
crypto_stream = CryptoDataStream(api_key, api_secret)

async def handle_stream_data(data):
    """Handle the incoming data from the crypto stream."""
    print("Received crypto stream data:", data)

if __name__ == "__main__":
    try:
        # Subscribe to a crypto stream (e.g., BTC/USD)
        crypto_stream.subscribe_trades(handle_stream_data, "BTC/USD")
        print("Subscribed to BTC/USD trades stream.")

        # Run the crypto stream
        crypto_stream.run()
    except Exception as e:
        print(f"Error: {e}")
        crypto_stream.stop()