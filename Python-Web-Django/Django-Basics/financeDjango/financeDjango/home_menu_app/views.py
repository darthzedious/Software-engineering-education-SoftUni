from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home_menu/home.html')

def stock_operations_menu(request):
    return render(request, 'home_menu/stock_shares_operation_menu.html')