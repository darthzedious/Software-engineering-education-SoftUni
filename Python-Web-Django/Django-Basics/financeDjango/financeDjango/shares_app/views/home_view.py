from django.core.exceptions import ValidationError
from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request, 'home_menu/home.html')

def stock_operations_menu(request):
    return render(request, 'home_menu/stock_shares_operation_menu.html')

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