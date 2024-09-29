from django.urls import path


from financeDjango.shares_app.views.home_view import home, calculate_preferences_shares_price, \
    calculate_ordinary_shares_price, calculate_return_on_equity, stock_operations_menu

urlpatterns = [
    path('', home, name='home'),
    path('shares-opeartions/', stock_operations_menu, name='stock_operations_menu'),
    path('preference-shares/', calculate_preferences_shares_price, name='preference_shares'),
    path('ordinary-shares/', calculate_ordinary_shares_price, name='ordinary_shares'),
    path('return-on-equity', calculate_return_on_equity, name='return_on_equity'),
]