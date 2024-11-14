from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

from financeDjango.accounts.models import Profile
from financeDjango.mixins import PlaceholderMixin

UserModel = get_user_model()

class RegisterForm(PlaceholderMixin, UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ['username','email']


class AppUserChangeForm(PlaceholderMixin, UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel

class ProfileEditForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', )

class LoginForm(PlaceholderMixin, AuthenticationForm):
    username = forms.CharField(label="Username or Email")