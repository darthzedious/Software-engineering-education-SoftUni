from django.urls import path

from FurryFunnies.author_app import views

urlpatterns = [
    path('create/', views.CreateAuthorView.as_view(), name='create-author'),
    path('details/', views.DetailsAuthorView.as_view(), name='details-author'),
    path('edit/', views.edit_profile, name='edit-author'),
    path('delete/', views.AuthorDeleteView.as_view(), name='delete-author'),
]
