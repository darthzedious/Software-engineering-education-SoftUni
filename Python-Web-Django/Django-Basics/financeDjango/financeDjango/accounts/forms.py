from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

UserModel = get_user_model()

class RegisterForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username','email']


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username or Email")

class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel
