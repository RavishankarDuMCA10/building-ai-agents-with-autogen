

def get_stock_prices(
    stock_symbols,
    start_data,
    end_data
):
    """
    Fetch stock closing prices for given stock symbols between start and end dates.
    
    Args:
        stock_symbols: Stock symbol(s) to fetch prices for. Can be a string or a list of strings.
        start_date: The start date in 'YYYY-MM-DD' format.
        end_date: The end date in 'YYYY-MM-DD' format.
        
    Returns:
        DateFrame: Stock closing prices indexed by date, with one column per stock symbol.
    """
    import yfinance
    from pandas import DataFrame
    
    try:
        stock_data = yfinance.download(stock_symbols, start=start_date, end=end_date)
        return stock_date["Close"]
    except Exception as e:
        print(f"Error fetching stock data: {str(e)}")
        return DataFrame()


def plot_stock_prices(stock_prices, filename):
    """
    Plot stock prices and save the figure to a file.
    
    Args:
        stock_prices (DataFrame): Stock prices indexed by date, with columns for each stock.
        filename (str): Name of the file to save the plot.
    """
    import matplotlib.pyplot as plt
    from pandas import DataFrame
    plt.figure(figsize=(10, 5))
    stock_prices.plot(ax=plt.gca(), grid=True)
    plt.title("Stock Prices")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend(loc='best')
    plt.savefig(filename)
    plt.close()


