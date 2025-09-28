import yfinance as yf
import pandas as pd
from datetime import date, timedelta

def get_stock_data(ticker, start_date, end_date):
    """
    downloads historical stock data for a given ticker from Yahoo Finance.

    args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL').
        start_date (str): The start date for the data in 'YYYY-MM-DD' format.
        end_date (str): The end date for the data in 'YYYY-MM-DD' format.

    returns:
        pd.DataFrame: A DataFrame containing the stock data, or None if the
                      ticker is invalid or data cannot be retrieved.
    """
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        if data.empty:
            print(f"No data found for {ticker} in the specified date range.")
            return None
        return data
    except Exception as e:
        print(f"Error downloading data for {ticker}: {e}")
        return None

def get_stock_data_by_years(ticker, years):
    """
    downloads historical stock data for a given ticker for the last N years.

    args:
        ticker (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL').
        years (int): The number of years of data to retrieve.

    returns:
        pd.DataFrame: A DataFrame containing the stock data, or None if the
                      ticker is invalid or data cannot be retrieved.
    """
    end_date = date.today()
    start_date = end_date - timedelta(days=years * 365)
    
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')
    
    print(f"Fetching data for {ticker} from {start_date_str} to {end_date_str}")
    
    return get_stock_data(ticker, start_date_str, end_date_str)

def get_multiple_stock_data(tickers, years):
    """
    downloads historical stock data for a list of tickers for the last N years.
    returns a single DataFrame with a MultiIndex.

    args:
        tickers (list): A list of stock ticker symbols.
        years (int): The number of years of data to retrieve.

    returns:
        pd.DataFrame: A single DataFrame with a MultiIndex (ticker, Date),
                      or None if no data could be downloaded.
    """
    stock_data_dict = {}
    for ticker in tickers:
        data = get_stock_data_by_years(ticker, years)
        if data is not None:
            data['Ticker'] = ticker
            stock_data_dict[ticker] = data
            
    if not stock_data_dict:
        print("No stock data could be downloaded.")
        return None

    # concatenate all DataFrames into a single DataFrame
    all_data = pd.concat(list(stock_data_dict.values()))
    
    # set the MultiIndex
    all_data.set_index(['Ticker', all_data.index], inplace=True)
    
    # rename the date index to 'Date'
    all_data.index.set_names(['Ticker', 'Date'], inplace=True)

    return all_data

# test code
if __name__ == "__main__":
    print("--- Testing data_acquisition.py ---")
    
    # test 1: Get data for a list of major US and EU stocks
    tickers = [
        'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', # US Stocks
        'MC.PA', 'AZN.L', 'SIE.DE', 'SHEL.L', 'SAP.DE', # EU Stocks
        'ASML', 'NESN.SW' # Additional stocks to reach 10-15
    ]
    years_to_fetch = 3
    
    print(f"\nAttempting to download {years_to_fetch} years of data for {len(tickers)} tickers.")
    all_stocks_data = get_multiple_stock_data(tickers, years_to_fetch)

    if all_stocks_data is not None:
        print("\nSuccessfully downloaded and combined data into a single DataFrame.")
        print("Here are the first 10 rows:")
        print(all_stocks_data.head(10))
        print("\nDataFrame information:")
        all_stocks_data.info()
    else:
        print("\nFailed to download any stock data.")
        
    # test 2: Test with a ticker that should fail (remains for robustness)
    print("\nAttempting to download data for a non-existent ticker ('INVALID_TICKER')...")
    invalid_data = get_stock_data_by_years('INVALID_TICKER', 1)
    if invalid_data is None:
        print("Test passed: No data was returned as expected.")
