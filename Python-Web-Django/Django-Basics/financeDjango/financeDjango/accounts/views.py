from django.contrib.auth import  login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import , CreateView, DetailView

from financeDjango.accounts.forms import LoginForm, RegisterForm

UserModel = get_user_model()
# Create your views here.
# def login_view(request):
#     if request.method == "POST":
#         form = LoginForm(request, data=request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')  # redirect to homepage after successful login
#             else:
#                 messages.error(request, "Invalid username or password")
#     else:
#         form = LoginForm()
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'accounts_templates/log_in.html', context)

class UserLoginView(LoginView):
    template_name = 'accounts_templates/log_in.html'

# def register_view(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('profile')  # redirect to homepage after successful registration
#     else:
#         form = RegisterForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'accounts_templates/register.html', context)

class UserRegisterView(CreateView):
    model = UserModel
    form_class = RegisterForm
    template_name = 'accounts_templates/register.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)

        return response

def logout_view(request):
    logout(request)
    return redirect('home')


class LoadProfile(DetailView):
    template_name = 'accounts_templates/user_profile.html'