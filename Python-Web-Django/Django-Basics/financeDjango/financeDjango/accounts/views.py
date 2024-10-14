from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from financeDjango.accounts.forms import LoginForm, RegisterForm


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # redirect to homepage after successful login
            else:
                messages.error(request, "Invalid username or password")
    else:
        form = LoginForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts_templates/log_in.html', context)

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # redirect to homepage after successful registration
    else:
        form = RegisterForm()

    context = {
        'form': form,
    }

    return render(request, 'accounts_templates/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')


def load_profile(request):
    return render(request, 'accounts_templates/user_profile.html')