from django.urls import path

from financeDjango.home_menu_app.views import home_view, stock_operations_menu, log_in_view, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('shares-opeartions/', stock_operations_menu, name='stock_operations_menu'),
    path('register/', register_view, name='register'),
    path('login/', log_in_view, name='login'),
]