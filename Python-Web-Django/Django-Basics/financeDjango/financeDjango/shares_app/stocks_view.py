import os

import numpy as np
from django.core.exceptions import ValidationError
from django.shortcuts import render
import requests
from financeDjango.shares_app.helpers import fetch_stock_price, fetch_historical_data


def calculate_preferences_shares_price(request):
    result = None
    div = None
    r = None

    if request.method == 'POST':
        try:
            div = float(request.POST.get('div'))
            r = float(request.POST.get('r'))

            result = div / r

        except (ValueError, TypeError):
            result = "Invalid input. Please enter a valid number."


    context = {
        'operation_name': 'Preferences Shares Price',
        'input_fields': [
            {'name': 'div', 'label': 'Dividends', 'description': 'Enter the dividend of the preference share:', 'value': div, 'placeholder': 'Enter dividend'},
            {'name': 'r', 'label': 'Rate of return', 'description': 'Enter the required rate of return (as a decimal, e.g., 0.08 for 8%):', 'value': r, 'placeholder': 'Enter rate of return'}
        ],
        'result': result,

    }

    return render(request, 'shares_templates/calculate_shares_prices.html', context)

def calculate_ordinary_shares_price(request):
    result = None
    error_message = None
    d1 = None
    r = None
    g = None

    # Check if the request is a POST request
    if request.method == 'POST':  # Fix typo here
        try:
            # Get the inputs from the form
            d1 = float(request.POST.get('d1'))
            r = float(request.POST.get('r'))
            g = float(request.POST.get('g'))

            # Validate: r must be greater than g
            if r <= g:
                raise ValueError("The required rate of return must be greater than the growth rate.")

            # Perform the calculation: Price = d1 / (r - g)
            result = round(d1 / (r - g), 2)

        except (ValueError, TypeError) as e:
            # Handle invalid input or calculation errors
            result = "Invalid input. Please enter a valid number."
            # error_message = str(e)

    # Prepare the context for rendering
    context = {
        'operation_name': 'Calculate Ordinary Shares Price',
        'input_fields': [
            {'name': 'd1', 'label': 'Expected Dividend', 'description': 'Enter the expected dividend in the next period:', 'value': d1, 'placeholder': 'Enter expected dividend'},
            {'name': 'r', 'label': 'Rate of Return', 'description': 'Enter the required rate of return (as a decimal, e.g., 0.08 for 8%;The required rate of return must be greater than the growth rate.):', 'value': r, 'placeholder': 'Enter rate of return'},
            {'name': 'g', 'label': 'Growth Rate', 'description': 'Enter the growth rate of dividends (as a decimal, e.g., 0.02 for 2%):', 'value': g, 'placeholder': 'Enter growth rate'},
        ],
        'result': result,
        'error_message': error_message
    }

    return render(request, 'shares_templates/calculate_shares_prices.html', context)


def calculate_return_on_equity(request):

    net_profit = None
    equity_capital = None
    result = None

    if request.method == 'POST':
        try:
            net_profit = float(request.POST.get('net_profit'))
            equity_capital = float(request.POST.get('equity_capital'))

            result =round(net_profit / equity_capital, 4)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter a valid number."



    context = {
        'operation_name': 'Calculate Return on Equity',
        'input_fields': [
            {'name': 'net_profit', 'label': 'Net Profit',
             'description': 'Enter the net profit of the company:', 'value': net_profit,
             'placeholder': 'Enter expected net profit of the company:'},
            {'name': 'equity_capital', 'label': 'Equity Capital',
             'description': 'Enter the equity capital of the company:',
             'value': equity_capital, 'placeholder': 'Enter equity capital of the company:'},
        ],
        'result': result,
    }

    return render(request, 'shares_templates/calculate_shares_prices.html', context)


def calculate_growth_rate_of_dividends(request):
    """Retention Ratio (ki): The proportion of earnings a company retains for reinvestment,
     calculated as the percentage of net profit that is not distributed as dividends.
    The complement, 1 − ki, represents the Payout Ratio,
     or the portion of net income paid to shareholders as dividends."""

    net_profit = None
    equity_capital = None
    ki = None
    result = None
    # roe = None

    if request.method == 'POST':
        try:
            net_profit = float(request.POST.get('net_profit'))
            equity_capital = float(request.POST.get('equity_capital'))
            ki = float(request.POST.get('ki'))
            roe = round(net_profit / equity_capital, 4)

            result = round(roe * (1 - ki), 4)

        except (ValueError, TypeError):
            result = "Invalid input. Please enter a valid number."


    context ={
        'operation_name': 'Calculate Growth Rate of Dividends',
        'input_fields': [
            {'name': 'net_profit', 'label': 'Net Profit',
             'description': 'Enter the net profit of the company:', 'value': net_profit,
             'placeholder': 'Enter expected net profit of the company:'},
            {'name': 'equity_capital', 'label': 'Equity Capital',
             'description': 'Enter the equity capital of the company:',
             'value': equity_capital, 'placeholder': 'Enter equity capital of the company:'},
            {'name': 'ki', 'label': 'Ki',
             'description': 'Enter the Retention Ratio (Ki) of the company:', 'value': ki, 'placeholder': 'Enter "Ki" of the company:'},
        ],
        'result': result,
    }

    return render(request, 'shares_templates/calculate_shares_prices.html', context)



def get_fundamental_stock_data(request):
    symbol = request.GET.get('symbol')
    stock_data = None
    error_message = None

    # Check if the symbol parameter is provided
    if symbol:
        api_key = os.getenv('ALPHA_VANTAGE_API_KEY')

        if not api_key:
            error_message = 'API key is missing. Please set the API key.'
        else:
            url = f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={api_key}'

            try:
                response = requests.get(url)
                data = response.json() # => If the API response is valid, data will be a dictionary that can be further processed.

                # Check if the response contains data
                if data and 'Symbol' in data:
                    stock_data = data
                else:
                    error_message = 'Error retrieving data. Please check the symbol or API key.'

            except requests.RequestException as e:
                error_message = f'Error retrieving data: {str(e)}'

    context = {
        'symbol': symbol,
        'stock_data': stock_data,
        'error_message': error_message,
    }

    return render(request, 'shares_templates/fundamental_stock_data.html', context)


def get_live_stock_price(request):
    """
    Django view to get the live stock price for an individual symbol.
    """
    symbol = request.GET.get('symbol', None)
    stock_price = None
    error_message = None

    if symbol:
        stock_price = fetch_stock_price(symbol)
        if stock_price is None:
            error_message = f"Error retrieving price for symbol {symbol}."

    context = {
        'symbol': symbol,
        'stock_price': stock_price,
        'error_message': error_message
    }

    return render(request, 'shares_templates/live_stock_price.html', context=context)


def get_top_10_stock_prices(request):
    """
    Django view to get live prices for the top 10 stocks.
    """
    top_10_symbols = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'BRK.B', 'NVDA', 'META', 'JPM', 'JNJ']
    stock_prices = {}
    error_message = None

    for symbol in top_10_symbols:
        price = fetch_stock_price(symbol)
        if price is not None:
            stock_prices[symbol] = price
        else:
            error_message = f"Error retrieving data for {symbol}."

    context = {
        'stock_prices': stock_prices,
        'error_message': error_message
    }

    return render(request, 'shares_templates/top_10_shares.html', context)

def calculate_beta_coefficient(request):
    symbol = request.GET.get('symbol')
    beta = None
    error_message = None

    if symbol:
        stock_data, market_data = fetch_historical_data(symbol)

        try:
            # Extract closing prices and calculate returns
            stock_prices = []
            market_prices = []

            # Assume we have monthly adjusted closing prices
            if "Monthly Adjusted Time Series" in stock_data and "Monthly Adjusted Time Series" in market_data:
                stock_series = stock_data["Monthly Adjusted Time Series"]
                market_series = market_data["Monthly Adjusted Time Series"]

                for date in stock_series:
                    if date in market_series:
                        stock_prices.append(float(stock_series[date]["5. adjusted close"]))
                        market_prices.append(float(market_series[date]["5. adjusted close"]))

                # Convert to returns
                stock_returns = np.diff(stock_prices) / stock_prices[:-1]
                market_returns = np.diff(market_prices) / market_prices[:-1]

                # Calculate beta
                beta = np.cov(stock_returns, market_returns)[0][1] / np.var(market_returns)

            else:
                error_message = "Error retrieving data. Please check the symbol or API key."

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"

    context = {
        'symbol': symbol,
        'beta': beta,
        'error_message': error_message
    }

    return render(request, 'shares_templates/calculate_beta.html', context)


def calculate_capm(request):
    """
                Calculate the expected return of an asset using the Capital Asset Pricing Model (CAPM).

                Args:
                    rf (float): Risk-free rate (e.g., 0.03 for 3%).
                    beta (float): Beta of the asset (e.g., 1.2).
                    rm (float): Expected market return (e.g., 0.08 for 8%).

                Returns:
                    float: Expected return of the asset.
                """
    #may use the first template
    pass
