# filename: plot_ytd_stock_gains.py

import matplotlib.pyplot as plt
import yfinance as yf

# Define the stock symbols and the time frame
stocks = ['NVDA', 'TSLA']
start_date = '2025-01-01'
end_date = '2025-08-09'

# Download the stock data with auto_adjust=True
data = yf.download(stocks, start=start_date, end=end_date, auto_adjust=True)['Close']

# Calculate YTD performance
ytd_performance = (data / data.iloc[0] - 1) * 100

# Plot the YTD performance
plt.figure(figsize=(10, 6))
for stock in stocks:
    plt.plot(ytd_performance.index, ytd_performance[stock], label=stock)

# Add titles and labels
plt.title('YTD Stock Performance (2025)')
plt.xlabel('Date')
plt.ylabel('Percentage Gain (%)')
plt.legend()

# Save the graph as an image file
plt.savefig('ytd_stock_gains.png')

# Display the plot
plt.show()