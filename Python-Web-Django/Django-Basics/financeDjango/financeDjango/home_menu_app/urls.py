from django.urls import path

from financeDjango.home_menu_app.views import home_view, stock_operations_menu

urlpatterns = [
    path('', home_view, name='home'),
    path('shares-opeartions/', stock_operations_menu, name='stock_operations_menu'),

]