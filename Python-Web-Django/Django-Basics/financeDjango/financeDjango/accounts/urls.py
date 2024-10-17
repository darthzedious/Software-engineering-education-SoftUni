from django.urls import path

from financeDjango.accounts import views

urlpatterns = [

    path('register/', views.register_view, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),
    path('user/', views.LoadProfile.as_view(), name='profile'),
]