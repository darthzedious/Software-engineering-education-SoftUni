from django.urls import path

from financeDjango.home_menu_app.views import home_view, stock_operations_menu,  register_view, logout_view, login_view

urlpatterns = [
    path('', home_view, name='home'),
    path('shares-opeartions/', stock_operations_menu, name='stock_operations_menu'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]