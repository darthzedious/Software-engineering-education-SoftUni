from django.urls import path, include

from worldOfSpeed.car_app.views import catalogue_page, create_car_page, car_details_page, edit_car_page, delete_car_page

urlpatterns = [
    path('catalogue/', catalogue_page, name='catalogue'),
    path('create/', create_car_page, name='create-car'),
    path('<int:pk>/', include([
        path('details/', car_details_page, name='car-details'),
        path('edit/', edit_car_page, name='edit-car'),
        path('delete/', delete_car_page, name='delete-car'),
    ]))
]


# •	http://localhost:8000/car/catalogue/ - Catalogue page
# •	http://localhost:8000/car/create/ - Car create page
# •	http://localhost:8000/car/<id>/details/ - Car details page
# •	http://localhost:8000/car/<id>/edit/ - Car edit page
# •	http://localhost:8000/car/<id>/delete/ - Car delete page
