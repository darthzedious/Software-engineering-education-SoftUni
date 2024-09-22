
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
        'div': div,
        'r': r,
        'preferences_shares_price': preferences_shares_price,

    }

    return render(request, 'shares_templates/preference_shares.html', context)