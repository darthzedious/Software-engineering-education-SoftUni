from django.urls import path, include

from tatsyRecipes.recipe_app import views


urlpatterns = [
    path('catalogue/', views.CataloguePageView.as_view(), name='catalogue'),
    path('create/', views.RecipeCreateView.as_view(), name='create_recipe'),
    path('<int:recipe_id>/', include([
        path('details/', views.RecipeDetailsView.as_view(), name='recipe_details'),
        path('edit/', views.EditRecipeView.as_view(), name='recipe_edit'),
    ])),
]