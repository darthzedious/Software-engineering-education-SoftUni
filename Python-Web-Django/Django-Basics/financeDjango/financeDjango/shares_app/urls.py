from django.urls import path


from financeDjango.shares_app.views.home_view import home, calculate_preferences_shares_price

urlpatterns = [
    path('', home, name='home'),
    path('preference-shares/', calculate_preferences_shares_price, name='preference_shares'),
]