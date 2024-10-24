from django.urls import path

from tatsyRecipes.recipe_app import views

urlpatterns = [
    path('catalogue/', views.catalogue_view, name='catalogue'),
    path('create/', views.RecipeCreateView.as_view(), name='create_recipe'),
]