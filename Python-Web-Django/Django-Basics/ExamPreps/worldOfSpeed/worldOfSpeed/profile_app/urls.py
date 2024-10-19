from django.urls import path

from worldOfSpeed.profile_app.views import create_profile_page, edit_profile_page, delete_profile_page, \
    profile_details_page

urlpatterns = [
    path('create/', create_profile_page, name='create-profile'),
    path('edit/', edit_profile_page, name='edit-profile'),
    path('delete/', delete_profile_page, name='delete-profile'),
    path('details/', profile_details_page, name='profile-details'),
]

# •	http://localhost:8000/profile/create - Profile create page
# •	http://localhost:8000/profile/details/ - Profile details page
# •	http://localhost:8000/profile/edit/ - Profile edit page
# •	http://localhost:8000/profile/delete/ - Profile delete page
