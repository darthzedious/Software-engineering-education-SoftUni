from django.urls import path


from financeDjango.shares_app.stocks_view import (calculate_preferences_shares_price, \
                                                  calculate_ordinary_shares_price, calculate_return_on_equity,
                                                  calculate_growth_rate_of_dividends,
                                                  get_fundamental_stock_data, get_live_stock_price,
                                                  get_top_10_stock_prices, calculate_beta_coefficient,calculate_capm)

urlpatterns = [
    path('preference-shares/', calculate_preferences_shares_price, name='preference_shares'),
    path('ordinary-shares/', calculate_ordinary_shares_price, name='ordinary_shares'),
    path('return-on-equity/', calculate_return_on_equity, name='return_on_equity'),
    path('growth-rate/', calculate_growth_rate_of_dividends, name='growth_rate'),
    path('stock-data/', get_fundamental_stock_data, name='stock_data'),
    path('live-stock-price/', get_live_stock_price, name='stock_price'),
    path('top-10-stocks/', get_top_10_stock_prices, name='top_10_stocks'),
    path('calculate-beta', calculate_beta_coefficient, name='calculate_beta'),
    path('calculate_capm/', calculate_capm, name='calculate_capm'),

]