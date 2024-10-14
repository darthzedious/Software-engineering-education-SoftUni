from django.contrib.auth import logout, login, authenticate  # Import login function
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from financeDjango.home_menu_app.forms import LoginForm, RegisterForm



# Create your views here.
def home_view(request):
    print("Is user authenticated?", request.user.is_authenticated)
    return render(request, 'home_menu/home.html')

def stock_operations_menu(request):
    return render(request, 'home_menu/stock_shares_operation_menu.html')


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # redirect to homepage after successful login
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'home_menu/log_in.html', context)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # redirect to homepage after successful registration
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'home_menu/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')