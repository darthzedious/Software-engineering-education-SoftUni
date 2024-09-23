
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'shares_templates/home.html')


def calculate_preferences_shares_price(request):
    preferences_shares_price = None
    div = None
    r = None

    if request.method == 'POST':
        try:
            div = float(request.POST.get('div'))
            r = float(request.POST.get('r'))

            preferences_shares_price = div / r

        except (ValueError, TypeError):
            preferences_shares_price = "Invalid input. Please enter a valid number."


    context = {
        'operation_name': 'Preferences Shares Price',
        'input_fields': [
            {'name': 'div', 'label': 'Dividends', 'description': 'Enter the dividend of the preference share:', 'value': div, 'placeholder': 'Enter dividend'},
            {'name': 'r', 'label': 'Rate of return', 'description': 'Enter the required rate of return (as a decimal, e.g., 0.08 for 8%):', 'value': r, 'placeholder': 'Enter rate of return'}
        ],
        'preferences_shares_price': preferences_shares_price,

    }

    return render(request, 'shares_templates/preference_shares.html', context)