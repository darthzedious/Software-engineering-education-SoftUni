import os
import requests
import numpy as np

def fetch_stock_price(symbol):

    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json() # => If the API response is valid, data will be a dictionary that can be further processed.

        # Check if the data has the required keys
        # Global Quote is a key with value dict what holds key:value pares such as "05. price": "227.70"
        if "Global Quote" in data and "05. price" in data["Global Quote"]:
            return float(data["Global Quote"]["05. price"])
        else:
            return None
    except requests.RequestException:
        return None


def fetch_historical_data(symbol, function='TIME_SERIES_MONTHLY_ADJUSTED', market_index='^GSPC'):
    """
    Fetch historical price data for a given stock and the market index.

    Args:
        symbol (str): The stock symbol.
        function (str): The Alpha Vantage function to call.
        market_index (str): The market index symbol (default is S&P 500).

    Returns:
        dict: Historical prices for the stock and market index.
    """
    api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

    # Fetch stock data
    stock_url = f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={api_key}'
    market_url = f'https://www.alphavantage.co/query?function={function}&symbol={market_index}&apikey={api_key}'

    stock_response = requests.get(stock_url).json()
    market_response = requests.get(market_url).json()

    return stock_response, market_response