from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from tatsyRecipes.recipe_app.forms import CreateRecipeForm
from tatsyRecipes.recipe_app.models import Recipe
from tatsyRecipes.utils.get_user import get_user


# Create your views here.
def catalogue_view(request):
    return render(request, 'recipe/catalogue.html')


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipe/create-recipe.html'
    form_class = CreateRecipeForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = get_user()
        return super().form_valid(form)
