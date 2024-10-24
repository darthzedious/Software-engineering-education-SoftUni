from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tatsyRecipes.profile_app.forms import CreateProfileForm
from tatsyRecipes.profile_app.models import Profile


# Create your views here.
class CreateProfileView(CreateView):
    model = Profile
    template_name = 'profile/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('catalogue')