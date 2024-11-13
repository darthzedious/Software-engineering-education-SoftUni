from django.urls import path

from financeDjango.accounts import views

urlpatterns = [

    path('register/', views.UserRegisterView.as_view(), name='register'),

    path('login/', views.UserLoginView.as_view(), name='login'),

    path('logout/', views.logout_view, name='logout'),
    path('user/', views.LoadProfile.as_view(), name='profile'),
]