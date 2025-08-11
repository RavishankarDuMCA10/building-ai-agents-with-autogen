# filename: refine_analysis.py

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Download the stock data
stock_symbol = 'AAPL'
period = '1mo'
data = yf.download(stock_symbol, period=period)

# Calculate the 20-day Moving Average and Bollinger Bands
data['20 Day MA'] = data['Close'].rolling(window=20).mean()
data['Upper Band'] = data['20 Day MA'] + 2 * data['Close'].rolling(window=20).std()
data['Lower Band'] = data['20 Day MA'] - 2 * data['Close'].rolling(window=20).std()

# Plot the closing price, moving averages, and Bollinger Bands
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['20 Day MA'], label='20 Day MA', linestyle='--')
plt.plot(data['Upper Band'], label='Upper Bollinger Band', linestyle='--')
plt.plot(data['Lower Band'], label='Lower Bollinger Band', linestyle='--')
plt.fill_between(data.index, data['Upper Band'], data['Lower Band'], color='grey', alpha=0.1)
plt.title('Apple (AAPL) Stock Price with Moving Averages and Bollinger Bands')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend(loc='best')
plt.show()