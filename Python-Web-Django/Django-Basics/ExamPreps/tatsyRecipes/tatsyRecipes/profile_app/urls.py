from django.urls import path

from tatsyRecipes.profile_app.views import CreateProfileView

urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='create_profile'),
]