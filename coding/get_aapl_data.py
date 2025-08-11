# filename: get_aapl_data.py
import yfinance as yf

# Set the ticker symbol for Apple
ticker_symbol = 'AAPL'

# Download the data for the past 1 month
data = yf.download(ticker_symbol, period='1mo', interval='1d')

# Print the retrieved data
print(data[['Close']])