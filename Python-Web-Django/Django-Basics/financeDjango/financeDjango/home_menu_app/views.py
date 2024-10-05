from django.contrib.auth import login as auth_login, logout  # Import login function
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils import timezone

from financeDjango.home_menu_app.forms import LoginForm, RegisterForm
from financeDjango.home_menu_app.models import User


# Create your views here.
def home_view(request):
    print("Is user authenticated?", request.user.is_authenticated)
    return render(request, 'home_menu/home.html')

def stock_operations_menu(request):
    return render(request, 'home_menu/stock_shares_operation_menu.html')

def log_out_view(request):
    return render(request, 'home_menu/home.html')


def log_in_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if check_password(password, user.password):

                    auth_login(request, user)  # Log the user in
                    user.last_login = timezone.now()  # Set last_login time
                    user.save()  # Save user instance to the database
                    messages.success(request, 'Login successful!')

                    return redirect('home')  # Redirect to the homepage after login
                else:
                    messages.error(request, 'Invalid username or password.')
            except User.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'home_menu/log_in.html', context)

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])  # Hash the password
            user.save()  # Save the user instance to the database

            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page after registration

        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'home_menu/register.html', context)

def logout_view(request):
    logout(request)  # This will work with your custom user model
    return redirect('home')