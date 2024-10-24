from django import forms

from tatsyRecipes.profile_app.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['bio',]