from django.urls import path

from worldOfSpeed.base.views import home_page

urlpatterns = [
    path('', home_page, name='home'),
]