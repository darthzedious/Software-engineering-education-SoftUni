from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tatsyRecipes.common.urls')),
    path('recipe/', include('tatsyRecipes.recipe_app.urls')),
    path('profile/', include('tatsyRecipes.profile_app.urls')),
]
