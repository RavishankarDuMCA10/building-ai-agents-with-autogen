# filename: fetch_aapl_data.py

import yfinance as yf
import pandas as pd

# Define the stock symbol and the period
stock_symbol = 'AAPL'
period = '1mo'

# Download the stock data
data = yf.download(stock_symbol, period=period)

# Show the retrieved data
print(data)