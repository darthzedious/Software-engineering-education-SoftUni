from django import forms

from financeDjango.home_menu_app.models import User


class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                # 'class': 'form-control',
                'placeholder': 'Username',
            }
        )
    )

    password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                # 'class': 'form-control',
                'placeholder': 'Password',

            }
        )
    )
