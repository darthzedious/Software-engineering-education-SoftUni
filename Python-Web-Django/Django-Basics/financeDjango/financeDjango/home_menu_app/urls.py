from django.urls import path

from financeDjango.home_menu_app import views

urlpatterns = [
    path('',views.HomeView.as_view() , name='home'),
    path('shares-opeartions/', views.stock_operations_menu, name='stock_operations_menu'),
    path('future-value/', views.future_value_menu, name='future-value-menu'),

]