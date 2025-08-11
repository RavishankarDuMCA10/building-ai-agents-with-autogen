# filename: analyze_aapl_data.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download the data for the past 1 month
ticker_symbol = 'AAPL'
data = yf.download(ticker_symbol, period='1mo', interval='1d')

# Descriptive Statistics
closing_prices = data['Close']
mean_price = closing_prices.mean()
median_price = closing_prices.median()
std_dev_price = closing_prices.std()
highest_price = closing_prices.max()
lowest_price = closing_prices.min()

print(f"Mean Price: {mean_price}")
print(f"Median Price: {median_price}")
print(f"Standard Deviation: {std_dev_price}")
print(f"Highest Price: {highest_price}")
print(f"Lowest Price: {lowest_price}")

# Visualization
plt.figure(figsize=(10, 5))
plt.plot(closing_prices.index, closing_prices, label='Closing Prices', color='blue')
plt.plot(closing_prices.index, closing_prices.rolling(window=5).mean(), label='5-Day Moving Average', color='orange')
plt.title('AAPL Closing Prices - Last 1 Month')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()