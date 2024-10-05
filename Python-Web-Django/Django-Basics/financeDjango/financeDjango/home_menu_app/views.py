from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from financeDjango.home_menu_app.forms import LoginForm, RegisterForm


# Create your views here.
def home_view(request):
    return render(request, 'home_menu/home.html')

def stock_operations_menu(request):
    return render(request, 'home_menu/stock_shares_operation_menu.html')

def log_in_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home_view')
            else:
                messages.error(request, 'Invalid username or password')

    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'home_menu/log_in.html', context)

def register_view(request):
    if request.method =='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            messages.success(request, 'Registration successful! You are now logged in.')
            return redirect('home_view')
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }
    return render(request, 'home_menu/register.html', context)