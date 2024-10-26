

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from tatsyRecipes.recipe_app.forms import CreateRecipeForm, EditRecipeForm
from tatsyRecipes.recipe_app.models import Recipe
from tatsyRecipes.utils.get_user import get_user


class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'recipe/create-recipe.html'
    form_class = CreateRecipeForm
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.instance.author = get_user()
        return super().form_valid(form)

class CataloguePageView(ListView):
    model = Recipe
    template_name = 'recipe/catalogue.html'
    success_url = reverse_lazy('catalogue')

class RecipeDetailsView(DetailView):
    model = Recipe
    template_name = 'recipe/details-recipe.html'
    success_url = reverse_lazy('recipe_details')
    pk_url_kwarg = 'recipe_id'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingredients_list'] = self.object.ingredients.split(', ')
        return context

class EditRecipeView(UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    pk_url_kwarg = 'recipe_id'
    template_name = 'recipe/edit-recipe.html'
    success_url = reverse_lazy('catalogue')

