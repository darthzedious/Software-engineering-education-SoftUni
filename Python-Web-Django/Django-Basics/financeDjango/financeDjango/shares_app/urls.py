from django.urls import path


from financeDjango.shares_app.stocks_view import  calculate_preferences_shares_price, \
    calculate_ordinary_shares_price, calculate_return_on_equity

urlpatterns = [
    path('preference-shares/', calculate_preferences_shares_price, name='preference_shares'),
    path('ordinary-shares/', calculate_ordinary_shares_price, name='ordinary_shares'),
    path('return-on-equity/', calculate_return_on_equity, name='return_on_equity'),
]