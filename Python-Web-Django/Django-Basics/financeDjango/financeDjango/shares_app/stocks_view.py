import os
import numpy as np
from django.shortcuts import render
import requests

from financeDjango.shares_app.forms import PreferencesSharesForm, OrdinarySharesPrice, ReturnOnEquityForm, \
    GrowthRateOfDividendsForm
from financeDjango.shares_app.helpers import fetch_stock_price, fetch_historical_data


def calculate_preferences_shares_price(request):
    result = None

    if request.method == 'POST':
        form = PreferencesSharesForm(request.POST)
        if form.is_valid():
            dividends = form.cleaned_data['dividends']
            rate_of_return = form.cleaned_data['rate_of_return']

            try:
                result = dividends / rate_of_return
            except (ValueError, ZeroDivisionError):
                result = "Invalid input. Please enter a valid number."
    else:
        form = PreferencesSharesForm()

    context = {
        'operation_name': 'Preference Shares Price',
        'form': form,
        'result': result,
    }


    return render(request, 'shares_templates/calculations.html', context)

def calculate_ordinary_shares_price(request):
    result = None

    if request.method == "POST":
        form = OrdinarySharesPrice(request.POST)
        if form.is_valid():
            d = form.cleaned_data['dividends']
            r = form.cleaned_data['rate_of_return']
            g = form.cleaned_data['growth_rate']

            try:
                if r <= g:
                    raise ValueError("The required rate of return must be greater than the growth rate.")
                result = round(d / (r - g), 2)

            except (ValueError, TypeError):
                result = "Invalid input. Please enter a valid number."
    else:
        form = OrdinarySharesPrice()

    context = {
        'operation_name': 'Ordinary Shares Price',
        'form': form,
        'result': result,
    }

    return render(request, 'shares_templates/calculations.html', context)


def calculate_return_on_equity(request):
    result = None

    if request.method =="POST":
        form = ReturnOnEquityForm(request.POST)
        if form.is_valid():
            net_profit = form.cleaned_data['net_profit']
            equity_capital = form.cleaned_data['equity_capital']

            try:
                result =round(net_profit / equity_capital, 4)
            except (ValueError, TypeError):
                result = "Invalid input. Please enter a valid number."
    else:
        form = ReturnOnEquityForm()

    # if request.method == 'POST':
    #     try:
    #         net_profit = float(request.POST.get('net_profit'))
    #         equity_capital = float(request.POST.get('equity_capital'))
    #
    #         result =round(net_profit / equity_capital, 4)
    #     except (ValueError, TypeError):
    #         result = "Invalid input. Please enter a valid number."

    context = {
        'operation_name': 'Calculate Return on Equity',
        'form': form,
        'result': result,
    }

    return render(request, 'shares_templates/calculations.html', context)


def calculate_growth_rate_of_dividends(request):
    """Retention Ratio (ki): The proportion of earnings a company retains for reinvestment,
     calculated as the percentage of net profit that is not distributed as dividends.
    The complement, 1 − ki, represents the Payout Ratio,
     or the portion of net income paid to shareholders as dividends."""


    result = None

    if request.method == 'POST':
        form = GrowthRateOfDividendsForm(request.POST)
        if form.is_valid():
            net_profit = form.cleaned_data['net_profit']
            equity_capital = form.cleaned_data['equity_capital']
            ki = form.cleaned_data['retention_ratio']
            try:
                roe = round(net_profit / equity_capital, 4)

                result = round(roe * (1 - ki), 4)

            except (ValueError, TypeError):
                result = "Invalid input. Please enter a valid number."
    else:
        form = GrowthRateOfDividendsForm()


    context ={
        'operation_name': 'Calculate Growth Rate of Dividends',
        'form': form,
        'result': result,
    }

    return render(request, 'shares_templates/calculations.html', context)



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
    result = None
    rf = None
    rm = None
    beta = None

    if request.method == 'POST':
        try:
            rf = float(request.POST.get('rf'))
            rm = float(request.POST.get('rm'))
            beta = float(request.POST.get('beta'))

            result = rf + beta * (rm - rf)
        except (ValueError, TypeError):
            result = "Invalid input. Please enter a valid number."

    context = {
        'operation_name': 'Capital Asset Pricing Model (CAPM)',
        'input_fields': [
            {'name': 'rf', 'label': 'Risk-free rate', 'description': 'Risk-free rate (e.g., 0.03 for 3%):',
             'value': rf, 'placeholder': 'Enter Risk-free rate'},
            {'name': 'rm', 'label': 'Expected market return',
             'description': 'Expected market return (e.g., 0.08 for 8%):', 'value': rm,
             'placeholder': 'Enter expected market return'},
            {'name': 'beta', 'label': 'Beta coefficient of the asset',
             'description': 'Beta of the asset (e.g., 1.2):', 'value': beta,
             'placeholder': 'Beta coefficient of the asset'},

        ],
        'result': result,

    }

    return render(request, 'shares_templates/calculate_shares_prices.html', context=context)
