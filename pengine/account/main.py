import os
from alpaca.trading.client import TradingClient
from alpaca.trading.stream import TradingStream
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

# Alpaca API credentials
api_key = os.getenv("ALPACA_API_KEY")
api_secret = os.getenv("ALPACA_SECRET_KEY")
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

# Initialize Alpaca Trading Client and Stream
trading_client = TradingClient(api_key, api_secret, paper=True)
trading_stream = TradingStream(api_key, api_secret, paper=True)

def send_email(subject, body):
    """Send an email with the given subject and body."""
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)
            server.sendmail(email_user, recipient_email, msg.as_string())
            print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

def handle_account_update(data):
    """Handle account updates and send an email notification."""
    subject = "Account Update Notification"
    body = f"Account Update:\n{data}"
    send_email(subject, body)

def handle_portfolio_update(data):
    """Handle portfolio updates and send an email notification."""
    subject = "Portfolio Update Notification"
    body = f"Portfolio Update:\n{data}"
    send_email(subject, body)

# Subscribe to account and portfolio updates
trading_stream.subscribe_account_updates(handle_account_update)
trading_stream.subscribe_portfolio_updates(handle_portfolio_update)

if __name__ == "__main__":
    try:
        print("Starting trading stream...")
        trading_stream.run()
    except KeyboardInterrupt:
        print("Stopping trading stream...")
        trading_stream.stop()