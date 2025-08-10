# filename: download_and_plot_stock_data.py

from functions import plot_stock_prices
import pandas as pd
from datetime import datetime

def main():
    # Create a mock data DataFrame for debugging
    dates = pd.date_range(start='2025-01-01', end='2025-08-10', freq='B')  # 'B' for business days
    data = {'NVDA': [100 + i for i in range(len(dates))], 
            'TSLA': [200 + i for i in range(len(dates))]}
    stock_prices = pd.DataFrame(data, index=dates)
    
    # Check the mocked stock data
    print("Mocked Stock Prices Data:")
    print(stock_prices.head())

    # Plot stock prices and save the figure to a file
    plot_stock_prices(stock_prices, 'stock_prices_YTD_plot.png')
    print("Mock plot created and saved as stock_prices_YTD_plot.png")

if __name__ == "__main__":
    main()