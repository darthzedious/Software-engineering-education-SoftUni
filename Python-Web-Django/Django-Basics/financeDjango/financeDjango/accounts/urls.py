from django.urls import path

from financeDjango.accounts.views import register_view, logout_view, login_view, load_profile

urlpatterns = [

    path('register/', register_view, name='register'),

    path('login/', login_view, name='login'),

    path('logout/', logout_view, name='logout'),
    path('user/', load_profile, name='profile'),
]